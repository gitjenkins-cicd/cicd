import os
folders = input("Please provide folder name with spaces: ").split()
# print("folders are:", folders)

for folder in folders:
    # print("folders are:", folder)
    try:
        files=os.listdir(folder)
        print(files)
    except FileNotFoundError:
        print("File not found")
        continue
    for file in files:
        print(file)