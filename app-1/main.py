user_prompt = "Enter a todo:"

todos = []

# Boolean loop. append and capitalize are methods, methods can take arguments
while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)

