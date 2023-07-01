# The ranking list given in the coding area represents the ranking of three athletes, John, Sen, and Lisa. John won 1st place, Sen got 2nd, and Lisa 3rd.

# Your task is to create a program that:

# 1. Contains the above list.

# 2. Prompts the user to input a rank number.

# 3. Returns the person who has the given rank.

ranking = ['John', 'Sen', 'Lisa']
 
# Prompt the user to input a rank number and assign it to the variable 'rank'.
rank = int(input("Enter rank number: ")) - 1
 
# Access the element in the ranking list based on the given rank and assign it to the variable 'name'.
name = ranking[rank]
 
# Print the name of the person who has the given rank.
print(name)