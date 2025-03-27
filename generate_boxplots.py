import pandas as pd
import seaborn as sns
from load_data import DataLoader 
import matplotlib.pyplot as plt


def generateBoxplots():
    loader = DataLoader()
    df = loader.load_data()

    if df is not None:
        sns.set_style("whitegrid")

        plt.figure(figsize=(8,6))
        sns.boxplot(data=df, x="Target", y="Age at enrollment", palette="pastel")
        plt.title("Age at Enrollment by Target", fontsize=14)
        plt.xlabel("Target", fontsize=12)
        plt.ylabel("Age at Enrollment", fontsize=12)
        plt.savefig("Boxplot Age at Enrollment by Target.png", dpi=300, bbox_inches="tight")  
        # plt.show()
        
        plt.figure(figsize=(8,6))
        sns.boxplot(data=df, x="Target", y="Curricular units 1st sem (grade)", palette="pastel")
        plt.title("Curricular units 1st sem (grade) by Target", fontsize=14)
        plt.xlabel("Target", fontsize=12)
        plt.ylabel("Curricular units 1st sem (grade)", fontsize=12)
        # plt.show()
        plt.savefig("Boxplot Curricular units 1st sem (grade) by Target.png", dpi=300, bbox_inches="tight")  

        pass        

    else:
        print("Cannot operate on empty data set.")


if __name__ == "__main__":
    generateBoxplots()
