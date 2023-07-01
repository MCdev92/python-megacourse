# Open the essay.txt file in read mode.
file = open("essay.txt", 'r')
 
# Read the contents of the file and assign it to a variable.
content = file.read()
 
# Convert the first letter of each word to uppercase and print out the output.
print(content.title())

## OUTPUT ##
"The True Meaning Of Obscurity Lies Underneath " 
"The Most Delicate Structures Of Viscosity. "
"The Idea Of Changing That Balance Is Obscure By Itself."