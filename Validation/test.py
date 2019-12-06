import datetime

a_str = "1 2 3 4 5 6"
b_str = a_str.replace(" ", "")
print(b_str.isdigit())

nde_str = "sigurdur@nanair.is"
siggf  = nde_str.split("@")
print(siggf)
nd = int(1)

year = int(input("Enter a year: "))
month = int(input("Enter a month "))
day = int(input("Enter a day: "))
hour = int(input("Enter a hour: "))
minute = int(input("Enter a minute: "))
second = int(input("Enter a second: "))
for index in range(7):
    c = datetime.datetime(year, month, day+index, hour, minute, second).isoformat()
    
    print(c)

