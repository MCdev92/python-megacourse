# Open the essay.txt file in read mode.
file = open("essay.txt", 'r')
 
# Read the contents of the file and assign it to a variable.
content = file.read()
 
# Calculate the number of characters in the content.
nr_chars = len(content)
 
# Print out the number of characters.
print(nr_chars)
