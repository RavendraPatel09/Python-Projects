import os
path = input("Enter folder path: ")
keyword = input("Enter filename to search: ")
for root, dirs, files in os.walk(path):
    for file in files:
        if keyword in file:
            print(os.path.join(root, file))