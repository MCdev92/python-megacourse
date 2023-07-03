# This is a simple app that checks if a kid has the required height to use the ride
# This app will use decopling inside a custom function definition to convert ft and in to height
# optimization added: created parse to store the var parts, feet and inch.
# then only use the convert func to convert feet and inch to meters
feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
 
parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Sorry you are too small to enter te ride.")
else:
    print("Come on in you can enter the ride.")