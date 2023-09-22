# Matrix Testing Project for Fall 2023-706 ![CI](https://github.com/nogibjj/ids706-week4-matrix/actions/workflows/ci.yml/badge.svg)

## Objective
This project aims to implement matrix testing using Github actions across various Python versions. Given that different teams might use different versions of Python, there can be inconsistencies in how functions perform. Our matrix test ensures that functions behave as expected across these versions. We are testing the following Python versions:
- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11

## What's Inside
- Github action configurations (.yml)
- Makefile for build and test
- Requirements file for dependencies
- A main script (main.py)
- Test script for main (test_main.py)

## How to Proceed
1. Begin by cloning the template from the project of week2.
2. Adjust the Github actions to perform tests across the specified Python versions.
3. Ensure that each Python version is properly set up in the testing environment. Validate using main.py and test_main.py.

# The source code for the project is below

# Pandas Descriptive Statistics Project 

## Overview

This project aims to demonstrate the application of the Pandas library in Python for descriptive statistics. We use the popular Iris dataset to calculate and visualize statistical summaries.

## Features

- **Data Import**: Supports both CSV and Excel formats.
- **Descriptive Statistics**: Computes mean, median, and standard deviation.
- **Visualization**: Generates scatter plots for data visualization.

## Quick Start

1. Ensure you have Python and the required libraries installed.
2. Clone the repository or download the project files.
3. Navigate to the project directory.
4. Run the main script:
   ```
   python main.py
   ```
5. Check the output for summary statistics.
6. A scatter plot visualization will be generated and displayed.

## Visualization Preview

Here's a preview of the scatter plot generated using the Iris dataset:

[![Scatter Plot of Iris Dataset](scatter_plot.png)](scatter_plot.png)

## Contribute

Feel free to contribute to this project by reporting bugs, suggesting enhancements, or sending pull requests.