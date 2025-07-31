import numpy as np

class FunctionSelector:
    def __init__(self, training_data, ideal_functions):
        self.training_data = training_data
        self.ideal_functions = ideal_functions

    def select_functions(self):
        """
        Select the four ideal functions that are closest to the noisy training functions.

        Returns:
            list: A list of pandas.DataFrame objects containing the selected ideal functions and the corresponding x values.
        """
        selected_functions = []
        for y_train in ['y1', 'y2', 'y3', 'y4']:
            y_train_values = self.training_data[y_train].values
            squared_deviations = []
            for i in range(1, 51):
                y_ideal = self.ideal_functions[f'y{i}'].values
                squared_dev = np.sum((y_train_values - y_ideal) ** 2)
                squared_deviations.append((i, squared_dev))

            squared_deviations.sort(key=lambda x: x[1])
            best_function_index = squared_deviations[0][0]
            selected_columns = [0] + [best_function_index]
            selected_function = self.ideal_functions.iloc[:, selected_columns]
            selected_functions.append(selected_function)
        print(type(selected_functions))
        return selected_functions
    