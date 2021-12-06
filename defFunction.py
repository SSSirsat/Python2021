# #Variable length argument
# sum=100
# def vararg_fun1(*a,**b):
#     global sum
#     print("1. Sum value is: ", sum)
#     if len(a)>0:
#         sum=0
#         for i in a:
#             sum+=i
#         print("Sum of the values in the tuple is ", sum)
#     else:
#         print("There is no value in the Touple")
# vararg_fun1(12,5,32,5,6, num1=2, num2=5)

###Function in side the function>>>>>.Local and global function as same as variable.


def fun1():
    print("This is line 1 of fun1")
    def fun2():
        print("This is line 1 of fun2")
        print("This is line 2 of fun2")
    print("This is line 2 of fun1")
    fun2()
    print("This is line 3 of fun1")

fun1()




