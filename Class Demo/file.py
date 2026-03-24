# Write a Text file
with open("test.txt", "w") as f:
    
    
    f.write("sample log\n")

# Opening the file for reading
with open("test.txt", "r")    as f:
    print(f.read())