# Harris Khan
# January 29, 2026
# DATA221, Assignment 1, Question 8

# Import the pandas package using the alias pd
import pandas as pd

# Use the given data in the form of a dictionary
given_data_of_numbers = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Create a dataframe using pandas and the data above
data_frame_of_numbers = pd.DataFrame(given_data_of_numbers)

# Create a new column "D" that is derived by multiplying the values of each column
data_frame_of_numbers["D"] = data_frame_of_numbers["A"] * data_frame_of_numbers["B"] * data_frame_of_numbers["C"]
print(data_frame_of_numbers)