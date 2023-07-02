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