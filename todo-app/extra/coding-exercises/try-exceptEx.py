                                # Coding Exercise 1 #
# The given code is incomplete. Your task is to continue that program. You need to:

# 1. calculate the percentage using the  value/total * 100 formula

# 2. print out, for example, "That is 40.0%" 

# The program should also print a message if the user doesn't enter a number for the "total value or for the "value":
 
try:
    # Prompt the user to enter the total value and convert it to a float
    total_value = float(input("Enter total value: "))
 
    # Prompt the user to enter the value and convert it to a float
    value = float(input("Enter value: "))
 
    # Calculate the percentage using the formula value/total_value * 100
    percentage = value / total_value * 100
 
    # Print the calculated percentage
    print(f"That is {percentage}%")
except ValueError:
    # Handle the case when the user doesn't enter a number
    print("You need to enter a number. Run the program again.")   
# ---------------------------------------------------------------------------------------------------
                                # Coding Exercise 2 #
# As you might know, it is not mathematically possible to divide a number by zero. Consequently, this is also not possible in Python either -you will get a ZeroDivisionError if you try:

# >>> 20 / 0
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# With that in mind, your task for this exercise is to extend the program you created in Exercise 1 by displaying a message to the user when they enter 0 for the "total value".
 
try:
    # Prompt the user to enter the total value
    total_value = float(input("Enter total value: "))  
    value = float(input("Enter value: "))  # Prompt the user to enter the value
    percentage = value / total_value * 100  # Calculate the percentage
    print(f"That is {percentage}%")  # Print the calculated percentage
except ValueError:
    # Handle the ValueError if the user doesn't enter a valid number
    print("You need to enter a number. Run the program again.")  
except ZeroDivisionError:
    # Handle the ZeroDivisionError if the total value is zero
    print("Your total value cannot be zero.") 
    
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
                                # Coding Exercise 3 #
# Loop over the colors items and print out the item in every loop only if the item is greater than 50. So, the output of your program would be:

# 98
# 54
# 54


# Solution #

colors = [11, 34, 98, 43, 45, 54, 54]
 
# Iterate over each color in the list
for color in colors:
    # Check if the color is greater than 50
    if color > 50:
        # Print the color if it satisfies the condition
        print(color)
        
# ---------------------------------------------------------------------------------------------------
