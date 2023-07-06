                                # Coding Exercise 1#
# Write a program that:

# 1. asks users to enter a password.

# 2. returns "Great password there!" if the password has more than 7 characters. 

# 3. returns "Your password is weak." if the password has 7 or fewer characters.


## Solution ##

# Prompt the user to enter a password
password = input("Enter a new password: ")
 
# Check the length of the password
if len(password) > 7:
    print("Great password there!")
else:
    print("Your password is weak.")
# ---------------------------------------------------------------------------------------------------
                                # Coding Exercise 2 #
# Write a program that: 

# 1. asks users to enter a password.

# 2. returns "Great password there" if the password has more than 7 characters. 

# 3. returns "Password is OK, but not too strong" if the password has exactly 7 characters.

# 4. returns "Your password is weak" if the password has 7 or fewer characters.


# Solution #

# Prompt the user to enter a password
password = input("Enter a new password: ")
 
# Check the length of the password
if len(password) > 7:
    print("Great password there")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak")
    
# ---------------------------------------------------------------------------------------------------
