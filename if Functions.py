#inputs 2 sides of trinagle if its rectangle  or a square  and perfo
# rm calcualction of perimeter and area
# Inputs 3 sides of Triangle and based on sides entered ,
# display if its a Equilateral , Isoscale and and right angle triangle
M1=10
M2=60
M3=100
M4=93
M5=100
sum_marks = M1+M2+M3+M4+M5
avg = sum_marks /5
print("Average obtained by student: ",avg)

if avg >= 40:
    print("You have Passed")
    if avg > 90:
        if avg >95:
            print("wowo wowo wowo woow")
            if avg ==100:
                print("Centum")
        print("You Have got Grade A")
    if avg > 80:
        print("You Have got Grade B")
    if avg > 70:
        print("You Have got Grade C")

else:
    print("Sorry You have Failed")
    print("You got Grade E")