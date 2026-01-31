# DATA221 Assignment 1, Question 1
- This file has a set threshold value of 1000 and uses a while loop to multiply consecutive integers starting from 1 to a product variable.
- Once the product is greater than the threshold value, the while loop stops, and the value of the product that passed the threshold value is printed. The value of the integer that caused the total product to pass the threshold value is also printed.

# DATA221 Assignment 1, Question 2
- This file defines a function that takes a list of strings and returns some information about each string in the form of a dictionary.
- The dictionary stores the keys as each string in the given list and the values as nested dictionaries containing information on the string's length and whether the string has an odd or even number of characters
- When printing the returned dictionary from the function, the Pretty Print function is used to format the dictionary nicely

# DATA221 Assignment 1, Question 3
- This file defines a function that takes in two numerical arguments and returns the first argument raised to the power of the second argument.
- After defining the function, a for loop is used to iterate through a list of pairs containing integers. If the second number in each pair is positive, the pair is passed into the function and appended to a list of valid results.

# DATA221 Assignment 1, Question 4
- This file takes a list of 20 random numbers from between 0 and 1 (and rounds them down to two decimals for visual simplicity) and one random variable x, also between 0 and 1.
- Afterwards, it sorts the list, then uses a for loop to find all values that are greater than or equal to the random variable x and puts those values in a separate list.
- Finally, the file prints the sorted list, the random variable x, and the first index of the list containing values greater than or equal to the random variable x (if any such values exist)

# DATA221 Assignment 1, Question 5
- This file defines a function that takes the radii of two circles and returns the percentage of how much area the smaller circle covers of the bigger circle.
- The function first checks if the given inputs are positive and are integers. Then calculates each circle's area. Then returns the percentage of how much area the smaller circle covers of the bigger circle.

# DATA221 Assignment 1, Question 6
- This file defines a function that takes in a list of integers and returns a dictionary, each integer's percentage of how prevalent it and other integers lower than it are in the list.
- The function first sorts the list before doing any calculations to ensure that the dictionary is automatically sorted by key.
- Each key is a unique value from the list. Each value is the percentage of elements in the list that are less than or equal to that key.

# DATA221 Assignment 1, Question 7
- This file defines a function that takes in any number of seconds and returns its time conversion in the format of Hours, Minutes, Seconds, AM/PM.
- First, the function determines whether the input is valid, that is, whether the given inputs positive and an integer.
- The function then calculates and returns the time of day based on the seconds given. If the given seconds exceed the number of seconds in a day (86400), the function simply "starts a new day" and only uses the remaining seconds after using the modulo operator.

# DATA221 Assignment 1, Question 8
- This file imports the pandas package using the alias pd and creates a data frame using the given data in the assignment instructions.
- The file then creates a new column that is derived by multiplying the values of the previous three columns. Then it prints the data frame.
