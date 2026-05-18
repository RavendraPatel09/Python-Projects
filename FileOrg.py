import os, shutil

path = input("Enter folder path: ")

for file in os.listdir(path):
    ext = file.split(".")[-1]
    folder = os.path.join(path, ext)

    if not os.path.exists(folder):
        os.mkdir(folder)

    shutil.move(os.path.join(path, file), os.path.join(folder, file))