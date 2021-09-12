import datetime
from datetime import time # sanity check to make sure it gets imported
from datetime import date # ditto
import sys
import time
import os # this is only used to re-open the program at the end if desired
import msvcrt # to enable inputs without requiring Enter after
date = datetime.date # because otherwise it breaks by the time combining


print("Work Hours Calculator, By Manmeyco")
print() # blank line
print("This is a simple calculator for calculating (duh) total pay for a workweek. You put in your start and end times for each day, and it will figure out the total dollar amount you have earned.")
print("For workdays longer than 8 hours, it will give you time and a half for overtime.")
print() # blank line
print("Please note that all start times must be in the AM, and end times must be in the PM, no later than 9:59 PM.") # because otherwise my simpleton 24 hour converter won't work
print() # blank line


# This section is inputting the start and end times
# Monday
print() # blank line
print("Did you work on Monday?")
print("y for Yes, n for No.")
print() # blank line
worked_monday = msvcrt.getwch()

if(worked_monday == 'y'):
    mon_start_hour = int(input("Monday Start Hour:")) # prompt to input starting hour for Monday
    mon_start_min = int(input("Monday Start Minute:")) # ditto starting minute
    mon_end_hour = int(input("Monday End Hour:")) # ditto ending hour

    # Simpleton 12 hr to 24 hr format converter
    # Well, actually a 9 hr to 21 hr converter
    # yes, I could've added all of the hours, but I am lazy, and I only wanted to type it 9 times
    # and anyways, why are you working past 9?
    # If you choose a bad hour, the program will exit
    # yes, that's right - my program doesn't have bad days. It has bad hours.
    if(mon_end_hour == 1):
        mon_end_hour = 13
    elif(mon_end_hour == 2):
        mon_end_hour = 14
    elif(mon_end_hour == 3):
        mon_end_hour = 15
    elif(mon_end_hour == 4):
        mon_end_hour = 16
    elif(mon_end_hour == 5):
        mon_end_hour = 17
    elif(mon_end_hour == 6):
        mon_end_hour = 18
    elif(mon_end_hour == 7):
        mon_end_hour = 19
    elif(mon_end_hour == 8):
        mon_end_hour = 20
    elif(mon_end_hour == 9):
        mon_end_hour = 21
    else:
        print("Error! Invalid Monday end hour. Please close and reopen this program, and input an end hour from 1 PM to 9 PM.")
        input("Press ENTER to exit.")
        sys.exit()
    
    mon_end_min = int(input("Monday End Minute:")) # ditto ending minute (OK I think you get it)
else:   # Make all times equal zero.
    mon_start_hour = 0
    mon_start_min = 0
    mon_end_hour = 0
    mon_end_min = 0

# Tuesday
print() # blank line
print("Did you work on Tuesday?")
print("y for Yes, n for No.")
print() # blank line
worked_tuesday = msvcrt.getwch()

if(worked_tuesday == 'y'):
    tue_start_hour = int(input("Tuesday Start Hour:"))
    tue_start_min = int(input("Tuesday Start Minute:"))
    tue_end_hour = int(input("Tuesday End Hour:"))

    if(tue_end_hour == 1):
        tue_end_hour = 13
    elif(tue_end_hour == 2):
        tue_end_hour = 14
    elif(tue_end_hour == 3):
        tue_end_hour = 15
    elif(tue_end_hour == 4):
        tue_end_hour = 16
    elif(tue_end_hour == 5):
        tue_end_hour = 17
    elif(tue_end_hour == 6):
        tue_end_hour = 18
    elif(tue_end_hour == 7):
        tue_end_hour = 19
    elif(tue_end_hour == 8):
        tue_end_hour = 20
    elif(tue_end_hour == 9):
        tue_end_hour = 21
    else:
        print("Error! Invalid Tuesday end hour. Please close and reopen this program, and input an end hour from 1 PM to 9 PM.")
        input("Press ENTER to exit.")
        sys.exit()

    tue_end_min = int(input("Tuesday End Minute:"))
else:
    tue_start_hour = 0
    tue_start_min = 0
    tue_end_hour = 0
    tue_end_min = 0
    
# Wednesday
print() # blank line
print("Did you work on Wednesday?")
print("y for Yes, n for No.")
print() # blank line
worked_wednesday = msvcrt.getwch()

if(worked_wednesday == 'y'):
    wed_start_hour = int(input("Wednesday Start Hour:"))
    wed_start_min = int(input("Wednesday Start Minute:"))
    wed_end_hour = int(input("Wednesday End Hour:"))

    if(wed_end_hour == 1):
        wed_end_hour = 13
    elif(wed_end_hour == 2):
        wed_end_hour = 14
    elif(wed_end_hour == 3):
        wed_end_hour = 15
    elif(wed_end_hour == 4):
        wed_end_hour = 16
    elif(wed_end_hour == 5):
        wed_end_hour = 17
    elif(wed_end_hour == 6):
        wed_end_hour = 18
    elif(wed_end_hour == 7):
        wed_end_hour = 19
    elif(wed_end_hour == 8):
        wed_end_hour = 20
    elif(wed_end_hour == 9):
        wed_end_hour = 21
    else:
        print("Error! Invalid Wednesday end hour. Please close and reopen this program, and input an end hour from 1 PM to 9 PM.")
        input("Press ENTER to exit.")
        sys.exit()

    wed_end_min = int(input("Wednesday End Minute:"))
