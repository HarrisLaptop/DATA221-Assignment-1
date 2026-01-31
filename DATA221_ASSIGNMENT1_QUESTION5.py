# Harris Khan
# January 30, 2026
# DATA221, Assignment 1, Question 5

# From the math package, import the constant pi
from math import pi

# Define function that returns the percentage of area covered by the circles when given their radii
def circle_area_coverage(radius_of_circle1, radius_of_circle2):

    # Check to see if the two inputs are valid, i.e. they are positive and they are integers
    if (radius_of_circle1 > 0 and radius_of_circle2 > 0 and
            radius_of_circle1 == int(radius_of_circle1) and
            radius_of_circle2 == int(radius_of_circle2)):

        # Calculate the area of both circles using the pi constant and the given radii
        area_of_circle1 = pi * radius_of_circle1 ** 2
        area_of_circle2 = pi * radius_of_circle2 ** 2

        # If the area of circle 1 is greater than circle 2,
        if area_of_circle1 > area_of_circle2:

            # Return the percentage that the area of circle 2 covers the area of circle 1
            return area_of_circle2 / area_of_circle1 * 100

        else: # Otherwise, since the area of circle 2 is greater than circle 1,

            # Return the percentage that the area of circle 1 covers the area of circle 2
            return area_of_circle1 / area_of_circle2 * 100

    # If the given inputs are not valid, return a message clarifying what the valid inputs are
    else:
        return "One or more of your inputs are invalid. Please enter positive integer values."

# Print the percentage of the larger circle’s area that can be covered by the smaller circle
print(circle_area_coverage(4, 3))