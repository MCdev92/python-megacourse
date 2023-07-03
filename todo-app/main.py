# doc-strings are very important when using fuctions for multiple programs and colab
def get_todos(filepath="todo-app/todos.txt"):
    """ Read a txt file and return the list of to-do items. """
    with open(filepath, 'r') as file_local: 
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todo-app/todos.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
            
while True: 
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] 
        
        todos = get_todos()
            
        todos.append(todo + '\n')
        
        write_todos(todos)

    elif user_action.startswith('show'):
            
            todos = get_todos()
            
            for index, item in enumerate(todos): 
                item = item.strip('\n') 
                row = f"{index + 1}-{item}" 
                print(row)
                
    # Try and except added for error handling
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) 
            print(number)
            
            number = number - 1 
            
            todos = get_todos()
            
            new_todo = input("Enter new todo: ") 
            todos[number] = new_todo + '\n'
            
            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    # Try and except added for error handling
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            todos = get_todos()
            index = number -1 
            todo_to_remove = todos[index].strip('\n') 
            todos.pop(index) 
            
            write_todos(todos)
                
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)  
        except IndexError:
            print("Wrong command: wrong number")
            continue 
            
    elif user_action.startswith('exit'):
        break
    else:
        print("Error Command is not Supported")
    
print("Bye!")

