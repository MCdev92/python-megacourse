# Open your computer IDE and place the following in a Python file:

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# Then, create a program that:

# 1. generates multiple text files by iterating over the filenames list,

# 2. and writes the text Hello  inside each generated text file.

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()
    
# ---------------------------------------------------------------------------------------------------

                            ### Coding Exercise 2 ###
                            
# Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.

# Then, create a program that:

# 1. reads each text file and

# 2. prints out the content of each file in the command line.

# The expected output would be like the following:
        # I am a.
        # I am b.
        # I am c.
        
filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)
# ---------------------------------------------------------------------------------------------------

                            ### Coding Exercise 3 ###
                            
# Open the file named "bear.txt"
file = open("bear.txt")
 
# Read the content of the file and assign it to the variable 'content'
content = file.read()
 
# Print the content of the file
print(content)
# ---------------------------------------------------------------------------------------------------

                            ### Coding Exercise 4 ###
                            
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

# ---------------------------------------------------------------------------------------------------

                            ### Coding Exercise 5 ###


# Open the essay.txt file in read mode.
file = open("essay.txt", 'r')
 
# Read the contents of the file and assign it to a variable.
content = file.read()
 
# Calculate the number of characters in the content.
nr_chars = len(content)
 
# Print out the number of characters.
print(nr_chars)

