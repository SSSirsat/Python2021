number = int(input("Enter the numbers to be checked"'\n'))
for i in range(2,number):
    if number % 2 == 0:
        print("Not a Prime Number")
        break
    else:
        print("Prime Number")
        break

