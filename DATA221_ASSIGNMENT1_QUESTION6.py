# Harris Khan
# January 30, 2026
# DATA221, Assignment 1, Question 6

# Define a function that returns each integer's percentage of values less than or equal to it in a given list
def distribution_analysis_of_a_list(list_of_integers):

    # Define empty dictionary that will contain each integer's percentages
    dictionary_of_integer_percentages = {}

    # Sort the given list so that the keys in the dictionary will be automatically sorted
    sorted_list_of_integers = sorted(list_of_integers)

    # For every integer we want to compare to other integers in our sorted list,
    for integer_to_compare in sorted_list_of_integers:

        # Set counter for values less than or equal to the integer we are analyzing to 0
        less_than_or_equal_counter = 0

        # For every integer in our sorted list
        for integer_in_list in sorted_list_of_integers:

            # If the integer we are currently looking at it less than or equal to the integer we are comparing it to,
            if  integer_in_list <= integer_to_compare:
                # Increment our counter by 1
                less_than_or_equal_counter += 1

        # After we have counted the number of values less than or equal to the current integer,

        #  Calculate the percentage of integers in the list that are less than or equal to the current integer
        percentage = less_than_or_equal_counter / len(sorted_list_of_integers) * 100

        # Create a new key-pair item in our dictionary containing the integer and its corresponding percentage
        dictionary_of_integer_percentages[integer_to_compare] = percentage

    # Return the dictionary of integers in our list and their respective percentages
    return dictionary_of_integer_percentages

# Define an example list to be used in our function
example_list_of_integers = [3, 1, 4, 2, 3, 2, 2, 2]

# Print the distribution analysis of each integer in our example list
print(distribution_analysis_of_a_list(example_list_of_integers))