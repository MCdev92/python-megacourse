                        ### Coding Exercise 1 ###
# Coding Exercise Exchange rate
# Create a program that:

# 1. Prompts the user to input a (dollar) amount.

# 2. Calculates the corresponding amount in euros, given an exchange rate of 2.

# 3. Prints out the amount in euros.

rate = 2
 
# Prompt the user to input a dollar amount and assign it to the variable 'dollars'.
dollars = float(input("How many dollars have you got? "))
 
# Calculate the corresponding amount in euros by multiplying dollars with the rate.
euros = dollars * rate
 
# Print out the amount in euros.
print(euros)

# ---------------------------------------------------------------------------------------------------

                            ### Coding Exercise 2 ###
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

# ---------------------------------------------------------------------------------------------------
                        
                        ### Coding Exercise 3 ###
# create a program that:

# 1. Contains the above list.

# 2 Prompts the user to input the person's name.

# 3. Returns the rank that person has.

ranking = ['John', 'Sen', 'Lisa']
 
# Prompt the user to input a person's name and assign it to the variable 'name'.
name = input("Enter a name: ")
 
# Find the index of the given name in the ranking list and add 1 to get the rank.
rank = ranking.index(name) + 1
 
# Print the rank of the person with the given name.
print(rank)                       