# # for loops
# iteration=1
# val = 6
# print(val not in [0,6,5])
#
# for value in range(10,50,10):
#     print("value in VALUES is: ", value)
#     print("value of ITERATION is :", iteration)
#     iteration += 1
#
# print("Thanks for using for loop ")

# for value in range(5):
#     for val in range(6):
#         for val2 in range(2):
#             print(f"{value} : {val}")
#         for val3 in range(3):
#             print(f"{value} : {val}")

#Printing '*******'

for i in range(5):
    for i in range(5):
        print("* ", end='')
    print()

for i in range(5):
    for j in range(i):
        print('*', end=' ')
    print()
for i in range(5):
    for j in range(i):
        print('*', end=' ')
    print()





