'''# a bridge
file_object = open("D:\AI, ML, DL\Python2021\Myfile.txt",'r')
# print("Content from the file:  \n", file_object.read())
# print(file_object.read(10))
# print(file_object.read(25))
# file_object.seek(0)
#
# #read
# #readline
# print(file_object.readline())
# print(file_object.readline())
# #readlines
# file_object.seek(0)
# print(file_object.readlines(5))
# file_object.close()
#
# # write
# # write
# file_object = open("D:\AI, ML, DL\Python2021\Myfile.txt",'w')
# file_object.write("This is a new file line")
# # file_object.close()
#
# l1=["This is a sample text \n","This is another sample text \n","This is Third sample text \n","This is fourth sample text \n"]
# file_object.writelines(l1)
#
# #writelines
# '''
#
# import csv
# csv_file= open("D:\\AI, ML, DL\\Python2021\\Sample_csv.csv")
# csv_containt = csv.reader(csv_file)
#
# for i in csv_containt:
#     print("Containt in csv file: ", i)
#
#
# #
# # print(open.__doc__)


import json

person = '{"Name":"Sachin", "City":"Mumbai","Hobbies":["Music","Dance","Swimming"]}'
person_dict = json.loads(person)
print("Type of person dict: ", type(person_dict))


file_obj = open("D:\AI, ML, DL\Python2021\myjson.json",'w')
json.dump(person, file_obj)

