else:
    wed_start_hour = 0
    wed_start_min = 0
    wed_end_hour = 0
    wed_end_min = 0

# Thursday
print() # blank line
print("Did you work on Thursday?")
print("y for Yes, n for No.")
print() # blank line
worked_thursday = msvcrt.getwch()

if(worked_thursday == 'y'):
    thu_start_hour = int(input("Thursday Start Hour:"))
    thu_start_min = int(input("Thursday Start Minute:"))
    thu_end_hour = int(input("Thursday End Hour:"))

    if(thu_end_hour == 1):
        thu_end_hour = 13
    elif(thu_end_hour == 2):
        thu_end_hour = 14
    elif(thu_end_hour == 3):
        thu_end_hour = 15
    elif(thu_end_hour == 4):
        thu_end_hour = 16
    elif(thu_end_hour == 5):
        thu_end_hour = 17
    elif(thu_end_hour == 6):
        thu_end_hour = 18
    elif(thu_end_hour == 7):
        thu_end_hour = 19
    elif(thu_end_hour == 8):
        thu_end_hour = 20
    elif(thu_end_hour == 9):
        thu_end_hour = 21
    else:
        print("Error! Invalid Thursday end hour. Please close and reopen this program, and input an end hour from 1 PM to 9 PM.")
        input("Press ENTER to exit.")
        sys.exit()

    thu_end_min = int(input("Thursday End Minute:"))
else:
    thu_start_hour = 0
    thu_start_min = 0
    thu_end_hour = 0
    thu_end_min = 0

# Friday
print() # blank line
print("Did you work on Friday?")
print("y for Yes, n for No.")
print() # blank line
worked_friday = msvcrt.getwch()

if(worked_friday == 'y'):
    fri_start_hour = int(input("Friday Start Hour:"))
    fri_start_min = int(input("Friday Start Minute:"))
    fri_end_hour = int(input("Friday End Hour:"))

    if(fri_end_hour == 1):
        fri_end_hour = 13
    elif(fri_end_hour == 2):
        fri_end_hour = 14
    elif(fri_end_hour == 3):
        fri_end_hour = 15
    elif(fri_end_hour == 4):
        fri_end_hour = 16
    elif(fri_end_hour == 5):
        fri_end_hour = 17
    elif(fri_end_hour == 6):
        fri_end_hour = 18
    elif(fri_end_hour == 7):
        fri_end_hour = 19
    elif(fri_end_hour == 8):
        fri_end_hour = 20
    elif(fri_end_hour == 9):
        fri_end_hour = 21
    else:
        print("Error! Invalid Friday end hour. Please close and reopen this program, and input an end hour from 1 PM to 9 PM.")
        input("Press ENTER to exit.")
        sys.exit()

    fri_end_min = int(input("Friday End Minute:"))
else:
    fri_start_hour = 0
    fri_start_min = 0
    fri_end_hour = 0
    fri_end_min = 0

# Combining the hours and minutes (there's probably an easier way to do this, but whatever)

# Monday
mon_start_time = datetime.time(mon_start_hour, mon_start_min)
mon_end_time = datetime.time(mon_end_hour, mon_end_min)

# Tuesday
tue_start_time = datetime.time(tue_start_hour, tue_start_min)
tue_end_time = datetime.time(tue_end_hour, tue_end_min)

# Wednesday
wed_start_time = datetime.time(wed_start_hour, wed_start_min)
wed_end_time = datetime.time(wed_end_hour, wed_end_min)

# Thursday
thu_start_time = datetime.time(thu_start_hour, thu_start_min)
thu_end_time = datetime.time(thu_end_hour, thu_end_min)

# Friday
fri_start_time = datetime.time(fri_start_hour, fri_start_min)
fri_end_time = datetime.time(fri_end_hour, fri_end_min)


# This section is for getting a total time elapsed, for each day, in datetime format
# APPARENTLY, you can't subtract datetime.time, you can only subtract datetime
# so you need to combine the time with a date
# so I am using today's date because it makes no difference to me
# because of that, don't run this program at 11:59 PM, or it may give you an unexpected answer
# you might want to change this
# oh, and the combine module is inside of datetime.datetime, because WHY NOT

# Monday
mon_total_time = datetime.datetime.combine(date.today(), mon_end_time) - datetime.datetime.combine(date.today(), mon_start_time)

# Tuesday
tue_total_time = datetime.datetime.combine(date.today(), tue_end_time) - datetime.datetime.combine(date.today(), tue_start_time)

# Wednesday
wed_total_time = datetime.datetime.combine(date.today(), wed_end_time) - datetime.datetime.combine(date.today(), wed_start_time)

# Thursday
thu_total_time = datetime.datetime.combine(date.today(), thu_end_time) - datetime.datetime.combine(date.today(), thu_start_time)

# Friday
fri_total_time = datetime.datetime.combine(date.today(), fri_end_time) - datetime.datetime.combine(date.today(), fri_start_time)


