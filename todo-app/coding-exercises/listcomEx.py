                    ### Coding Exercise 1 ###
                    
# Extend the given code (in the exercise area) so the code capitalizes
# all the names and surnames of the list and then prints the new list. 
# The output of your code should be as below:

# ['John Smith', 'Jay Santi', 'Eva Kuki']


# Define the initial list of names
names = ["john smith", "jay santi", "eva kuki"]
 
# Use list comprehension to capitalize names and surnames
names = [name.title() for name in names]

# Print the updated list
print(names)

# ---------------------------------------------------------------------------------------------------
                     ### Coding Exercise 2 ###
                         
# Extend the given code so the code prints out a list containing 
# the number of characters for each username.

# The output of your code should be as below:

              # [9, 11, 11]
              
# Define the initial list of usernames
usernames = ["john 1990", "alberta1970", "magnola2000"]
 
# Use list comprehension to calculate the number of characters for each username
chars = [len(item) for item in usernames]
 
# Print the list of character counts
print(chars)

# ---------------------------------------------------------------------------------------------------

                             ### Coding Exercise 3 ###
                            
# Extend the given code so the code prints out a list containing the same items as floats.

# The output of your code should be as below:

# [10.0, 19.1, 20.0]

# Define the initial list of user entries as strings
user_entries = ['10', '19.1', '20']
 
# Use list comprehension to convert each item to a float
user_numbers = [float(item) for item in user_entries]
 
# Print the list of floats
print(user_numbers)

# ---------------------------------------------------------------------------------------------------

                            ### Coding Exercise 4 ###
# Extend the given code so it prints out the sum of the numbers.

# The output of your code should be as below:

# 49.1

user_entries = ['10', '19.1', '20']

user_sum = [float(item) for item in user_entries]

print(sum(user_sum))