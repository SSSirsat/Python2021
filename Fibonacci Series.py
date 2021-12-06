a = int(input("Enter the first Number:"))
b = int(input("Enter the second Number:"))
n = int(input("Enter the Numbers of elements:"))

print(a,b, end=" ")

while n-2:
    c = a+b
    a = b
    b = c
    print(c, end=" ")
    n = n-1
