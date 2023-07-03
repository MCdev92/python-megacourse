# This is a simple app that checks if a kid has the required height to use the ride
# This app will use decopling inside a custom function definition to convert ft and in to height

feet_inches = input("Enter feet and inches: ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    
    meters = feet * 0.3048 + inches * 0.0254
    return meters

result = convert(feet_inches)

if result < 1:
    print("Sorry you are too small to enter te ride.")
else:
    print("Come on in you can enter the ride.")