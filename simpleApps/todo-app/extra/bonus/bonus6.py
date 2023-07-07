# This program will store and create filenames inside files folder
# You can break lines with commas en inside .py files
contents = ["My daughter is 17 months.", 
           "Her name is Italia Corporan",
           "She is an amazing child",
           "Her mother's name is Genesis"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# This line of code will create, read and overwrite the files inside "files"
for content, filename in zip(contents, filenames):
    file = open(f"todo-app/files/{filename}", 'w')
    file.write(content)