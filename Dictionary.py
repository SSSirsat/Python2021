# dict1 = {"John":25, "Jack":26, "Jill":18, "Tim":35, "Scahin":40}
# dict2 = {"John":"Hyderabad", "Tim":"Bngalore"}
# dict3 = {"Jack":"Chennai", "Jill":"Kolkata"}
# #We havre to print "John is of age 25 and lives in Hydarabad
#
# for key in dict1.keys():
#
#     if key in dict2.keys(): #and key =="John":
#         print("John is of age {} and lives in {}".format(dict1["John"], dict2["John"]))
#     # elif key in dict3.keys():
#     #     print("Girl")
#     if key in dict2.keys(): #and key =="John":
#         print("{} is of age {} and lives in {}".format(key, dict1[key], dict2[key]))
#
#     else:
#         print("Undefined Value")

list1 = [21,22,23,24,25,26,27,30,35]
dict_marks = {}.fromkeys(list1,0)
print("Maks = ", dict_marks)
print("Enter marks for roll no 21")
sub=[]
for i in range(3):
    sub.append(input("Enter your marks: "))
dict_marks[21] = sub
print("Marks = ", dict_marks)



