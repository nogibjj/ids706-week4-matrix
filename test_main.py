from main import read_dataset, compute_summary_statistics, generate_scatter_plot
import pandas as pd
import math

def test_read_dataset():
    test_data_csv = "data/iris.csv"
    df = read_dataset(test_data_csv)
    assert isinstance(df, pd.DataFrame), "Failed to read CSV dataset"

def test_compute_summary_statistics():
    test_data = {
        'Id': [1, 2, 3],
        'SepalLengthCm': [4.9, 5.1, 4.7]
    }
    df = pd.DataFrame(test_data)
    mean, median, std_dev = compute_summary_statistics(df, 'SepalLengthCm')

    
    assert math.isclose(mean, 4.9), f"Mean calculation ({mean}) is incorrect"
    assert math.isclose(mean, 4.9), f"Median calculation ({median}) is incorrect"
    assert math.isclose(std_dev, 0.2), f"Standard deviation calculation ({std_dev}) is incorrect"
    
def test_generate_scatter_plot():
    test_data = {
        'Id': [1, 2, 3],
        'SepalLengthCm': [4.9, 5.1, 4.7]
    }
    df = pd.DataFrame(test_data)
    try:
        generate_scatter_plot(df, 'Id', 'SepalLengthCm')
        assert True, "Scatter plot generation succeeded"
    except:
        assert False, "Scatter plot generation failed"

def test_main_functions():
    test_read_dataset()
    test_compute_summary_statistics()
    test_generate_scatter_plot()

if __name__ == "__main__":
    test_main_functions()