# CONSTANT added to custom fucntion
FILEPATH = "todo-app/todos.txt"

# doc-strings are very important when using fuctions for multiple programs and colab
def get_todos(filepath=FILEPATH):
    """ Read a txt file and return the list of to-do items. """
    with open(filepath, 'r') as file_local: 
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
            
