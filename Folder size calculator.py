import os
def folder_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    return total
path = input("Enter path: ")
print("Size (bytes):", folder_size(path))