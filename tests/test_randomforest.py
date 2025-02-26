import pytest
from jda import RandomForest
import pandas as pd
import numpy as np

class TestRandomForest:
    def test_train_test_split(self):
        values = [ _ for _ in range(50)]
        X = pd.DataFrame({column:values for column in ["f1","f2", "target"]})
        rf = RandomForest(data = X, target_value = "target")
        rf.train_test_split()
        assert len(rf.X_test) == 0.2*(len(rf.X_train)+len(rf.y_test))

    def test_test_model(self):
        values = np.array([ _+10 for _ in range(100)])
        X = pd.DataFrame({column:values for column in ["f1","f2", "target"]})
        rf = RandomForest(data = X, target_value = "target")
        rf.train_test_split()
        model = rf.train_random_forest()
        mape, rmse, si = rf.test_model(model)
        print("***mape******", mape)
        assert mape < 5



        



