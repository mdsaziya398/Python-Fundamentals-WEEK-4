# Step 1: Create a text file and write data into it
file = open("sample.txt", "w")

file.write("Welcome to Python File Handling.\n")
file.write("This is the first line of data.\n")
file.write("Python allows us to create and manage files easily.\n")

file.close()

print("File created and data written successfully.\n")


# Step 2: Read and display the file content
file = open("sample.txt", "r")

print("Original File Content:")
print(file.read())

file.close()


# Step 3: Append new data to the existing file
file = open("sample.txt", "a")

file.write("This is the newly appended data.\n")
file.write("File handling includes reading, writing, and appending.\n")

file.close()

print("New data appended successfully.\n")


# Step 4: Read and display the updated file content
file = open("sample.txt", "r")

print("Updated File Content:")
print(file.read())

file.close()