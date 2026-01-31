# Harris Khan
# January 29, 2026
# DATA221, Assignment 1, Question 4

# IMPORTANT NOTE: For the sake of visual simplicity, I have rounded each random value in the program to two decimals

# From the random package, import the random() function to let us pick a random number from 0 to 1
from random import random

# Define a list of 20 values between 0 and 1
values_between_0_and_1 = [round(random(), 2) for i in range(20)]

# Store a random value between 0 and 1 to compare against the values in the list defined above
random_value_x = round(random(), 2)

# Sort the values in our list of random values
values_between_0_and_1.sort()

# Define a list of values greater than or equal to our random_value_x
values_greater_than_random_value = []

# For every value in our sorted list
for value_in_list in values_between_0_and_1:

    # If the value is greater than or equal to our random_value_x
    if value_in_list >= random_value_x:

        # Append the value in our sorted list to a list of values that are greater than random_value_x
        values_greater_than_random_value.append(value_in_list)

# Print the sorted list
print("Sorted List: " + str(values_between_0_and_1))
# Print our random value x
print("Random Value x: " + str(random_value_x))
# Print the first value that was greater than or equal to our random_value_x (if such a value exists)
if len(values_greater_than_random_value) > 0:
    print("First value in sorted list greater than Random Value x: " + str(values_greater_than_random_value[0]))