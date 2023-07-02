while True: 
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] 
        
        with open("todo-app/todos.txt", 'r') as file: 
            todos = file.readlines()
            
        todos.append(todo + '\n')
        
        with open("todo-app/todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
            
        with open("todo-app/todos.txt", 'r') as file:
            todos = file.readlines()
            
            for index, item in enumerate(todos): 
                item = item.strip('\n') 
                row = f"{index + 1}-{item}" 
                print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) 
            print(number)
            
            number = number - 1 
            
            with open("todo-app/todos.txt", 'r') as file: 
                todos = file.readlines()
            
            new_todo = input("Enter new todo: ") 
            todos[number] = new_todo + '\n'
            
            with open("todo-app/todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            user_action = input("Type add, show, edit, complete or exit: ")
            user_action = user_action.strip()

        
    elif user_action.startswith('complete'):
        number = int(user_action[9:])
        
        with open("todo-app/todos.txt", 'r') as file: 
            todos = file.readlines()
        index = number -1 
        todo_to_remove = todos[index].strip('\n') 
        todos.pop(index) 
        
        with open("todo-app/todos.txt", 'w') as file:
            file.writelines(todos)
            
        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)   
            
    elif user_action.startswith('exit'):
        break
    else:
        print("Error Command is not Supported")
    
print("Bye!")

