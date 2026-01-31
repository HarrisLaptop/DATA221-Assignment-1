# Harris Khan
# January 29, 2026
# DATA221, Assignment 1, Question 3

# Define a function that simply calculates Argument 1 (x) raised to the power of Argument 2 (y)
def calculate_exponent_of_pairs(x, y):
    return x ** y

# Define a list of pairs that will be used in our calculations
example_list_of_pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

# Define an empty list of valid calculations
list_of_valid_exponent_results = []

# For every pair in our list,
for pair_in_list in example_list_of_pairs:

    # If the exponent in the pair is greater than or equal to zero
    if pair_in_list[1] >= 0:
        # Append the result of the returned value of our function into the list of valid calculations
        list_of_valid_exponent_results.append(calculate_exponent_of_pairs(pair_in_list[0], pair_in_list[1]))

# Print the list of valid exponent results
print(list_of_valid_exponent_results)
