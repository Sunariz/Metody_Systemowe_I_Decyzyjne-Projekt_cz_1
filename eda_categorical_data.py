import pandas as pd
from load_data import *


def analyzeCategoricalData():
    loader = DataLoader()
    df = loader.load_categorical_data()

    if df is not None:
        missing_values = df.isnull().sum()
        unique_classes = df.nunique()
        

        stats = pd.DataFrame({
            'Missing Values': missing_values,
            'Unique Classes': unique_classes,
        })

        stats.to_csv("statistics_from_categorical_data.csv")

        columns = get_categorical_columns()
        class_proportions = ""
        for column in columns:
            class_proportions += str(df[column].value_counts(normalize=True)) +"\n\n"
        print(class_proportions)

        try:
            with open("class_proportions.txt", "w", encoding="utf-8") as file:
                file.write(class_proportions)
            print("Proportions saved to class_proportions.txt")
        except Exception as e:
            print(f"Error while saving the file: {e}")

    else:
        print("Cannot operate on empty data set.")


if __name__ == "__main__":
    analyzeCategoricalData()