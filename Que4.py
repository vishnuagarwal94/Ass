date = int(input("Enter date :"))
month = int(input("Enter month :"))
year = int(input("Enter year :"))
#print ("date="+date +"&" +"month = "+month)
y = year/4
a = year/100
c = year/400
print(y)
print(a)
print(c)
if year%4==0 and year%400 !=0:
    print("This is Leap Year & Days in Leap Year = 366 ")
else:
    for i in range(3):
        year = year +1
        if year%4==0 and year%400 !=0:
            year = str(year)
            print("year :"+year+" is Leap Year & Days in Leap Year = 366 ")
            break;
        else:
            year = year+1
    