number = input("Enter a number to see its multiplication table: ")

i = 1
for _ in range(10):
    print(f"{number} * {i} = {int(number) * int(i)}")
    i += 1