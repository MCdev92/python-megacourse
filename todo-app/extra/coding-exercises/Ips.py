ips = ['100.122.133.105', '100.122.133.111']
 
# Prompt the user to input the index of the IP they want and convert it to an integer.
user_choice = int(input("Enter the index of the IP you want: "))
 
# Create a formatted message string that includes the chosen IP based on the user's input.
message = f"You chose {ips[user_choice]}"
 
# Print the message.
print(message)
