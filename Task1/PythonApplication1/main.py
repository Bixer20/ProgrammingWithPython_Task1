from data_loader import DataLoader
from database import Database
from function_selector import FunctionSelector
from test_mapper import TestDataMapper
from visualizer import Visualizer


def main():
    # Load data
    train_file = 'D:/IUBH/ProgrammingWithPython/Teams/Datasets1/train.csv'
    test_file = 'D:/IUBH/ProgrammingWithPython/Teams/Datasets1/test.csv'
    ideal_file = 'D:/IUBH/ProgrammingWithPython/Teams/Datasets1/ideal.csv'
    data_loader = DataLoader(train_file, test_file, ideal_file)
    training_data = data_loader.load_training_data()
    test_data = data_loader.load_test_data()
    ideal_functions = data_loader.load_ideal_functions()
    
    try:
        training_data = data_loader.load_training_data()
    except Exception as e:
        print(f"Error loading training data: {e}")
        return

    try:
        test_data = data_loader.load_test_data()
    except Exception as e:
        print(f"Error loading test data: {e}")
        return

    try:
        ideal_functions = data_loader.load_ideal_functions()
    except Exception as e:
        print(f"Error loading ideal functions: {e}")
        return

    print(ideal_functions.columns)

    # Set up database
    db = Database('data.db')
    db.create_tables()
    db.clear_tables()  # Clear existing data before loading new data
    
    # Load data into database
    db.load_training_data(training_data)
    db.load_ideal_functions(ideal_functions)

    # Select ideal functions
    function_selector = FunctionSelector(training_data, ideal_functions)
    selected_functions = function_selector.select_functions()



    # Map test data
    test_data_mapper = TestDataMapper(test_data, selected_functions, training_data)
    mapped_data = test_data_mapper.map_test_data()
    db.save_test_data(mapped_data)
    
    saved_mapped_data = db.get_test_data()
    print("Saved Mapped Data:")
    print(saved_mapped_data)
    # Print selected_functions
    #for i, function in enumerate(selected_functions):
    #    print(f"Selected Function {i+1}:")
    #    print(function)
    #    print()
    print(selected_functions)
    print()
    
    # Visualize data
    visualizer = Visualizer(training_data, test_data, ideal_functions, selected_functions, test_data_mapper)
    visualizer.plot_training_data()
    visualizer.plot_ideal_functions()
    visualizer.plot_selected_ideal_functions()
    visualizer.plot_test_data_mapping()


if __name__ == "__main__":
    main()