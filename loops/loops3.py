line = "Welcome to Python loops"
count= 0
p={"a", "e", "i", "o", "u"}
for letter in line:
    if letter in p:
        count += 1
print(count)

