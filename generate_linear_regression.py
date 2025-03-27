import pandas as pd
import seaborn as sns
from load_data import DataLoader 
import matplotlib.pyplot as plt


def generateLinearRegression():
    loader = DataLoader()
    df = loader.load_data()

    if df is not None:
        
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 6))

        sns.lmplot(
            data=df, 
            x="Curricular units 1st sem (approved)", 
            y="Curricular units 2nd sem (approved)", 
            scatter_kws={"alpha": 0.5},  # Przezroczystość punktów
            line_kws={"color": "coral"},   # Kolor linii regresji
            height=7, aspect=1.2
        )

        plt.title("Linear Regression: 1st vs 2nd Semester Approved Units", fontsize=16, weight='bold')
        plt.xlabel("1st Semester Approved Units", fontsize=14)
        plt.ylabel("2nd Semester Approved Units", fontsize=14)

        # plt.show()
        plt.savefig("Linear Regression 1st vs 2nd Semester Approved Units.png", dpi=300, bbox_inches="tight")  


    else:
        print("Cannot operate on empty data set.")
        
        
if __name__ == "__main__":
    generateLinearRegression()