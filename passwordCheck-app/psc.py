# This app checks if the user password input is weak or strong using 
# if else statemnets and dictionaries.

password = input("Create new password: ")

result = {} # this is a dictionary

if len(password) >= 10:
    result["length"] = True
else:
    result["length"] = False
    
digit = False
for index in password:
    if index.isdigit():
        digit = True
        
result["digits"] = digit

uppercase = False
for index in password:
    if index.isupper():
        uppercase = True

result["upper-case"] = uppercase

# print(result)

if all(result.values()):
    print("Strong Password :^)")
else:
    print("Weak Password :^(")
