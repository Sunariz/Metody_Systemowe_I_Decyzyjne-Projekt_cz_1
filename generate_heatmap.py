import pandas as pd
import seaborn as sns
from load_data import DataLoader 
import matplotlib.pyplot as plt


def generateHeatmap():
    loader = DataLoader()
    df = loader.load_numerical_data()

    if df is not None:
        
        if not all(df.dtypes.apply(lambda x: x.kind in 'ifc')):  
            print("Dataset contains non-numeric values. Selecting only numerical columns.")
            df = df.select_dtypes(include=['number'])

        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=False, cmap="coolwarm", linewidths=0.5)

        plt.title("Heatmap of Feature Correlations", fontsize=18, weight='bold', pad=15)
        # plt.show()
        plt.savefig("Heatmap of Feature Correlations.png", dpi=300, bbox_inches="tight")  

    else:
        print("Cannot operate on empty data set.")

        
if __name__ == "__main__":
    generateHeatmap()