import random 
import os
import string

file_path = "../serverdata/random.txt"
directory_path = os.path.dirname(file_path)

# Create the directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        existing_content = file.read()
        print("Existing content:")
        print(existing_content)

with open(file_path, "w") as file:
    random_text = "".join(random.choices(string.ascii_letters + string.digits, k=100))
    file.write(random_text)
    print("New content:")
    print(random_text)
