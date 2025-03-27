import pandas as pd

numerical_columns = ["Application order", "Age at enrollment", "Curricular units 1st sem (credited)", 
                     "Curricular units 1st sem (enrolled)", "Curricular units 1st sem (evaluations)", 
                     "Curricular units 1st sem (approved)", "Curricular units 1st sem (grade)",
                     "Curricular units 1st sem (without evaluations)", "Curricular units 2nd sem (credited)",
                     "Curricular units 2nd sem (enrolled)", "Curricular units 2nd sem (evaluations)", 
                     "Curricular units 2nd sem (approved)", "Curricular units 2nd sem (grade)", 
                     "Curricular units 2nd sem (without evaluations)", "Unemployment rate", "Inflation rate", "GDP"]
categorical_columns = ["Marital status", "Application mode", "Course", "Daytime/evening attendance",
                       "Previous qualification", "Nacionality", "Mother's qualification", "Father's qualification",
                       "Mother's occupation", "Father's occupation", "Displaced", "Educational special needs", 
                       "Debtor", "Tuition fees up to date", "Gender", "Scholarship holder", "International", "Target"]
    

class DataLoader:
    
    def __init__(self):
        self.file_path = "dataset.csv"
    
    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            print("Data has been successfully read")
            return data
        except Exception as e:
            print(f"Error while reading the data: {e}")
            return None
    
    def load_numerical_data(self):
        data = self.load_data()
        if data is not None:
            for column in categorical_columns:
                if column in data.columns:
                    data.drop(columns=column, inplace=True)
        return data
    
    def load_categorical_data(self):
        data = self.load_data()
        if data is not None:
            for column in numerical_columns:
                if column in data.columns:
                    data.drop(columns=column, inplace=True)
        return data

def get_categorical_columns():
    return categorical_columns