# Readme
This Python script uses the Pandas and Matplotlib libraries to plot air quality data from a CSV file. The script also includes functions for copying and manipulating the data in the CSV file.

## Getting started
To use this script, you will need to have Python installed on your computer. You will also need to install the Pandas and Matplotlib libraries. You can do this using pip, the Python package manager, by running the following commands in your terminal:

## Copy code
pip install pandas
pip install matplotlib

Once you have installed the required libraries, you can download the script and the CSV file to your computer.

## Usage
The script expects a CSV file named 'main.csv' in a subdirectory called 'data'. The script first makes a copy of 'main.csv' and saves it as 'data.csv' in the same directory. This copy is then manipulated to clean the data and make it suitable for plotting.

Once the data is cleaned, the script prompts the user to enter an ID. The script then filters the data based on the entered ID and plots the PM1, PM2.5, PM4, and PM10 values over time.

To run the script, navigate to the directory where the script is saved and enter the following command in your terminal:

## Copy code
python script.py
Functions
fileCopie()

This function makes a copy of 'main.csv' in the 'data' directory and saves it as 'data.csv' in the same directory.

## changeData()
This function reads the 'data.csv' file and performs several operations on the data to clean it and make it suitable for plotting. It converts the 'Time' column to a datetime object, rounds the datetime object to the nearest 10 minutes, and converts the 'id' column to only include the last part of the ID. The cleaned data is then saved back to 'data.csv'.

## getId()
This function simply prints a message to the console indicating that the data is being loaded.

## main()
This function calls the 'fileCopie()', 'getId()', and 'changeData()' functions to prepare the data for plotting. It then prompts the user to enter an ID, filters the data based on the entered ID, and plots the PM1, PM2.5, PM4, and PM10 values over time using Matplotlib. The plot is displayed in a new window.

## Conclusion
This Python script demonstrates how to use the Pandas and Matplotlib libraries to clean and plot data from a CSV file. The script also includes functions for copying and manipulating the data in the CSV file. With a few modifications, this script could be adapted to work with other CSV files containing time series data.