year = int(input("Enter Year:\n"))

if year % 400 == 0:
    print("leap Year")
elif year % 4 == 0:
    print("leap Year")
elif year % 100 == 0:
    print("Not a leap year")
else:
    print("Not a leap Year")
