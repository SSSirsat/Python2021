set1 = {1,2,3,4,5,1,2,3,4,5}
print("set-1", set1)
set2 = set1
set3=set1.copy()
set1.add(6)
set2.add(7)
# set1.pop()
set1.discard(5)

print("set 1=",set1)
print("set 2=",set2)
print("set 3=", set3)

set1={1,2,3,4,5}
set2={1,2,3}

set4 ={5,4,3,2,1}
print(set1.isdisjoint(set4))
print(set1.issuperset(set2))
