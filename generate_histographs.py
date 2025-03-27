import pandas as pd
import seaborn as sns
from load_data import DataLoader 
import matplotlib.pyplot as plt


def generateHistographs():
    loader = DataLoader()
    df = loader.load_data()

    if df is not None:

        sns.set_style("whitegrid")

        plt.figure(figsize=(10, 6))

        sns.histplot(data=df, x="Curricular units 1st sem (approved)", hue="Daytime/evening attendance",
                    multiple="stack", palette="coolwarm", bins=15, edgecolor="black")

        plt.title("Histogram of Curricular Units (1st Semester) Approved by Attendance Mode", fontsize=18, weight='bold')
        plt.xlabel("Curricular Units (1st Semester) Approved", fontsize=14)
        plt.ylabel("Count", fontsize=14)

        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()

        # plt.show()
        plt.savefig("Histogram of Curricular Units (1st Semester) Approved by Attendance Mode.png", dpi=300, bbox_inches="tight")  

        
        sns.set_style("whitegrid")

        plt.figure(figsize=(10, 6))

        sns.histplot(data=df, x="Target", hue="Gender", multiple="stack", palette="coolwarm", bins=15, edgecolor="black")

        plt.title("Histogram of Target by Gender", fontsize=18, weight='bold')
        plt.xlabel("Target", fontsize=14)
        plt.ylabel("Count", fontsize=14)

        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()

        # plt.show()
        plt.savefig("Histogram of Target by Gender.png", dpi=300, bbox_inches="tight")  


        sns.set_style("whitegrid")

        g = sns.displot(df, x="International", binwidth=1, kde=False, palette="coolwarm", discrete=True)

        plt.xticks([0, 1], ["No", "Yes"], fontsize=12)
        plt.yticks(fontsize=12)

        plt.title("Histogram of International Students", fontsize=18, weight='bold')
        plt.xlabel("International", fontsize=14)
        plt.ylabel("Count", fontsize=14)

        plt.tight_layout()

        # plt.show()
        plt.savefig("Histogram of International Students.png", dpi=300, bbox_inches="tight")  

    else:
        print("Cannot operate on empty data set.")


if __name__ == "__main__":
    generateHistographs()