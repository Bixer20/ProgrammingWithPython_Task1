import numpy as np
import pandas as pd

class TestDataMapper:
    def __init__(self, test_data, selected_functions, training_data):
        self.test_data = test_data
        self.selected_functions = selected_functions
        self.training_data = training_data
        self.max_deviations = []
        for function_df in self.selected_functions:
            y_ideal = function_df.iloc[:, 1].values
            max_deviation = self.calculate_max_deviation(training_data, y_ideal, function_df)
            self.max_deviations.append(max_deviation)

    def map_test_data(self):
        """
        Map the test data to the selected ideal functions.
    
        Returns:
            list: A list of dictionaries containing 'x', 'y', 'ideal_function_id', and 'deviation' for each test data point.
        """
        mapped_data = []
        for _, row in self.test_data.iterrows():
            min_deviation = float('inf')
            ideal_function_id = None
            x = row['x']
            y = row['y']
            for function_df in self.selected_functions:
                for column in function_df.columns[1:]:  # Iterate over all columns except the first ('x')
                    y_ideal = np.interp(x, function_df.iloc[:, 0], function_df[column].values)
                    deviation = abs(y - y_ideal)
                    max_deviation = self.calculate_max_deviation(self.training_data, function_df[column].values, function_df)
                    if deviation <= max_deviation * np.sqrt(2) and deviation < min_deviation:
                        min_deviation = deviation
                        ideal_function_id = column
            if ideal_function_id is not None:
                mapped_data.append({'x': x, 'y': y, 'ideal_function_id': ideal_function_id, 'deviation': min_deviation})
        return mapped_data

    def calculate_max_deviation(self, data, y_ideal, function_df):
        """
        Calculate the maximum deviation between the training data and an ideal function.
    
        Args:
            data (pandas.DataFrame): Training data with columns 'x', 'y1', 'y2', 'y3', 'y4'.
            y_ideal (numpy.ndarray): Ideal function values.
            function_df (pandas.DataFrame): The DataFrame containing the ideal function column.
    
        Returns:
            float: Maximum deviation.
        """
        max_deviation = 0
        for y_train in data.columns[1:]:  # Iterate over all columns except 'x'
            y_train_values = data[y_train].values
            deviations = np.abs(y_train_values - y_ideal)
            max_deviation = max(max_deviation, np.max(deviations))
        return max_deviation
    