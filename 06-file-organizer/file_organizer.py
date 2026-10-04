import os
import shutil

folder = input("Enter the folder path: ")

text_folder = folder + "/Text Files"

if not os.path.exists(text_folder):
    os.mkdir(text_folder)

for file in os.listdir(folder):
    if file.endswith(".txt"):
        shutil.move(folder + "/" + file, text_folder + "/" + file)

print("Text files organized!")
