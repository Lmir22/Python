#displaying text of the amount of books read.
num_Books = int(input("Please enter the amount of books read: "))
#message variable with an empty string
msg = ""

#scenario if the a negative number is entered
if num_Books < 0:
    msg = "An error has occured in the program. \n" + \
              "Please enter a positive number and try again. \n"
    #no error then display this message
else:
    msg = "Congratulations! You have recieved "

#calculate the amount of points that reading each book is worth
    if num_Books >= 0 and num_Books <= 1: msg += "0 "
    elif num_Books >= 2 and num_Books <= 3: msg += "5 "
    elif num_Books >= 4 and num_Books <= 5: msg += "15 "
    elif num_Books >= 6 and num_Books <= 7: msg += "30 "
    elif num_Books >= 8: msg += "60 "

#displaying the points
    msg += "pts."

print(msg)