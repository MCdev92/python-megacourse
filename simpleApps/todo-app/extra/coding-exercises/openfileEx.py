# Open the file named "file.txt" in write mode using a context manager
# The 'with' statement ensures that the file is properly closed after writing
with open("file.txt", "w") as file:
    # Write the string "snail" to the file
    file.write("snail")