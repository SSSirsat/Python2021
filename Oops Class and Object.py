#Class and object
#Oops
# class Library:
#     books_count = 0
#     def add_books(self, name, author, price, dat):
#         self.naam = name
#         self.auth = author
#         self.daam = price
#         self.dates =dat
#         print(self.daam,self.naam, self.dates,self.auth)
#         Library.books_count +=1
#
# # b1= Library()b1= Library()"Harry Potter and the Witch", "shuabhm", price=251, 20-05-2021
# b1= Library()
# b1.add_books("Harry Potter and the Witch", "shuabhm", price=251, dat=2546)
# b1.add_books()
#
#
# # #How many books in the Library
# # print("Books count are {} in the library".format(b1.books_count))

class Cricketer:
    def __init__(self, name, city, runs, matches,balls):
        self.name = name
        self.city = city
        self.runs = runs
        self.matches = matches
        self.balls = balls

    def getdetails(self):
        print("The Cricketer name is {} and city name is {}.".format(self.name, self.city))

    def avg_score(self):
        bat_avg = self.runs / self.matches
        print("Batting average of {} is {}".format(self.name, bat_avg))

    def sticke_rate(self):
        batting_strk= self.runs/self.balls *100
        print("Strike Rate of {} is {}".format(self.name, batting_strk))


s1 = Cricketer("Sachin", "Mumbai", 185065, 450,250505)
s1.getdetails()
s1.avg_score()
s1.sticke_rate()










