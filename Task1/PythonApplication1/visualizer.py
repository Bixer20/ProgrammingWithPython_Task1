import numpy as np 
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Paired12  # Import the color palette
from bokeh.transform import factor_cmap

class Visualizer:
    def __init__(self, training_data, test_data, ideal_functions, selected_functions, test_data_mapper):
        self.training_data = training_data
        self.test_data = test_data
        self.ideal_functions = ideal_functions
        self.selected_functions = selected_functions
        self.test_data_mapper = test_data_mapper
        
    def plot_training_data(self):
        """
        Plot the training data.
        """
        p = figure(title="Training Data")
        colors = Paired12[:4]  # Get the colors from the palette
        source = ColumnDataSource(self.training_data)
        for i in range(1, 5):
            y_column = f'y{i}'
            line_color = colors[i-1]
            p.line('x', y_column, source=source, color=line_color, legend_label=f'y{i} (training func)')
        show(p)        

    def plot_ideal_functions(self):
        """
        Plot the ideal functions.
        """
        p = figure(title="Ideal Functions", x_axis_label='x', y_axis_label='y')
        colors = Paired12 * 5  # Get the colors from the palette

        source = ColumnDataSource(self.ideal_functions)
        for i in range(1, 51):
            y_column = f'y{i}'
            line_color = colors[i-1]
            p.line('x', y_column, source=source, color=line_color, legend_label=f'y{i} (ideal func)')
        show(p)   
        
    def plot_selected_ideal_functions(self):
        """
        Plot the mapped test data and the selected ideal functions.
        """
        # Combine all DataFrames in the list into a single DataFrame
        combined_df = pd.concat(self.selected_functions, axis=1)
    
        p = figure(title="selected Ideal Functions", x_axis_label='x', y_axis_label='y')
        colors = Paired12[:12]  # Get colors from the palette
    
        # Create a ColumnDataSource from the combined DataFrame
        source = ColumnDataSource(combined_df)
     
        # Plot each column as a separate line
        for i, col in enumerate(combined_df.columns):
            if col == 'x':
                continue  # Skip the 'x' column
            line_color = colors[i]
            p.line('x', col, source=source, color=line_color, legend_label=col)
        show(p) 
        
    def plot_test_data_mapping(self):
        """
        Plot the mapped test data and the selected ideal functions.
        """
        p = figure(title="Test Data Mapping", x_axis_label='x', y_axis_label='y')
        colors = Paired12[:12] # Get colors from the Paired12 palette
    
        # Create a color mapping dictionary
        color_mapping = {}
        for i, function_df in enumerate(self.selected_functions):
            for col in function_df.columns[1:]:
                color_mapping[col] = colors[i+1]
    
        # Plot the selected ideal functions
        for i, function_df in enumerate(self.selected_functions):
            for j, col in enumerate(function_df.columns[1:], start=1):
                line_color = colors[i+1]
                p.line('x', col, source=ColumnDataSource(function_df), color=line_color, legend_label=f'Selected Function {i+1}: {col}')
    
        # Plot the mapped test data
        mapped_data = self.test_data_mapper.map_test_data()
        mapped_data_df = pd.DataFrame(mapped_data)
        colors_for_points = [color_mapping[row['ideal_function_id']] for _, row in mapped_data_df.iterrows()]
        mapped_data_df['color'] = colors_for_points
        mapped_data_source = ColumnDataSource(mapped_data_df)
        p.circle('x', 'y', source=mapped_data_source, color='color', legend_label='Test Data')
    
        show(p)