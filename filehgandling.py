# 1. Writing to a file (creates the file if it doesn't exist)
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a file handling example in Python.\n")

print("File written successfully.")

# 2. Reading from the file
with open("example.txt", "r") as file:
    content = file.read()

print("\nContents of the file:")
print(content)


