def multiply(a,b):
    return a/b


try:
    x=multiply(6,0)
    print(x)

except ZeroDivisionError:
    print("any print statement")

except NameError:
    print("This is name error")
