waiting_list = ["manuel", "genesis", "italia"]
waiting_list.sort() # the .sort() method will sort the list alphabetically 

for index, item in enumerate(waiting_list):
    row = f"{index +1}.{item.capitalize()}" # this command will return the list starting from 1 and caoitalized
    print(row)