# Sanity checkpoint!
# This next section won't be in comments, but you can put it in if you don't need to check
# and then you can take it out to check that your times are correct

print() # blank line
print("Calculating total time for each day...")
time.sleep(3)
print() # blank line
print("Total time worked for Monday:")
print(mon_total_time)
print("Total time worked for Tuesday:")
print(tue_total_time)
print("Total time worked for Wednesday:")
print(wed_total_time)
print("Total time worked for Thursday:")
print(thu_total_time)
print("Total time worked for Friday:")
print(fri_total_time)

# Print total time (useful to know hours in a week worked)
hours_in_week = mon_total_time + tue_total_time + wed_total_time + thu_total_time + fri_total_time
print("Total time worked for the week:")
print(hours_in_week)

# convert timedelta object to a normal integer

mon_total_sec = mon_total_time.total_seconds()
tue_total_sec = tue_total_time.total_seconds()
wed_total_sec = wed_total_time.total_seconds()
thu_total_sec = thu_total_time.total_seconds()
fri_total_sec = fri_total_time.total_seconds()


# add time and a half if you worked over 8 hours

# Monday
if(mon_total_sec > 28800):
    print() # blank line
    print("Calculating time and a half for Monday...")
    time.sleep(3) # Time delays to make it feel like it's calculating something, and to give you time to read, you can remove all "time.sleep" lines if you wish
    mon_ot1 = mon_total_sec - 28800 # subtract 8 hours from total time worked
    mon_ot2 = mon_ot1 * 1.5 # multiply overtime by 1.5
    mon_total_sec = mon_ot2 + 28800 # add overtime back to total time
    
# Tuesday
if(tue_total_sec > 28800):
    print() # blank line
    print("Calculating time and a half for Tuesday...")
    time.sleep(3)
    tue_ot1 = tue_total_sec - 28800
    tue_ot2 = tue_ot1 * 1.5
    tue_total_sec = tue_ot2 + 28800

# Wednesday
if(wed_total_sec > 28800):
    print() # blank line
    print("Calculating time and a half for Wednesday...")
    time.sleep(3)
    wed_ot1 = wed_total_sec - 28800
    wed_ot2 = wed_ot1 * 1.5
    wed_total_sec = wed_ot2 + 28800

# Thursday
if(thu_total_sec > 28800):
    print() # blank line
    print("Calculating time and a half for Thursday...")
    time.sleep(3)
    thu_ot1 = thu_total_sec - 28800
    thu_ot2 = thu_ot1 * 1.5
    thu_total_sec = thu_ot2 + 28800

# Friday
if(fri_total_sec > 28800):
    print() # blank line
    print("Calculating time and a half for Friday...")
    time.sleep(3)
    fri_ot1 = fri_total_sec - 28800
    fri_ot2 = fri_ot1 * 1.5
    fri_total_sec = fri_ot2 + 28800


# convert seconds to hours

mon_total_hr = mon_total_sec / 60 / 60
tue_total_hr = tue_total_sec / 60 / 60
wed_total_hr = wed_total_sec / 60 / 60
thu_total_hr = thu_total_sec / 60 / 60
fri_total_hr = fri_total_sec / 60 / 60


# define hourly wage
# you can edit the hourly_wage variable for your wage

print() # blank line
print("Calculating your wages...")
time.sleep(3)
print() # blank line

hourly_wage = 14 # <--- Edit this number for your hourly wage

your_wage = "Your hourly wage is ${} an hour. You can change this by opening this file in a text editor, such as Notepad or IDLE, and editing the hourly_wage variable.".format(hourly_wage)
print(your_wage)


# finally calculating total pay, for each day

mon_pay = mon_total_hr * hourly_wage
tue_pay = tue_total_hr * hourly_wage
wed_pay = wed_total_hr * hourly_wage
thu_pay = thu_total_hr * hourly_wage
fri_pay = fri_total_hr * hourly_wage


# adding it all up

total_pay = mon_pay + tue_pay + wed_pay + thu_pay + fri_pay

# rounding the sum - if you don't want rounding, remove this
total_pay = round(total_pay, 2) # .004 and lower rounded down to 0.00, .005 and up rounded up to 0.01

print() # blank line
print("Your pay for the week is...")
time.sleep(3)
print("$", total_pay)

print() # blank line
print("Thank you for using my calculator!\nLicensed by Manmeyco under the GNU GPLv3 and later.\nHave a great day!")

# Keep python open so you can see the result without Python closing on you
# edit: stuck it into a comment because IT DIDN'T WORK
# edit 2: not anymore - apparently, if there's an error, python closes anyways

# Attempt to be able to re-open the program to calculate an additional week

print() # blank line
print("Do you want to calculate another week?")
print("y for Yes, n for No.")
print() # blank line
another_week = msvcrt.getwch()

if(another_week == 'y'):
    os.system('python workhours.py')
else:   # For some reason it prompts to press enter twice. Solve later. -- Turns out it was somehow calling it twice. Else solved it ¯\_(ツ)_/¯
    print() # blank line
    input('Press ENTER when done!')
