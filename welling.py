
#Residents

    #Delete Resident
def killem():
    mark = input('Delete all Records of Residents with chosen name, email, etc: ')
    #Opena  CSV
    residents = open('residents.txt', mode='r')
    #Copy Every Line From CSV
    peeps = residents.readlines()
    residents.close
    #Overwrite so the selection is excluded
    residents = open('residents.txt', mode='w')
    for lad in peeps:
        if not mark in lad:
            residents.write(lad)
    residents.close()

    #Retrieve Person
def getem():
    mark = input('Search Residents by using name, email, etc: ')
    #Open CSV
    residents = open('residents.txt', mode='r+')
    #copy every line from csv
    peeps = residents.readlines()
    for lad in peeps:
        if mark in lad:
            info = lad.split(',')
            #Didn't want to have to write out each case
            fields = ['Name: ','Room: ', 'Phone: ','Email: ']
            for stuff in info:
                print(fields[info.index(stuff)] + stuff)

    #Prompt for Resident Creation
def birthem():
    #User Input
    name = input("Enter Resident's Full Name: ")
    room = input("Enter Room Number: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    #Save to CSV
    residents = open('residents.txt', mode='a')
    residents.write(name + ',' + room + ',' + phone + ',' + email + '\n')  
    residents.close()



#Coffee Hour

    #Prompt for Coffee Hour Creation
def brew():
    #Input from User
    name = input("Enter Resident's Full Name: ")
    month = str(input("Enter Month (mm): "))
    if len(month) == 1:
        month = '0' + month
    year = str(input("Enter Year (yyyy): "))
    day = str(input("Enter Day (dd): "))
    if len(day) == 1:
        day = '0' + day
    datekey = year + month + day 
    #Open CSV
    ch = open('times.txt', mode='a')
    ch.write(datekey + ',' + month + ',' + day +  ',' + year + ',' + name + '\n')  
    ch.close()


    #List Coffee Hour Sessions
def siplist():
        #Open CSV
        coffeehours = open('times.txt', mode='r')
        listing = coffeehours.readlines()
        #Set up the dates in a proper order
        listing.sort()
        for hour in listing:
            info = hour.split(',')
            print('%s-%s-%s: %s' % (info[1],info[2],info[3],info[4]))


    #Delete Coffee Hour Session
def spillsip():
    month = str(input("Enter Month (mm): "))
    if len(month) == 1:
        month = '0' + month
    year = str(input("Enter Year (yyyy): "))
    day = str(input("Enter Day (dd): "))
    if len(day) == 1:
        day = '0' + day
    #datekey is used to sort when listing the dates
    datekey = year + month + day 
    coffeehours = open('times.txt', mode='r')
    #Copy Every Line From CSV
    listing = coffeehours.readlines()
    coffeehours.close
    #Open CSV to write the copied
    coffeehours = open('times.txt', mode='w')
    for hour in listing:
        if not datekey in hour:
            coffeehours.write(hour)
    coffeehours.close()


#Menu Options

def pickem(): 
    go = True 
    while go is True : 
        #Options
        selection = input("""
                1. Look Up Resident 
                2. Register Resident
                3. Delete Resident
                4. Coffee Hour
                5. Quit
                """)
        #To Ensure it's not a string
        selection = int(selection)

        if selection == 1:
            getem()  
            input("Press Enter to Continue")
        if selection == 2:
            birthem()
        if selection == 3:
            killem()
        if selection == 4:
            whatsip() 
    #Quit
        if selection > 4:
            go = False

#Coffee Hour
def whatsip(): 
    keep = True 
    while keep is True : 
        #Options
        tap = input("""
                1. View Coffee Hours 
                2. Sign Up for Coffee Hour
                3. Delete Coffee Hour
                4. Quit
                """)
        #Make it an integer
        tap = int(tap)

        if tap == 1:
            siplist()  
            input("Press Enter to Continue")
        if tap == 2:
            brew()
        if tap == 3:
            spillsip()
    #Quit
        if tap > 3:
            keep = False
