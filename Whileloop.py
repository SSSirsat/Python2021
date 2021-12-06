empty_list = []
while True:
    num=int(input("Enter the value here: "))
    if num== 000: #To stop list inserting/ adding values you need to enter this value '000'
        break
    empty_list.append(num)

print(f"List Created is {empty_list}")

while True:
    success = False
    num = int(input("Enter the number to be searched in the list: "))
    pos = 1
    for i in range(len(empty_list)):
        if num  == empty_list[i]:
            success= True
            break
        pos+=1

    if success:
        print("Number found in the list at {} position.".format(pos))
    else:
        print("Number not found in the list")

    option=input("do you want to search more number in the list Enter (y to YES) : ")
    if option.lower() != 'y':
        break



# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i*j:>4}",end='   ')
#     print()

