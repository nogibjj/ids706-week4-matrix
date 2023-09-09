import pandas as pd
import matplotlib.pyplot as plt

def read_dataset(file_path):
    """
    Read dataset from the provided file path. Supports both CSV and Excel files.
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

def compute_summary_statistics(df, column_name):
    """
    Compute summary statistics (mean, median, standard deviation) for the specified column.
    """
    mean_value = df[column_name].mean()
    median_value = df[column_name].median()
    std_dev = df[column_name].std()
    
    return mean_value, median_value, std_dev

def generate_scatter_plot(df, x_col, y_col):
    """
    Generate scatter plot for the specified columns.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], color='blue', alpha=0.5)
    plt.title(f'Scatter plot of {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.tight_layout()
    # Save the scatter plot as an image
    plt.savefig('scatter_plot.png')
    plt.show()

def main():
    """
    Main function to execute the operations.
    """
    # Read dataset
    df = read_dataset("data/iris.csv")
    
    # Compute summary statistics
    column_name = "SepalLengthCm"
    mean, median, std_dev = compute_summary_statistics(df, column_name)
    print(f"Mean of {column_name}: {mean:.2f}")
    print(f"Median of {column_name}: {median:.2f}")
    print(f"Standard Deviation of {column_name}: {std_dev:.2f}")
    
    # Generate scatter plot
    generate_scatter_plot(df, "Id", column_name)

    
    # Generate a Markdown file
    with open('summary.md', 'w', encoding='utf-8') as f:
        f.write(f"# Summary Statistics for {column_name}\\n")
        f.write(f"- Mean: {mean}\\n")
        f.write(f"- Median: {median}\\n")
        f.write(f"- Standard Deviation: {std_dev}\\n")
        f.write("![Scatter Plot](scatter_plot.png)\\n")

if __name__ == "__main__":
    main()