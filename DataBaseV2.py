# 2019
# DataBaseV2
# Powered by LGleba
"""
Work with databases
Use Pickle
"""
# Import the Pickle module
import pickle

# 1 new file creation Function
def create_file(S, flag_baza, name1):
    print ("if you enter a name that is already in use,")
    print ("then the database will be overwritten to an empty one")
    
    # The database name
    name = input ("Enter the database name: ")

    # Checking for database availability
    if flag_baza:
        f = open(name1, 'wb')
        pickle.dump(S, f)
        f. close()
    
    # Creating a database template
    S = {'Name' : ['Quantity', 'Price']}
    
    # Return the dictionary and database name
    return S, name
    
# 2 the Function of opening an existing database
def open_file(S, flag_baza, name1):
    # Checking for database availability
    if flag_baza:
        f = open(name1, 'wb')
        pickle.dump(S, f)
        f. close()

    # Trying to open the database
    flag = 1
    while flag:
        name = input ("Enter the database name: ")
        try:
            f = open(name, 'rb')
            S = pickle.load(f)
            f. close()
            flag = 0
        except:
            print ("database entry Error!")

    # Return the dictionary and database
    return S, name
    
# 3 add record Function
def add_note(S):
    print("Records are stored in the form of:")
    print ("Name Quantity Price")

    # Attempt to add to the database
    flag = 1
    while flag:
        try:
            name = input ("Enter a name: ")
            kol = int (input ("Enter quantity: "))
            price = float(input("Enter the price: "))
            flag = 0
        except:
            print ("input Error!")

    # Checking for identical names
    if name in S:
        S1 = S[name] + [kol] + [price]
        S[name] = S1
    else:
        S. update({name : [kol,price]})

    # Return the dictionary
    return S

# 4 search Function for 1 parameter
def find_one(S):
    param = input ("Enter a name: ")

    # Check for availability by the 1st parameter
    if param in S:
        flag = 1
        i = 0
        S1 = S[param]
        while flag:
            try:
                a, b, c = param, S1[i], S1[i+1]
                print("┌────────────┬────────────┬────────────┐")
                print("│{:<12}│{:>12}│{:>12.4}│".format(param, S1[i], S1[i+1]))
                print("└────────────┴────────────┴────────────┘")
                i += 2
            except:
                flag = 0
    else:
        print ("no Record!")
    

# 5 search Function for 2 parameters
def find_two(S):
    # Trying to enter data
    flag = 1
    while flag:
        try:
            param = input ("Enter a name: ")
            param2 = int (input ("Enter quantity: "))
            flag = 0
        except:
            print ("input Error!")

    # Check for availability by the 1st parameter
    if param in S:
        S1 = S[param]
        i = 0
        while i != -1:
            try:
                # Check for availability by the 2nd parameter
                if S1[i] == param2:
                    a, b, c = param, S1[i], S1[i+1]
                    print("┌────────────┬────────────┬────────────┐")
                    print("│{:<12}│{:>12}│{:>12.4}│".format(param, S1[i], S1[i+1]))
                    print("└────────────┴────────────┴────────────┘")
                i += 2
            except:
                i = -1
    else:
        print ("no Record!")
    
# 6 function to output all records from a file
def output_file(S):
    # List of keys
    params = list(S. keys())

    # Make the headline higher than everyone else
    for i in range(len(params)):
        if params[i] = = " Name":
            params = params[:i] + params[i+1:]
            break
    params = ["Name"] + params

    # Key length
    n = len(params)

    # Number of records
    kol = 0
    for j in range(n):
        S1 = S[params[j]]
        i = 0
        while i != -1:
            try:
                a, b, c = params[j], S1[i], S1[i+1]
                i += 2
                kol += 1
            except:
                i = -1

    # Output records
    print("┌────────────┬────────────┬────────────┐")
    h = 0
    for j in range(n):
        S1 = S[params[j]]
        i = 0
        while i != -1:
            try:
                print("│{:<12}│{:>12}│{:>12.4}│".format(params[j], S1[i], S1[i+1]))
                if h != kol-1:
                    print("├────────────┼────────────┼────────────┤")
                h += 1
                i += 2
            except:
                i = -1
    print("└────────────┴────────────┴────────────┘")
    
# main function
def main():
    print ("Welcome!")
    print()

    # Initial values (dummy values)
    S = None
    name = None

    # Function selection flag
    flag = 1

    # Flag for existence of database
    flag_baza = 0
    
    while flag:
        print("1-Creating a new database")
        print("2-Opening an existing database")
        print("3-Adding a record to the database")
        print ("4-Search for the 1st parameter")
        print ("5-Search by 2 parameters")
        print ("6-Output all records from the database")
        print ("0-Output")

        # Check for correct input
        try:
            flag = int (input ("Enter the number of the desired function: "))

        # Execution in case of error
        except:
            print ("entered incorrectly")
            print()
            continue
        
        print()
        # Check for the selected function
        # 1 Function
        if flag == 1:
            S, name = create_file(S, flag_baza, name)
            flag_baza = 1
            print()
            print ("Done!")
            print()
            
        # 2 Function
        elif flag == 2:
            S, name = open_file(S, flag_baza, name)
            flag_baza = 1
            print()
            print ("Done!")
            print()
            
        # 3 Function
        elif flag == 3:
            # Checking for database availability
            if flag_baza:
                S = add_note(S)
            else:
                print ("Database not specified,")
                print ("you can use this function!")
            print()
            print ("Done!")
            print()
                    
        # 4 Function
        elif flag == 4:
            # Checking for database availability
            if flag_baza:
                find_one(S)
            else:
                print ("Database not specified,")
                print ("you can use this function!")
            print()
            print ("Done!")
            print()
                    
        # 5 Function
        elif flag == 5:
            # Checking for database availability
            if flag_baza:
                find_two(S)
            else:
                print ("Database not specified,")
                print ("you can use this function!")
            print()
            print ("Done!")
            print()
                    
        # 6 Function
        elif flag == 6:
            # Checking for database availability
            if flag_baza:
                output_file(S)
            else:
                print ("Database not specified,")
                print ("you can use this function!")
            print()
            print ("Done!")
            print()
        else:
            if flag != 0:
                print ("Try again!")
            if flag == 0:
                print ("Goodbye!")
                f = open(name, 'wb')
                pickle.dump(S, f)
                f. close()
            print()

# Main
main()
