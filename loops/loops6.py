#6. Multiply Dictionary Values if Key Starts with 'a'
#Given dictionary: {'apple': 2, 'banana': 3, 'apricot': 4, 'berry': 5}. Multiply values where keys start with
#'a'.
#Expected Output: Product of values:
fruits = {'apple': 2, 'banana': 3, 'apricot': 4, 'berry': 5}
result = 1
for key in fruits:
    if key.startswith('a'):
        result = result * fruits[key]
print(result)