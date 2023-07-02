while True: 
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n" 
            
            file = open("todo-app/files/todos.txt", 'r') 
            todos = file.readlines() 
            file.close() 
            
            todos.append(todo) 
            
            file = open("todo-app/files/todos.txt", 'w') 
            file.writelines(todos)
            file.close()
        case 'show':
                file = open("todo-app/files/todos.txt", 'r')
                todos = file.readlines() 
                file.close() 
                    
            # Added a new variable (list comprehension) to clean up the list A.K.A remove extra spaces
                new_todos =[item.strip('\n') for item in todos]
                    
                for index, item in enumerate(new_todos): 
                    row = f"{index + 1}-{item}" 
                    print(row)
 
        case 'edit':
            number = int(input("Number of todo to edit: ")) 
            number = number - 1 
            new_todo = input("Enter new todo: ") 
            todos[number] = new_todo 
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1) 
        case 'exit':
            break
    
print("Bye!")

