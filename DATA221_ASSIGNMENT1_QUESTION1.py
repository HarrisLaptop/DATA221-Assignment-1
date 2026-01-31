# Harris Khan
# January 29, 2026
# DATA221, Assignment 1, Question 1

# Set that the product needs to pass for the program to end
threshold_value_to_pass = 1000

# Stores the current integer of the factorial multiplier
current_multiplier = 1

# Stores the value of our total factorial product
product_to_pass_threshold = 1

# While the product is less than the threshold value,
while product_to_pass_threshold <= threshold_value_to_pass:
    # Multiply our current product with the next consecutive integer
    current_multiplier += 1
    product_to_pass_threshold *= current_multiplier

# Print the threshold value, the product, and the integer that caused the product to exceed the threshold
print("The product that has passed the threshold value of " + str(threshold_value_to_pass) + " is " + str(product_to_pass_threshold))
print("The integer that caused the product to pass the threshold value is " + str(current_multiplier))