# Dictionary Called Users
users= {"alice":25, "bob":30}


# Access a Value Using a Key
print(users["alice"])
#Safely Accessing Values
print(users.get("charlie", "Not Found"))

# Adding a new Item to the Dictionary
users["charlie"] = 28
    # Alice: 25
    # bob: 30
    # charlie: 28

# Prints Entire Dictionary
print(users)
