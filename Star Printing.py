# num_row = int(input("Enter the numbers of rows or stars:"))
#
# for i in range(num_row):
#     for j in range(i):
#         print("*", end=' ')
#     print()
# for i in range(num_row,0,-1):
#     for j in range(i):
#         print("*", end=' ')
#     print()

row = 3
col = (2*row)-2

for i in range(0,row):
    for j in range(0,col):
        print(end="")
    col = col -1
    for j in range(0,i+1):
        print("*", end=' ')
    print()



