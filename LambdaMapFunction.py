#Lambda: One time function / anynomes
my_fun= lambda x,y:x*y
a=my_fun(4,5)
print("A ", a)

USD_list=[2,5,6,9,2,3,5,58,2,525,46]
INR_list=[]
for i in USD_list:
    INR_list.append(i*73)
print(INR_list)

#### map, filter, reduce
INR_list=list(map(lambda x:x*73,USD_list))
print("2. INR Value :",INR_list)

def fun1(a):
    return a*a
def fun2(a):
    return a**3
INR_list=list(map(lambda x:x(5),[fun1,fun2]))
print("3. INR Value :",INR_list)
#
def fun1(a):
    return a*a
def fun2(a):
    return a**3
for i in range(6):
    INR_list = list(map(lambda x: x(i), [fun1, fun2]))
    print("3. INR Value :", INR_list)

##FILTER # True values only be printed
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
values =list(filter(lambda x:x%2,list1))  # x%2 become 0 = False mean it will not print in list
print("1. The Filtered List",values)


x =list(filter(lambda x:x>10,list1))
print("2. The Filtered List",x)
import statistics
avg_val = statistics.median(list1)
x =list(filter(lambda x:x>avg_val,list1))
print("2. The Filtered List",x)


##Reduce
import functools
list4 = [1,3,5,6,8,9,4,5]
val  = functools.reduce(lambda x,y :x*y , list4)
print("Output :", val)

