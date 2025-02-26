r"""
Preproceccing and feature engineering steps"""

__author__ = "Yasaman Samiee"
__email__ = "yasaman.msamiee@gmail.com"

import logging
import numpy as np
import pandas as pd



class Preprocessing():
    
    """ Class for performing preprocessing and feature engineering steps. 

    Parameters
    ----------
    data : pd.DataFrame
        Initial datafarme used for train and test. 
    target_column : str
        Name of the target column to be forecasted.
    
    """
    
    def __init__(self, data, target_column = "cnt", lag_n = 7):
        
        self.data : pd.DataFrame = data
        self.target_column : str = target_column
    
    def add_lags(self, lag_n) -> pd.DataFrame:
        """Add lags of the target variable to the dataframe and remove the initial null rows
        """

        for lag in range(lag_n):
            column_name = f"{self.target_column}_lag{lag+1}"
            self.data[column_name] = self.data[self.target_column].shift(lag + 1)
        self.data = self.data.iloc[lag_n:]
        
    def omit_columns(self, omit_features):
        """Omit columns that are not to be used in the training process. 
        """
        self.data.drop(omit_features,axis=1, inplace = True)
        
    def remove_nulls(self):
        
        """Removnig records with at leat one columns value of null
        """

        null_list = [sum(self.data[i].isna()) *100 / len(self.data) for i in self.data.columns]
        null_percent = all(i < 0.2 for i in null_list)
        if not null_percent: 
            logging.warn("Whatch Out! Too many records are being removed due to remove of nulls")
        self.data = self.data.dropna()
    

