#initializing count to 0
CNT = 0

#exception handler
try:

    #opens and reads the file
    in_F = open('names.txt', 'r')

    #reads the amount of items in list using loops
    for line in in_F:
        print(line)
        CNT += 1

    #closes the file
    in_F.close()

#Displaying the number of items in the list
except IOError:
    CNT = 0
print ("The number of items in the list is " + str(CNT))