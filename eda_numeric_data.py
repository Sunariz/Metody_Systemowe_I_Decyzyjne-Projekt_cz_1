import pandas as pd
from load_data import DataLoader 


def analyzeNumericalData():
    loader = DataLoader()
    df = loader.load_numerical_data()

    if df is not None:
        stats = df.describe().T
        stats["5%"] = df.quantile(0.05)
        stats["95%"] = df.quantile(0.95) 
        stats["missing_values"] = df.isnull().sum()
        stats.to_csv("statistics_from_numerical_data.csv")
        print(stats)
    else:
        print("Cannot operate on empty data set.")


if __name__ == "__main__":
    analyzeNumericalData()