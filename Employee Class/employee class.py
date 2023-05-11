#class created called Employee
class Employee:

    #attributes that will be initialized
    def __init__(self, nm, id, depart, title):
        self._nm = nm            #attribute for Name
        self._id = id            #attribute for ID
        self._depart = depart    #attribute for Department
        self._title = title      #attribute for Job Title

    #setting and returning the attributes to the corresponding string 
    #%s is used to format values in string by conversion and can be used 
    #for strings inside strings
    #%d is used essentially the same way as %s but for integers and decimals
    def __str__(self):
        return 'Name: %s\nID Number: %d\nDepartment: %s\nJob Title: %s\n' % (self._nm, self._id, self._depart, self._title)
    
#creates the objects for the employees that will match their attributes
def emp():
    emp_1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    emp_2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
    emp_3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    #displays the information for each employee
    print('Employee #1 Info:')
    print(emp_1)
    print('Employee #2 Info:')
    print(emp_2)
    print('Employee #3 Info:')
    print(emp_3)

#Ends the main program
emp()
