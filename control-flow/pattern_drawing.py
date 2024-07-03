number = int(input("Enter the size of the pattern: "))

row= number
while row > 0:
    for i in range(number):
        print("*", end="")
    print()
    row -= 1