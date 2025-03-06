import pytest
from bike_sharing import Preprocessing, preprocessing
import pandas as pd

class TestPreprocessing():

    def test_add_lag_columns(self):
        X = pd.DataFrame({"cnt":[_ for _ in range(500)]})
        ppr = Preprocessing(data=X, target_column = "cnt", lag_n = 7)
        ppr.add_lags()
        dataframe = ppr.data
        assert list(dataframe.columns) == ["cnt"] + [f"cnt_lag{i+1}" for i in range(7)]

    def test_omit_columns(self):
        arbit_columns = ["a","b","c","d","e","g"]
        values = [_ for _ in range(500)]
        X = pd.DataFrame({i:values for i in arbit_columns})
        ppr = Preprocessing(data = X)
        ppr.omit_features = ["a","c","d"]
        ppr.omit_columns()
        dataframe = ppr.data
        assert list(dataframe.columns) == ["b","e","g"]
         

