todos = []

# We can add a new case for when user enters an unknown command
while True:
    user_action = input("Type add or show: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display': # added a Bitwise or Operator
            for item in todos:
                item = item.title() # you can add more lines under the for line
                print(item)
        case 'exit':
            break
        case _: # this will allow the code to remind the user that they entered a wrong command
            print("Hey, you entered an unknown command")
    
print("Bye!")
