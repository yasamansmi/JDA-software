import logging
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
import matplotlib.pyplot as plt

from .preprocessing import Preprocessing
from .tools.tools import make_heatmap, calculate_mape, calculate_rmse, calculate_scatter_index


class RandomForest():
    
    def __init__(self, data, target_value = "cnt"):

        self.data: pd.DataFrame = data
        self.X_train: np.array = None
        self.X_test: np.array = None
        self.y_train: np.aray = None
        self.y_test: np.array = None
        self.train_features: list = None
        self.target_value: str = target_value
        self.y_pred = None

    def train_test_split(self, random_state: int = 123, test_size: float = 0.2):
        """splits the train and test dataset to create X_train,X_test, y_train, y_test arrays.

        Parameters
        ----------
        random_state: int
            random seed for deviding train and test.
        test_size: float
            proportion of data to be used for testing.
        """
        self.train_features = list(self.data.columns)
        self.train_features.remove(self.target_value)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.data[self.train_features].values,
            self.data[self.target_value].values,
            test_size=test_size,
            random_state=random_state,
        )
        

    def train_random_forest(
        self,
        random_state=123,
        n_estimators=10,
        max_features=None,
        max_depth="auto",
        min_samples_split=None,
        min_samples_leaf=1,
        bootstrap=True,
    ):

        """Initiaies the sklearn random forest instance and runs the training.

        Parameters
        ----------
        random_state: int
            random seed for initiating RandomForest model.

        n_estimators: int

        """
        model = RandomForestRegressor(n_estimators=10, random_state=random_state)
        model.fit(self.X_train, self.y_train)
        return model

    def test_model(self, model):
        """Tests the model using the test data.
        
        Parameters
        ----------
        model: sklearn.ensemble._forest.RandomForestRegressor
            RandomForestRegressor instance trained using sklearn.
        """
        self.y_pred = model.predict(self.X_test)
        mape = calculate_mape(self.y_test, self.y_pred)
        rmse = calculate_rmse(self.y_test, self.y_pred)
        si = calculate_scatter_index(self.y_test, self.y_pred)
        print(f"The model is created with a mean absolute percentge error of {mape:.2f}% and a root mean suqared of {rmse:.2f} and scatter index of {si:.2f}")
        return mape, rmse, si

    def cross_validation(
        self, n_iter: int=100, cv: int =3, verbose: int =2, random_state : int =123, n_jobs:int =-1
    ):
        """Performs corss validation on training data and yields the best model and parameters. 
        
        Parameters
        ----------
        n_iter: int
            Number of parameter settings that are sampled. 
            
        cv: int
            Determines the cross-validation splitting strategy. 
            
        verbose: int
            Controls the verbosity: the higher, the more messages.
        
        random_state: int
            random seed for [performing cross validation.         
            
        """
        n_estimators = [int(x) for x in np.linspace(10, 800, num=10)]
        max_features = ["auto", "sqrt"]
        max_depth = [int(x) for x in np.linspace(10, 70, num=7)]
        max_depth.append(None)
        min_samples_split = [2, 4]
        min_samples_leaf = [1, 3]
        bootstrap = [True, False]
        random_grid = {
            "n_estimators": n_estimators,
            "max_features": max_features,
            "max_depth": max_depth,
            "min_samples_split": min_samples_split,
            "min_samples_leaf": min_samples_leaf,
            "bootstrap": bootstrap,
        }
        rf = RandomForestRegressor()
        rf_random = RandomizedSearchCV(
            estimator=rf,
            param_distributions=random_grid,
            n_iter=60,
            cv=3,
            verbose=2,
            random_state=42,
            n_jobs=-1,
        )
        rf_random.fit(self.X_train, self.y_train)
        print(rf_random.best_params_)
        return rf_random.best_estimator_, rf_random.best_params_
    
    def inference(self, X: np.array, model):
        """Yields the forecasted value in the inference. 
        
        Parameters
        ----------
        X: np.array
            The feature array for forecasting. 
        """
        y_inference = model.predict(self.X)
        return y_inference
        