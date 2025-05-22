tags = {"python", "fastapi", "backend"}
user_inpu= input("enter a new tag : ")
if user_inpu in tags:
    print("it already exists")
else:
    tags.add(user_inpu)
print(tags)