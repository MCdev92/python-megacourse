# transforming the string inside filenames with a list comprehension
filenames = ["1.doc", "1.report", "1.preparation"]

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

print(filenames)