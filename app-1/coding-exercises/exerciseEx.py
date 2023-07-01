
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