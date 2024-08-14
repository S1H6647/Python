import os 

# Specify the directory you want to list
directory_path = '/'

# Makes list of the specified directory
contents = os.listdir(directory_path)

for items in contents:
    print(items)

# print(contents) is also valid but output won't be in a list.