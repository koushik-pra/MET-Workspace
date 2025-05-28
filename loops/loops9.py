#9. Capitalize Names if Short (Using Tuple)
#Given tuple: ('sam', 'john', 'alex', 'bob'). If the name is 3 or fewer letters, print in uppercase. Else,
#capitalize.  using loops

names = ('sam', 'john', 'alex', 'bob')

for name in names:
    if len(name) <= 3:
        print(name.upper())
    else:
        print(name.capitalize())