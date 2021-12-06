# a=[5,-67,8,[1,2,3,4],"Hello",True,False,5,4+3j]
# b=[]
# print("Type of a is",type(a))
# print("Type of a is",type(b))
# print("value of a ",a[1])
# print("value of a ",a[3][1])
# b =a[3]
# print("Value of b is :", b[3])
# print("length of a is:", len(a))
# a.append("hi")
# a.insert(2,505)
#
# print(a)


# a= "Hello Firenda I am shubham Here learning Python"
# for i in a:
#     print("value of i:", i)

#
# i = int(input())
# lis = list(map(int,raw_input().strip().split()))[:i]
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))
#
# print (max(lis))

# n = int(input())
#
# nums = map(int, input().split())
# print(sorted(list(set(nums)))[-2])
#
# n = int(input())
# a = [int(x) for x in input().split()]
# largest = secondlargest = -100
# for x in a:
#     if x > largest:
#         tmp = largest
#         largest = x
#         secondlargest = tmp
#     elif x > secondlargest and x != largest:
#         secondlargest = x
# print(secondlargest)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print (sorted(set(arr))[-2])

if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    a.sort()
    b = [i for i in a if i[0] != a[0][0]]
    c = [j for j in b if j[0] == b[0][0]]

    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])