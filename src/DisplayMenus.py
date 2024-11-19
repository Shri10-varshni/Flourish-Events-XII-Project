def entryChoice():
    print('-'*172)
    print('Welcome to Flourish events'.center(172,'_'))
    print('-'*172)
    print()
    print('''1-Create New Account
2-Login
3-Exit''')
    print('_'*172, end='\n\n')
    #entryChoice called in customerMenu

def userHomePage():     
    print('-'*172)
    print('Home Page'.center(172,'_'))
    print('-'*172)
    print()
    print('''1-Register for an event
2-Check registered event details
3-View Profile
4-Logout''')  
    print('_'*172, end='\n\n')
    #userHomePage called in userChoice

def registerEventPage():
    print('-'*172, '\n')
    print('''1-Enter Details again to register a new Event
2-Back to Home Page 
3-Logout''')    
    print('_'*172, end='\n\n')    
    #registerEventPage called in afterEventChoice