# Copying data from file 1 to file 2
file1 = open("Test_File_1.txt", "r")

file2 = open("Test_File_2.txt", "w")
for i in file1.readlines():
    file2.write(i)

file1.close()
file2.close()

# Reading the copied data from file 2

file2 = open("Test_File_2.txt", "r")
print("New file created")
for i in file2.readlines():
    print(i, end="")

file2.close()

# Updating the existing file 2

s = input("\nEnter your message: ")
file2 = open("Test_File_2.txt", "a")
file2.write("\n")
file2.write(s)
file2.close()

# Reading the copied data and updated data from file 2

file2 = open("Test_File_2.txt", "r")
print("Old file updated with new data")
for i in file2.readlines():
    print(i, end="")

file2.close()
