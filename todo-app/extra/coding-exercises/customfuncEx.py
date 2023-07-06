                                        # Coding Exercise 1 #
# Create a liters_to_m3 function that:

# 1. gets a liters parameter

# 2. converts liters to cubic meters knowing that 1000 liters are equal to 1 cubic meter and
# returns the cubic meters.

# Note: Defining the function is enough. You do not need to call or print out a function output,
# but you should name the function exactly liters_to_m3.


# Solution #

# Define a function named liters_to_m3 that takes one parameter, liters
def liters_to_m3(liters):
    # Convert liters to cubic meters by dividing liters by 1000
    m3 = liters / 1000
    
    # Return the result in cubic meters
    return m3
# ---------------------------------------------------------------------------------------------------
                                    # Coding Exercise 2 #

# Your task for this exercise is to complete the strength function. 
# The function is supposed to check the strength of the user's password. 

# The function should:

# 1. get a password argument

# 2. return the string "Strong Password" if all of the following conditions are true:

# Eight or more characters

# At least one uppercase letter.

# At least one digit.

# 3. returns "Weak Password" if at least one of the three conditions is not met.



# Solution: # 

# Define a function named strength that takes one parameter, password
def strength(password):
    # Create an empty dictionary to store the strength attributes
    result = {}
 
    # Check the length of the password
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False
 
    # Check if the password contains a digit and an uppercase letter
    digit = False
    uppercase = False
 
    # Iterate over each character in the password
    for i in password:
        # Check if the character is a digit
        if i.isdigit():
            digit = True
        # Check if the character is an uppercase letter
        if i.isupper():
            uppercase = True
 
    # Store the results in the dictionary
    result["digits"] = digit
    result["upper-case"] = uppercase
 
    # Check if all the strength attributes are True
    if all(result.values()):
        # Return "Strong Password" if all attributes are True
        return "Strong Password"
    else:
        # Return "Weak Password" if any attribute is False
        return "Weak Password"
    
# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 3 #
# Define a function that takes a list as an argument and returns the average value of the list items.
# For example, if I called your function with foo(10, 20, 30, 40) it should return 25, 
# the average of the numbers of the list.

# Solution #

def foo(mylist):
    # Calculate the sum of all elements in the list and divide it by the length of the list
    return sum(mylist) / len(mylist)
    
# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 4 #
                                        
# Implement a function that gets a person's name as a parameter and greets the person with Hi Person. 
# For example, if I call your function using foo("lisa") the function should return Hi lisa .

def foo(Manuel):
    # Return a greeting message with the provided name
    return f"Hi {Manuel}"

# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 4 #

# Implements a function that takes two strings as parameters, 
# concatenates them and returns the result.


# Solution #

def foo(s1, s2):
    # Concatenate the two provided strings
    return s1 + s2

# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 5 #
                                        
# Implement a function that gets a person's name (e.g. john) as a parameter and 
# returns a greeting (e.g. Hi John). Note that the first letter of the person's name 
# should always be uppercase


# Solution #

def foo(name):
    return f"Hi {name.title()}"

