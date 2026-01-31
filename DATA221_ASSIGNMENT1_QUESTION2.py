# Harris Khan
# January 29, 2026
# DATA221, Assignment 1, Question 2

# From pprint, import pprint (pretty printing) to format the dictionary when it is returned
from pprint import pprint

# Define function that takes a list of strings and returns a dictionary of information of each element
def information_of_strings_in_list(list_to_check):

    # Create an empty dictionary that will store the information for each string in the given list
    dictionary_of_string_information = {}

    # For every string in our list
    for string_within_list in list_to_check:

        # if the string is even,
        if len(string_within_list) % 2 == 0:
            # Create a new key with the value of a dictionary containing its length and an even parity
            dictionary_of_string_information[string_within_list] = {"length": len(string_within_list), "parity": "even"}

        else: # Otherwise, if the string is odd,
            # Create a new key with the value of a dictionary containing its length and an odd parity
            dictionary_of_string_information[string_within_list] = {"length": len(string_within_list), "parity": "odd"}

    # Return the dictionary containing information on each string in the given list
    return dictionary_of_string_information

# Create a sample list that we will use in our function
example_list_argument = ["Data", "Science", "221"]

# Pretty Print the returned value of our function when given the list above. The Pretty Print function will format the dictionary nicely as well.
pprint(information_of_strings_in_list(example_list_argument))