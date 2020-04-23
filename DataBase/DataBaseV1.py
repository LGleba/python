# 2019
# DataBaseV1
# Powered by LGleba
"""
Work with databases
"""
# 1 new file creation Function
def create_file():
    print ("if you enter a name that is already in use,")
    print ("then the database will be overwritten to an empty one")
    name = input ("Enter the database name: ")
    print()
    print ("Done!")
    print()
    # Open the file for recording
    f = open('{:}'.format(name), 'w')
    
    # Appended to the names of the columns
    f. write ("Name Quantity Price\n")
    
    # Close the file
    f. close()
    
    # Return the name of the database
    return name
    
# 2 the Function of opening an existing database
def open_file():
    name = input ("Enter the database name: ")
    # Error checking
    try:
        # Open the file for reading
        f = open('{:}'.format(name), 'r')
        
        # Close the file
        f. close()
        
        print()
        print ("Done!")
        print()
        # Return the name of the database
        return name

    # In case of error
    except:
        print()
        print("there is no such database!")
        print()
        
        # Return the dummy for verification
        return None
    
# 3 add record Function
def add_note(name):
    # Open the file for additional recording
    f = open('{:}'.format(name), 'a')
    
    print ("Enter Name, quantity, price:")
    # Error checking
    try:
        a = input ("Name: ")
        b = int(input("Number of: "))
        c = float (input ("Price: "))
        f. write("{:} {:} {:}\n".format(a, b, c))
        
    # In case of error
    except:
        print("You entered incorrect data")

    # Close the file
    f. close()
    
    print()
    print ("Done!")
    print()

# 4 search Function for 1 parameter
def find_one(name):
    param = input ("Enter a name: ")
    # Open the file for reading
    f = open('{:}'.format(name), 'r')

    # Check for a match
    for line in f:
        a, b, c = line.split()
        
        # The match
        flag = 1
        if a == param:
            print()
            print("{:} {:} {:}\n".format(a, b, c))
            flag = 0
        
    # Case of a mismatch
    if flag:
        print()
        print("there is No such entry\n")
        
    print ("Done!")
    print()
    # Close the file
    f. close()

# 5 search Function for 2 parameters
def find_two(name):
    print ("Enter name, Qty: ")
    param1 = input ("Enter a name: ")
    param2 = input ("Enter Qty: ")
    # Open the file for reading
    f = open('{:}'.format(name), 'r')
    # Check for a match
    flag = 1
    for line in f:
        a, b, c = line.split()
        # The match
        if a == param1 and b == param2:
            print()
            print("{:} {:} {:}\n".format(a, b, c))
            flag = 0

        # Case of a mismatch
    if flag:
        print()
        print("there is No such entry\n")

    print ("Done!")
    print()
    # Close the file
    f. close()
    
# 6 function to output all records from a file
def output_file(name):
    # Open the file for reading
    f = open('{:}'.format(name), 'r')

    # Flag for existence of records
    flag = 1

    # Check on the record
    flag_z = 0
    for line in f:
        flag_z = 1
        break

    # Close a file
    f. close()

    # Open the file for reading
    f = open('{:}'.format(name), 'r')
    
    # Output line by line entries
    if flag_z:
        print("┌───────────┬───────────┬───────────┐")
    fl = 0
    for line in f:
        if flag_z:
            flag_z = 0
        else:
            print("├───────────┼───────────┼───────────┤")
        a, b, c = line.split()
        print("│{:11}│{:11}│{:11}│\n".format (a, b, c), end="")
        flag = 0
        fl = 1
    if fl:
        print("└───────────┴───────────┴───────────┘")

    # Check for missing records
    if flag:
        print ("no Records!")

    print()
    # Close the file
    f. close()

# main function
def main():
    print ("Welcome!")
    print()

    # Function selection flag
    flag = 1

    # Flag for existence of database
    flag_baza = 0
    
    while flag:
        print("1-Creating a new database")
        print("2-Opening an existing database")
        print("3-Adding a record to the database")
        print("4-Search for the 1st parameter")
        print("5-Search by 2 parameters")
        print("6-Output all records from the database")
        print("0-Output")

        # Check for correct input
        try:
            flag = int (input("Enter the number of the desired function: "))

        # Execution in case of error
        except:
            print ("entered incorrectly")
            print()
            continue
        
        print()
        # Check for the selected function
        # 1 Function
        if flag == 1:
            flag_baza = 1
            name = create_file()
            
        # 2 Function
        elif flag == 2:
            name = open_file()
            if name != None:
                flag_baza = 1
                
        # 3 Function
        elif flag == 3:
            # Checking for database availability
            if flag_baza:
                add_note(name)
                
            else:
                print("You didn't specify the database!")
                name = open_file()
                if name != None:
                    flag_baza = 1
                    
        # 4 Function
        elif flag == 4:
            # Checking for database availability
            if flag_baza:
                find_one(name)
                
            else:
                print("You didn't specify the database!")
                name = open_file()
                if name != None:
                    flag_baza = 1
                    
        # 5 Function
        elif flag == 5:
            # Checking for database availability
            if flag_baza:
                find_two(name)
                
            else:
                print("You didn't specify the database!")
                name = open_file()
                if name != None:
                    flag_baza = 1
                    
        # 6 Function
        elif flag == 6:
            # Checking for database availability
            if flag_baza:
                output_file(name)
                
            else:
                print("You didn't specify the database!")
                name = open_file()
                if name != None:
                    flag_baza = 1
                    
        else:
            if flag != 0:
                print ("Try again!")
            if flag == 0:
                print ("Goodbye!")
            print()

# Main
main()
