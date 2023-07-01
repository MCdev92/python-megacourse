ranking = ['John', 'Sen', 'Lisa']
 
# Prompt the user to input a person's name and assign it to the variable 'name'.
name = input("Enter a name: ")
 
# Find the index of the given name in the ranking list and add 1 to get the rank.
rank = ranking.index(name) + 1
 
# Print the rank of the person with the given name.
print(rank)