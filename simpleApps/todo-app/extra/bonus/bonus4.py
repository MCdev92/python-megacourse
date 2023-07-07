# How to replace a srting using the .replace method
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentatiopns.txt"]

for filename in filenames:
    filename = filename.replace('.','-', 1)  # This variable will replace the . by - in place number 1
    print(filename)
    
 # You can use toples too. i.e: filenames = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentatiopns.txt")   
filenames = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentatiopns.txt")