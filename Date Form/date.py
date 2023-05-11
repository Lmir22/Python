#user will enter the date in this format
calendar = input('Please enter the date in this format (month/day/year): ')

#a function that will split the string using the character "/"
cal_List = calendar.split('/')

#the variable month as an integer in a sequence of a list
mth = int(cal_List[0])

#the variable day as an integer in a sequence of a list
dy = int(cal_List[1])

#the variable year as an integer in a sequence of a list
yr = int(cal_List[2])

#loop that determines the month based of the users input of 1-12
if mth == 1: mth = 'January'
elif mth == 2: mth = 'February'
elif mth == 3: mth = 'March'
elif mth == 4: mth = 'April'
elif mth == 5: mth = 'May'
elif mth == 6: mth = 'June'
elif mth == 7: mth = 'July'
elif mth == 8: mth = 'August'
elif mth == 9: mth = 'September'
elif mth == 10: mth = 'October'
elif mth == 11: mth = 'November'
elif mth == 12: mth = 'December'

#variable update containing the sequence of strings used for the date format
update = mth + ' ' + str(dy) + ', ' + str(yr) 

#display the date in the specific format 
print(update)
