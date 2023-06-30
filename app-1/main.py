user_prompt = "Enter a todo:"

todos = []

# For loop using match to allow the user to choose an action
while True:
    user_action = input("Type add or show: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
    
print("Bye!")

