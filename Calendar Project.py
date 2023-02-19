import sys
import calendar
import datetime

start = input("Would you like to begin? Y/N").lower()

if start == "y":
    print("Alright! Lets go!")
else:
    sys.exit
    
# day selection
days = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for p, day in enumerate(days):
    print("{0}: {1}".format(p, day))

while True:
            user_dayinput = input("Select your day by entering the digit listed before it: ")
            try:
                user_daynumber = int(user_dayinput)
                if 0 <= user_daynumber <= 6:
                    break
                else:
                    print("Error: Enter a number from 0 to 6")
            except ValueError:
                print("Error: Enter a valid integer.")
                
selected_day = days[user_daynumber]
print("You selected:", selected_day)

    
# month selection
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i, month in enumerate(months):
    print("{0}: {1}".format(i, month))
while True:
            user_monthinput = input("Select your month by entering the digit listed before it: ")
            try:
                user_monthnumber = int(user_monthinput)
                if 0 <= user_monthnumber <= 11:
                   break
                else:
                    print("Error: Enter a number from 0 to 11.")
            except ValueError:
                print("Error: Enter a valid integer.")
selected_month = months[user_monthnumber]


# year selection
while True:
    selected_year = input("Please enter a year: ")
    try:
        selected_year = int(selected_year)
        if datetime.MINYEAR <= selected_year <= datetime.MAXYEAR: 
           break
        else:
            print("Error: Please enter a real year.")
    except ValueError:
        print("Error: Enter a valid year.")
        
from datetime import date

firstdayofmonth = date(selected_year, (user_monthnumber+1), 1).isoweekday()

# print(firstdayofmonth)
firstxdayinthemonthdate = (user_daynumber-firstdayofmonth)%7+1
# print(firstxdayinthemonthdate)


user_monthnumber= user_monthnumber+1
days_in_month = calendar.monthrange(selected_year, user_monthnumber)[1]
user_monthnumber= user_monthnumber-1

w= 0
while firstxdayinthemonthdate<= days_in_month:
    w = w+1
    firstxdayinthemonthdate += 7

print("There are", w, selected_day, "in", selected_month, "of year", selected_year)
