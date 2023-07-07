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
                                        # Coding Exercise 5 #

# Implements a function that takes two strings as parameters, 
# concatenates them and returns the result.


# Solution #

def foo(s1, s2):
    # Concatenate the two provided strings
    return s1 + s2

# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 6 #
                                        
# Implement a function that gets a person's name (e.g. john) as a parameter and 
# returns a greeting (e.g. Hi John). Note that the first letter of the person's name 
# should always be uppercase


# Solution #

def foo(name):
    return f"Hi {name.title()}"

# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 7 #

# Define a get_age function that:

# 1. has two parameters, year_of_birth and current_year .

# 2. the current_year  parameter should be a default parameter. The default value should be the current year.

# 3. the function should calculate and return the age of the user given the year_of_birth and the current_year.

                                            # Solution #

# Define a function named get_age that takes two parameters
def get_age(year_of_birth, current_year=2023):
    # Calculate the age by subtracting the year_of_birth from the current_year
    age = current_year - year_of_birth
    # Return the calculated age
    return age

# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 8 #

# Write a get_nr_items function that:

# 1. gets one parameter. The parameter is expected to be a list of strings.

# 2. returns the number of items the list contains.


                                            # Solution #

# Define a function named get_nr_items that takes one parameter: user_input
def get_nr_items(user_input):
    # Split the user_input string by comma and store the resulting items in the 'items' list
    items = user_input.split(',')
    # Return the length of the 'items' list
    return len(items)

# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 9 #

# Define a function that calculates the area of a square.

# For example, if I was to call your function with foo(7) the output would be 49. 
# If I called it with foo(3)  it would return 9, and so on. 

# Note that you don't have to name your function foo. Give it any name you want.

                                            # Solution #

def foo(a):
    # Calculate the area of a square by multiplying the length of one side by itself
    return a * a

# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 10 #

# Define a function that:

# (1) takes a temperature as a parameter

# (2) returns "Warm" if the temperature is greater than 7

# (3) returns "Cold" if the temperature is equal to or less than 7

# If I called your function with foo(10) it would return Warm. 
# If I called it with foo(7) or foo(5) it would return Cold in both cases, and so on.

                                            # Solution #        

def foo(temperature):
    if temperature > 7:
        # If the temperature is greater than 7, it is considered warm
        return "Warm"
    else:
        # If the temperature is not greater than 7, it is considered cold
        return "Cold"

# ---------------------------------------------------------------------------------------------------
                                        # Coding Exercise 11 #
    
# Define a function that:

# (1) takes a string as a parameter

# (2) returns False if the string contains less than 8 characters

# (3) returns True if the string contains 8 or more characters

# In other words, if I called your function with foo("mypass") it would return False. 
# If I called it with foo("mylongpassword") it would return True, and so on.
                            
                                            # Solution #

def foo(password):
    if len(password) >= 8:
        # If the length of the password is greater than or equal to 8, return True
        return True
    else:
        # If the length of the password is less than 8, return False
        return False

# ---------------------------------------------------------------------------------------------------
                                     # Coding Exercise 11 #
                                     
# Define a  water_state function that:

# 1. gets a temperature argument

# 2. returns the string "Solid" if the temperature is less than or equal to 0

# 3. returns "Liquid" if the temperature is greater than 0, but less than 100.

# 4. returns "Gas" if the temperature is greater than or equal to 100.
                                            # Solution #

# Define a function named water_state that takes one parameter: temperature
def water_state(temperature):
    # Check if the temperature is less than or equal to 0
    if temperature <= 0:
        return "Solid"  # Return "Solid" if temperature is <= 0
    # Check if the temperature is between 0 and 100 (exclusive)
    elif 0 < temperature < 100:
        return "Liquid"  # Return "Liquid" if temperature is between 0 and 100
    else:
        return "Gas"  # Return "Gas" for all other cases

# ---------------------------------------------------------------------------------------------------
                                     # Coding Exercise 12 #
                            
# In the previous exercise, we hardcoded the values 0 and 100. However, it is better to place those values 
# in constants. Therefore, your task is to:

# 1. create a FREEZING_POINT and a BOILING_POINT variable and store the values 0 and 100 in them respectively.

# 2. modify the function of the previous exercise by using those variables instead of 
# the hardcoded 0 and 100 values. The previous function is given in the code area.

                                    # Solution #

# Define constants for freezing point and boiling point of water
FREEZING_POINT = 0
BOILING_POINT = 100
 
# Define a function named water_state that takes one parameter: temperature
def water_state(temperature):
    # Check if the temperature is less than or equal to the freezing point
    if temperature <= FREEZING_POINT:
        return "Solid" 
    # Check if the temperature is between the freezing point and boiling point
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid" 
    # Return "Gas" for all other cases
    else:
        return "Gas"  

# ---------------------------------------------------------------------------------------------------
                                     # Coding Exercise 13 #
           
           
# Define a function that:

# (1) takes a temperature as a parameter

# (2) returns "Hot" if the temperature is greater than 25

# (3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.

# (4) returns "Cold" if the temperature is less than 15.

# If I called your function with foo(10) it would return "Cold". 

# foo(15) or foo(16) or foo(25) would all return "Warm" and foo(26) would return "Hot".                          
                                        
                                        # Solution #

def foo(temperature):
    if temperature > 25:
        # If the temperature is greater than 25, return "Hot"
        return "Hot"
    elif 25 >= temperature >= 15:
        # If the temperature is between 25 and 15 (inclusive), return "Warm"
        return "Warm"
    else:
        # If the temperature is less than 15, return "Cold"
        return "Cold"
                            