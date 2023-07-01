todos = []

# For loop using match to allow the user to choose an action
while True: 
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos): # adding the func enumerate will show number of items
                row = f"{index + 1}-{item}" #  {index + 1} will make our list start from 1 not zero
                print(row) 
        case 'edit':
            number = int(input("Number of todo to edit: ")) # convert from str to int
            number = number - 1 # This variable will allow the user to choose the right number  i.e: 1-1 = 0, 1-2 = 1
            new_todo = input("Enter new todo: ") # this variable will store new user input in new_todo
            todos[number] = new_todo # Access items from a list and replace
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1) # this will make our list start from 1 not zero
        case 'exit':
            break
    
print("Bye!")

