#8. Check if Any Number is a Perfect Square
#Given: [10, 25, 36, 40]. Print the first number that is a perfect square. Stop after finding it.
#Expected Output: 25 is a perfect square
numbers = [10, 25, 36, 40]

for num in numbers:
    for i in range(1, num + 1):
        if i * i == num:
            print(f"{num} is a perfect square")
            exit()
        elif i * i > num:
            break
