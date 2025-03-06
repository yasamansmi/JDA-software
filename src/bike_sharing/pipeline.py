import pandas as pd
import os

from .preprocessing import Preprocessing
from .randomforest import RandomForest
from .tools.tools import plot_feature_importance



class Pipeline(RandomForest):

    """
    Class for running the pipline. Including preprocessing, optional hyperparameter
    tuning, training and inference.

    Patameters
    ----------
        path : string
            The path of the dataframe on which the training is done, by default path to the bikesharing dataset
        target_value : sting
            The name of the column of target variable.
        lags: int
            Number of lagged target values to be used in the modeling process
        cross_validation : bool
            If True, cross validation will run. (Takes time to run), default is Flase and the best parameters have been chosen before.
        cv: int
            The number of folds in cross validation, default is set to be 3
        n_inference: int
            Number of random points to choose from inital dataset to perform the inference.
        inference_input: pd.DataFrame
            A sample dataframe consisting of initial training features to perform the infernce on. 
        model: sklearn.ensemble._forest.RandomForestRegressor
            The trained random forest model.
        dataframe: pd.DataFrame
            dataframe used for training. Default is the hourly data from UCI repository. 
        omit_features: list
            The list of features to be omited from the dataset. default is ["dteday", "instant", "casual", "registered"]
        feature_importance: bool
            True for ploting the feature importance histogram, False for not plotting.default is True. 
    """

    def __init__(self):

        self.path = os.path.join(
            "..", "utils", "data", "Bike-Sharing-Dataset", "hour.csv"
        )
        self.target_value = "cnt"
        self.lags = 7
        self.cross_validation = False
        self.cv = 3
        self.n_inference = 10
        self.inference_input = None
        self.inference_output = None
        self.model = None
        self.dataframe = None
        self.omit_features = ["dteday", "instant", "casual", "registered"]
        self.feature_importance = True

    def run_training_pipeline(self):
        """ " Runs the preprocessing, tuning and training pipeline."""
        preprocessing = Preprocessing(pd.read_csv(self.path))
        preprocessing.add_lags(self.lags)
        preprocessing.omit_columns(self.omit_features)
        preprocessing.remove_nulls()
        self.dataframe = preprocessing.data
        rf = RandomForest(self.dataframe)
        rf.target_value = self.target_value
        self.inference_input = self.dataframe.sample(self.n_inference).drop(
            self.target_value, axis=1
        )
        rf.train_test_split()
        if self.cross_validation:
            cv_best_model, cv_best_params = rf.hyper_parameter_tuning()
            rf.test_model(cv_best_model)
            self.model = cv_best_model
        else:
            model = rf.train_random_forest()
            rf.test_model(model)
            self.model = model
        if self.feature_importance:
            plot_feature_importance(rf.train_features, self.model.feature_importances_)

    def run_inference(self):
        X_predict = self.model.predict(self.inference_input)
        self.inference_output = X_predict
        print("The predicted values are:", "\n", self.inference_output)
        


        



    
