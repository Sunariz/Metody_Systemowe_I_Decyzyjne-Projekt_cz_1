import pandas as pd
import seaborn as sns
from load_data import DataLoader 
import matplotlib.pyplot as plt


def generateViolinplots():
    loader = DataLoader()
    df = loader.load_data()

    if df is not None:

        plt.figure(figsize=(8,6))
        sns.catplot(
            data=df, y="Curricular units 1st sem (without evaluations)", x="Application order", hue="Gender", kind="violin", cut=0, palette="pastel"
        )
        plt.title("Curricular units 1st sem (without evaluations) by Application order", fontsize=12)
        plt.xlabel("Application order", fontsize=12)
        plt.ylabel("Curricular units 1st sem (without evaluations)", fontsize=12)
        # plt.show()
        plt.savefig("Violinplot Curricular units 1st sem (without evaluations) by Application order.png", dpi=300, bbox_inches="tight")  


        plt.figure(figsize=(8,6))
        sns.catplot(
            data=df, y="Curricular units 1st sem (grade)", x="Target", hue="Gender", kind="violin", cut=0, palette="pastel"
        )
        plt.title("Curricular units 1st sem (grade) by Target", fontsize=12)
        plt.xlabel("Target", fontsize=12)
        plt.ylabel("Curricular units 1st sem (grade)", fontsize=12)
        # plt.show()
        plt.savefig("Violinplot Curricular units 1st sem (grade) by Target.png", dpi=300, bbox_inches="tight")  


    else:
        print("Cannot operate on empty data set.")
        
        
if __name__ == "__main__":
    generateViolinplots()