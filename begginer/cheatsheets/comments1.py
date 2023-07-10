# How to use the python console to find methods

# Commands: 

# >>> dir(str) will show all string methods you can use in python
# >>> help(str.methodname) ex: >>> help(str.capitalize) will information about what this method does

# >>> dir(list) will show all list methods you can use in python
# >>> help(list.methodname) will give you information about the method

# >>> import builtins to import python functions
# >>> dir(builtins) will show you a list of functions that you can use in python

# .title() method will convert the first letter capital
# .capitalize() will convert only the first letter of a string capital

# Floats and Integers are used to do math operations in python
# You can convert strings into numbers by using float() or int(). i.e: int("10") = 10, float("5") = 5.0

# The sanme is true for strings. You can change numbers into string by using str()

# The function type() will return the type of format of an argument. i.e: x = 10.0 , type(x) = <float>

# we can use two ways to import functions:
# from functions import get_todos, write_todos, , , , ....... or
# import functions and add functions.nameofFunction i.e: funnction.get_todos()

# how slicing works: you can slice by specifying which letter [:4] 
# ie: Print out the slice ['a', 'b', 'c'] of the letters list using slicing. print(leters[:3]) or
# Print out the slice ['b', 'c', 'd'] of the letters list using slicing. 
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']   ..... print(letters[1:4]) this will cut the first letter
# or Print out the slice ['e', 'f', 'g'] of the letters list using slicing. print(letters[4:])

# def calculate_time(g=9.80665, h):
   # t = (2 * h / g) ** 0.5
    # return t
    
    ##
  
# time = calculate_time(100)
# print(time)

# Non-default parameters such as "h" should come first in a function definition, then the default parameters.