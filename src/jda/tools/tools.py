import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from matplotlib import cycler

def make_heatmap(data: pd.DataFrame):
    """Plot the heatmap of variables associations using Seaborn.

    Parameters
    ----------
    data: pd.DataFrame
        The dataset before performing train/test split.
    """
    fig = plt.figure(dpi=400)
    sns.heatmap(
        data.corr(), cmap="coolwarm", annot_kws={"size": 4}, annot=True, fmt=".2f"
    )


def calculate_mape(y_true:np.array, y_pred:np.array):
    """Calculates mean absolute percentage error. 
    
    Parameters
    ----------
    y_true: np.array
        The training labels of target value. 
        
    y_pred: np.array
        The predicted labels of target values."""
    
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return mape

def calculate_rmse(y_true, y_pred):
    """Calculates root mean squared error. 
    
    Parameters
    ----------
    y_true: np.array
        The training labels of target value. 
        
    y_pred: np.array
        The predicted labels of target values.
    """
    
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return rmse

def calculate_scatter_index(y_true, y_pred):
    """Calculates scatter index. 
    
    Parameters
    ----------
    y_true: np.array
        The training labels of target value. 
        
    y_pred: np.array
        The predicted labels of target values.
    """
        
    si = calculate_rmse(y_true, y_pred)/y_true.mean()
    return si

def plot_feature_importance(train_features, feature_importances):
    feature_importances = pd.DataFrame(
    {
        "feature": train_features, 
        "importance": feature_importances,
    }
    )
    feature_importances = feature_importances.sort_values(
    by="importance", ascending=True
    ).reset_index(drop=True)

    plt.barh(feature_importances["feature"], feature_importances["importance"])
    colors = cycler(
    "color", ["#EE6666", "#3388BB", "#9988DD", "#EECC55", "#88BB44", "#FFBBBB"]
    )
    plt.rc(
        "axes",
        facecolor="#E6E6E6",
        edgecolor="none",
        axisbelow=True,
        grid=True,
        prop_cycle=colors,
    )

    plt.rc("grid", color="w", linestyle="solid")
    plt.rc("xtick", direction="out", color="gray")
    plt.rc("ytick", direction="out", color="gray")
    plt.rc("patch", edgecolor="#E6E6E6")
    plt.rc("lines", linewidth=2)
    plt.rcParams["figure.dpi"] = 300
    plt.barh(feature_importances["feature"], feature_importances["importance"])
    plt.title("feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("features used")
