import parsefunc
import convertfunc

feet_inches = input("Enter feet and inches: ")
 
parsed = parsefunc.parse(feet_inches)

result = convertfunc.convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Sorry you are too small to enter te ride.")
else:
    print("Come on in you can enter the ride.")