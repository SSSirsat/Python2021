print("Hello World")
#we can write comments here by using '# ' in starting of line

'''
Or we can use tripple cotation to comments out any line 
i the prigraamm .
 IT is good practice to write comments to understand the program  in future to 
 understand the concepts 
  
'''

a = 5
b= 6
c=a+b
print("Sum of ",a,"and ", b,"is : ", c)

print("What\'s your \name")
print("\\n is for newline in python")
print("He said call me Tomarrow", end='\n')
print("\\\\n will give you \\n")

# r"string" - this means that ignore any special charecters inside


print(r"109. \name in python we can write here in new line???")
print(r"C:\Mydata\newdata\pythonfile\python.txt")

cost_price= 300
selling_price = 450
Profit = selling_price - cost_price
print("Cost price of an item is {} and when we sold at {} we get a profit of :{}".format(cost_price,selling_price,Profit))

#We can use '.format()'to provide variable in print flower 'bracket{}'
bat1 = "Sachin"
open1 = "Opner"
cont1 = " India"
print("{0} is plays cricket for {2} as a {1}".format(bat1,open1,cont1))
print("{0:10} is plays cricket for {2:10} as a {1:10}".format(bat1,open1,cont1))
print("{0:<10} is plays cricket for {2:^10} as a {1:>10}".format(bat1,open1,cont1))
print("{0:_<10} is plays cricket for {2:-^10} as a {1:*>10}".format(bat1,open1,cont1))


Total_cost = 500
Quanti = 13
cost_per_unit = Total_cost / Quanti
print("The Total cost of the Product is {} and the cost per unit is {:.5f}".format(Total_cost, cost_per_unit))

#Integers
a=5
b=6
#addition
c=a+b
print("Value of c: ", c)
print("Type of c: ", type(c))
#Substracrion
c=a-b
print("Value of c: ", c)
print("Type of c: ", type(c))
#Multiplication
c=a*b
print("Value of c: ", c)
print("Type of c: ", type(c))
#Division
c=a/b
print("Value of c: ", c)
print("Type of c: ", type(c))
#Reminder
c=a%b
print("Value of c: ", c)
print("Type of c: ", type(c))
#Power
c=a**b
print("Value of c: ", c)
print("Type of c: ", type(c))

#Float

#String
a="5"
print("1. Data type: ", type(a))
a= int(a)
print("2. Data type: ", type(a))
a=True
print("3. Data type: ", type(a))
a=int(a)
print("4. Data type: ", type(a))
a=5
a=bool(a)
print("5. Data type: ", type(a))
print("value of A:",a)
# any values other than "0" or empty "" will gives  us "True" only '0' will give us "False" value
a=-1
a=bool(a)
print("value of A:",a)
a=0
a=bool(a)
print("value of A:",a)
a="stringd"
a=bool(a)
print("value of A:",a)
a=""
a=bool(a)
print("value of A:",a)

#bool
#Logical: and, or, not
print("Boolean 1 :", True  and True )
print("Boolean 1 :", True or True )
print("Boolean 1 :", True or False )
#

#Bitwie and or not
a=5
b=10
print("Bitwise 1. ", a | b)
#LeftShit
print("Bitwise 2. ", b<<2)
#RightShift
print("Bitwise 2. ", b>>2)

a= 5
print("A :", a)
a==5
print('A :', a)
print(a==5)
c=a==5
print(c)
print(a!=5)
