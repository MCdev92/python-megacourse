while True: 
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n" # + "\n" will create a space between the items
            
            file = open("todos.txt", 'r') # this command will open the file in read mode
            todos = file.readlines() # this commannd reads and creates a list of what is in the file
            file.close() # we always need to use the close command
            
            todos.append(todo) # this command will append the items the user inputs
            
            file = open("todos.txt", 'w') # this overwrites the existing file 
            file.writelines(todos)
            file.close()
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

