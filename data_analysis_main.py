from eda_numeric_data import analyzeNumericalData
from eda_categorical_data import analyzeCategoricalData

from generate_boxplots import generateBoxplots
from generate_error_bars import generateErrorBars
from generate_heatmap import generateHeatmap
from generate_histographs import generateHistographs
from generate_linear_regression import generateLinearRegression
from generate_violinplots import generateViolinplots

if __name__ == "__main__":
    analyzeNumericalData()
    analyzeCategoricalData()
    generateBoxplots()
    generateErrorBars()
    generateHeatmap()
    generateHistographs()
    generateLinearRegression()
    generateViolinplots()