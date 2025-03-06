from bike_sharing import Pipeline
import matplotlib.pyplot as plt
import os


if __name__ == "__main__":
    p = Pipeline()
    p.path = os.path.join(
            "utils", "data", "Bike-Sharing-Dataset", "hour.csv"
        )
    p.lags = 3
    p.omit_features = [
        "dteday",
        "instant",
        "casual",
        "registered",
        "holiday",
        "weathersit",
        "windspeed",
        "weekday",
        "mnth",
        "atemp",
        "hum",
        "temp",
    ]
    p.run_training_pipeline()
    p.run_inference()
    plt.show()
