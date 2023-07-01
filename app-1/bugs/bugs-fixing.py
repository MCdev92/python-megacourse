# This line of code is missing the close brakets!
answers = ['Yes', 'No', 'Yes', 'No', 'No'
# ---------------------------------------------------------------------------------------------------
# This line of code is missing the commas after 'YES' and 'NO'      
my_answer = input("What is your answer?")
answers = ['Yes', 'No', 'Yes' 'No' my_answer]   
# ---------------------------------------------------------------------------------------------------
# This line of code id missing the "." on the input variable
my_answer = input(What is your answer?)
answers = ['Yes', 'No', 'Yes', 'No', my_answer]
# ---------------------------------------------------------------------------------------------------
# This line of code contains the wrong brakets for the string passing the input variable
my_answer = input["What is your answer?"]
answers = ['Yes', 'No', 'Yes', 'No', my_answer]
# ---------------------------------------------------------------------------------------------------
# This code is missing the : after True and indent after print
while True
print("Hello")

#The programmer here is trying to convert the string "hello" to "HELLO" by using the upper() method:

# The argument should be outside of the parentheses ex: print(greetin.upper())
greeting = "hello"
print(upper(greeting))

# ---------------------------------------------------------------------------------------------------
# However, the program returns an error. Can you help fix the code, so it prints out HELLO?

# A programmer wrote the following program:

countries = []
 
while True:
    country = input("Enter the country: ")
    countries.append(country)
print(countries)     #  --> This print function should be indented

## #The expected output is as follows:
    Enter the country: Cambodia
    ["Cambodia"]
    Enter the country: Triomindia
    ["Cambodia", "Triomindia"]
    Enter the country

### However, the code returns an error instead of the expected output. Fix the code, so it produces the expected output.
# ---------------------------------------------------------------------------------------------------

# The programmer is trying to loop over the buttons list and print out each item with the first letter capitalized. However, the programmer has done something wrong. Try to find and fix the issue.

for i in buttons:
    print(i.capitalize())
 
buttons = ["cancel", "reply", "submit"] # This function declaration should be define before the for loop!!!

# ---------------------------------------------------------------------------------------------------

#### The programmer is again missing something in the code. Try to find what it is and fix it.
buttons = ["cancel", "reply", "submit"]
 
for i in buttons:
print(i.capitalize()) ### Identation require after the for loop!!!

# ---------------------------------------------------------------------------------------------------

#### The code below is supposed to print out the items of the list with the first character of each item capitalized. However, the code contains two errors. Try to find and fix the errors.
for item in ["sandals", "glasses", "trousers"): 
    print(item.capitalize)
    
    #### Two Errors ###
## Wrong brackets are used for the list of items
## The print function is passing the capitalize method without parenthesis i.e: print(item.capitalize())
