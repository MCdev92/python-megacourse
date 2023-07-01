# We have a list of three strings defined in the code area.

# Extend the code so your program prints out the following out of that list:

# 0-Document.txt
# 1-Report.txt
# 2-Presentation.txt

filenames = ['document', 'report', 'presentation']
 
for index, item in enumerate(filenames): # Iterate over the list using the enumerate() function to get both the index and value.
    print(f'{index}-{item.capitalize()}.txt')  # Print the formatted output with the index and capitalized value.