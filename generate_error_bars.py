import pandas as pd
import seaborn as sns
from load_data import DataLoader 
import matplotlib.pyplot as plt


def generateErrorBars():
    loader = DataLoader()
    df = loader.load_data()

    if df is not None:
        
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 6))

        # Improved colors and thicker error bars
        sns.barplot(data=df, x="Scholarship holder", y="Curricular units 1st sem (grade)", 
                    ci=95, capsize=0.2, palette="coolwarm", errcolor="black", errwidth=2)

        plt.xlabel("Scholarship (1 - Yes, 0 - No)", fontsize=12, fontweight="bold")
        plt.ylabel("Average Grade (1st Semester)", fontsize=12, fontweight="bold")
        plt.title("Average Grade in 1st Semester by Scholarship", fontsize=14, fontweight="bold")

        plt.xticks(fontsize=11)
        plt.yticks(fontsize=11)

        # plt.show()
        plt.savefig("Error Bar Average Grade in 1st Semester by Scholarship.png", dpi=300, bbox_inches="tight")  

        
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 6))

        # Improved colors and thicker error bars
        sns.barplot(data=df, x="Gender", y="Age at enrollment", 
                    ci="sd", capsize=0.2, palette="coolwarm", errcolor="black", errwidth=2)

        plt.xlabel("Gender (0 = Male, 1 = Female)", fontsize=12, fontweight="bold")
        plt.ylabel("Average Age at Enrollment", fontsize=12, fontweight="bold")
        plt.title("Average Age at Enrollment by Gender", fontsize=14, fontweight="bold")

        plt.xticks(fontsize=11)
        plt.yticks(fontsize=11)

        # plt.show()
        plt.savefig("Error Bar Average Age at Enrollment by Gender.png", dpi=300, bbox_inches="tight")  

        pass        

    else:
        print("Cannot operate on empty data set.")
        
        
if __name__ == "__main__":
    generateErrorBars()