import pandas as pd

class DataLoader:
    def __init__(self, train_file, test_file, ideal_file):
        self.train_file = train_file
        self.test_file = test_file
        self.ideal_file = ideal_file

    def load_training_data(self):
        """
        Load training data from a csv file.

        Returns:
            pandas.DataFrame: Training data with columns 'X', 'Y1', 'Y2', 'Y3', 'Y4'.
            
        Raises:
            FileNotFoundError: If the file is not found.
            Exception: If any other error occurs while loading the data.

        """
        try:
            train_data = pd.read_csv(self.train_file)
            '''train_data = train_data.rename(columns={'y1 (training func)': 'y1',
                                                     'y2 (training func)': 'y2',
                                                     'y3 (training func)': 'y3',
                                                     'y4 (training func)': 'y4'})'''
            
            return train_data
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.train_file}' not found.")
        except Exception as e:
            raise Exception(f"Error loading training data: {e}")

    def load_test_data(self):
        """
        Load test data from a CSV file.

        Returns:
            pandas.DataFrame: Test data with columns 'x', 'y'.

        Raises:
            FileNotFoundError: If the file is not found.
            Exception: If any other error occurs while loading the data.
        """
        try:
            test_data = pd.read_csv(self.test_file, names=['x', 'y'])
            test_data['x'] = pd.to_numeric(test_data['x'], errors='coerce')
            test_data['y'] = pd.to_numeric(test_data['y'], errors='coerce')
            test_data.dropna(inplace=True)
            return test_data
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.test_file}' not found.")
        except Exception as e:
            raise Exception(f"Error loading test data: {e}")

    def load_ideal_functions(self):
        """
        Load ideal functions from a CSV file.

        Returns:
            pandas.DataFrame: Ideal functions with columns 'x', 'y1', 'y2', ..., 'y50'.

        Raises:
            FileNotFoundError: If the file is not found.
            Exception: If any other error occurs while loading the data.
        """
        try:
            ideal_functions = pd.read_csv(self.ideal_file)
            return ideal_functions
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.ideal_file}' not found.")
        except Exception as e:
            raise Exception(f"Error loading ideal functions: {e}")