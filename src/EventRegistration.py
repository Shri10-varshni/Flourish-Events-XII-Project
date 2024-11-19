from Validations import date_validation,numeric_validation
from UserLogin import validateUser
from EventDetails import getUserEvents,getEventInformation
from DisplayMenus import entryChoice,registerEventPage,userHomePage
from EventPageLoad import displayEventTypes,loadEventConfig,get_connection
from FrontendDisplay import eventTypeIDForEventType,locationForAnEvent,addonsForAnEvent,displayEstimatedCost,confirmRegistration,getNewUserDetails, displayEventDetails, displayUserDetails

eventIDQuery = "SELECT MAX(EVENT_ID) FROM EVENT_INFORMATION"
registerEventQuery = "INSERT INTO EVENT_INFORMATION(USER_ID,EVENT_TYPEID,EVENT_NAME,START_DATE,END_DATE,LOCATION_ID,ATTENDEE_COUNT,ADD_ONS,ESTIMATED_COST,EVENT_DESCRIPTION,EVENT_STATUS) VALUES (%s,%s,%s,CONVERT(%s,DATETIME),CONVERT(%s,DATETIME),%s,%s,%s,%s,%s,0)"
registerEventAddonQuery = "INSERT INTO EVENT_ADDONS_INFORMATION(EVENT_ID,ADDON_ID,ADDON_COUNT,ADDON_COST) VALUES (%s,%s,%s,%s)"
increaseEventCountQuery = "UPDATE USER_INFORMATION SET EVENT_COUNT = EVENT_COUNT+1 WHERE USER_ID = %s"

#Returns the last registered Event_ID + 1 from table EVENT_INFORMATION. This will be the Event_ID for the next Registration.
def getEventID():
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(eventIDQuery)
    Event_ID=cursor.fetchone()[0]+1
    return Event_ID

#Registers the event and returns register status (Inserts values into the table EVENT_INFORMATION) 
def registerEvent(USER_ID,EVENT_TYPEID,EVENT_NAME,START_DATE,END_DATE,LOCATION_ID,ATTENDEE_COUNT,ADD_ONS,ESTIMATED_COST,EVENT_DESCRIPTION):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(registerEventQuery , [USER_ID,EVENT_TYPEID,EVENT_NAME,START_DATE,END_DATE,LOCATION_ID,ATTENDEE_COUNT,ADD_ONS,ESTIMATED_COST,EVENT_DESCRIPTION])
    conn.commit()
    eventRegistered = None
    if(cursor.rowcount > 0):
        print("Event Registered Successfully")
        eventRegistered = True
    else:
        print("Error in Registering Event")
        eventRegistered = False
    cursor.close
    return eventRegistered


#Gets login info from user; Validates the information; returns the UserID
def getLoginInfo(tries):
    print('_'*172)
    print('Enter credentials to login')
    print('\n')
    username=input('User Name: ')
    password=input('Password: ')
    userid=validateUser(username,password) 
    if userid==None:
        if tries<3:
           getLoginInfo(tries+1)
        else:
            print('You have entered wrong credentials thrice. Redirecting to Main Page. Please create a new account if you do not have one.')
            print('_'*172)
            customerMenu()
    return userid  

#Updates the event count of a user after a successful registration 
def updateEventCount(increaseEventCountQuery,USER_ID):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(increaseEventCountQuery , [USER_ID])
    conn.commit()


#Registers each Add_on into the table EVENT_ADDONS_INFORMATION individually. Returns the register status
def registerEventAddons(eventAddons):
     conn = get_connection()
     cursor = conn.cursor(buffered=True)
     for addon in eventAddons:
        cursor.execute(registerEventAddonQuery,addon)
     conn.commit()
     addonsRegistered = None
     if(cursor.rowcount > 0):
        print("Event Addons Registered Successfully")
        addonsRegistered = True
     else:
        print("Error in Registering Event Addon")
        addonsRegistered = False
     cursor.close
     return addonsRegistered

#Choice Excecutaion after an Event is registered (OR) after an Event detail Entry is discarded 
def afterEventChoice(USER_ID):
    print('\n')
    registerEventPage()
    userch=input('Enter your Choice: ')
    print('\n')
    if userch=='1':
        getEventRegisterDetails(USER_ID)
    elif userch=='2':   
        userChoice(USER_ID)
    elif userch=='3':                                                                 #
        customerMenu()   
    else:
        print('Invalid Choice. Kindly re-enter.')
        afterEventChoice(USER_ID)

#Rgisters an Event in the Database after getting all the necessary parameters from the user
def getEventRegisterDetails(USER_ID):
    EVENT_ID=getEventID()                                                                                                                                            #Function in EventRegistration
    eventTypesInfo=displayEventTypes()                                                                                                                               #Function in EventPageLoad       
    EVENT_TYPEID=eventTypeIDForEventType(eventTypesInfo)                                                                                                             #          
    event_information,eventAddons,eventLocations=loadEventConfig(EVENT_TYPEID)                                                                                       #        
    EVENT_NAME=input('Event Name: ') 
    START_DATE=date_validation(input('Start Date: '))
    END_DATE=date_validation(input('End Date: '))
    ATTENDEE_COUNT=numeric_validation(input('Attendee Count: '))
    LOCATION_ID=locationForAnEvent(EVENT_ID,eventLocations)                                                                                                          #        
    ALL_ADD_ONS=addonsForAnEvent(EVENT_ID,eventAddons)                                                                                                               #        
    ADD_ONS=len(ALL_ADD_ONS)
    print('Hey dear customer, we care about little details for your personal touch. Metion all your specifications in the below description!')
    EVENT_DESCRIPTION=input('Personal Description: ')
    print('\n')
    ESTIMATED_COST=displayEstimatedCost(event_information, ALL_ADD_ONS)                                                                                              #        
    confirm=confirmRegistration()                                                                                                                                  #     
    if confirm==True:
        eventRegistered=registerEvent(USER_ID,EVENT_TYPEID,EVENT_NAME,START_DATE,END_DATE,LOCATION_ID,ATTENDEE_COUNT,ADD_ONS,ESTIMATED_COST,EVENT_DESCRIPTION)       #
        if(len(ALL_ADD_ONS)>0):
            addonsRegistered=registerEventAddons(ALL_ADD_ONS)                                                                                                            #        
        if eventRegistered==True :
            updateEventCount(increaseEventCountQuery,USER_ID)
            afterEventChoice(USER_ID)
        else:
            print('Sorry for the inconvenience. Kindly re-Enter Details.')
            getEventRegisterDetails(USER_ID)
    else:
        afterEventChoice(USER_ID)

#User Home Page choice Execution
def userChoice(USER_ID):
    userHomePage()
    userch=input('Enter your Choice: ')
    print('\n')
    if userch=='1':                                                            #Register for a new Event
        print('_'*80, 'Event Registration', '_'*80, end='\n')
        print('\n\n')
        getEventRegisterDetails(USER_ID)
    elif userch=='2':                                                          #View Details of Registered Events   
        userEvents=getUserEvents(USER_ID)
        if len(userEvents) >0:
            print('_'*80, 'Events Registered', '_'*80, end='\n')
            for event in userEvents:
                print('_'*172, end='\n')
                for detail in event: 
                    print(detail,' : ',event[detail], '\n')
                print('_'*172, end='\n')   
            print('\n\n')     
            EVENT_ID=numeric_validation(input("Enter Event_ID to View Event Details  :"))
            print()
            displayEventDetails(EVENT_ID,USER_ID)
            userChoice(USER_ID)
        else:
            print('No registered Events yet')   
            print('\n\n') 
            userChoice(USER_ID)
    elif userch=='3':                                                          #View Profile Details   
        displayUserDetails(USER_ID) 
        userChoice(USER_ID)  
    elif userch=='4':                                                          #Logout - Redirects to Entry Page   
        print('_'*70, 'Logout Successful', '_'*70, end='\n\n')
    else:                                                                      #Choice Invalid - Performs function again
        print("Invalid choice. Please check and Re-Enter!")
        userChoice(USER_ID)


'''#Final Execution Menu of Flourish Events        
def customerMenu ():
    entryChoice()
    ch=input('Enter your choice: ')
    print('\n')
    if ch=='1':
        getNewUserDetails() 
        customerMenu()  
    elif ch=='2':
        USER_ID=getLoginInfo(0)
        userChoice(USER_ID)
    elif ch=='3':
        input('Are you sure you want to close the Application? Enter (Yes) or (No) :')
    else:
        print('_'*172,'\nInvalid Choice. Kindly re-enter.\n','_'*172, end='\n\n') 
        customerMenu()   '''

def customerMenu ():
    while True:
        entryChoice()
        ch=input('Enter your choice: ')
        print('\n')
        if ch=='1':
            getNewUserDetails()
        elif ch=='2':
            USER_ID=getLoginInfo(0)
            userChoice(USER_ID)    
        elif ch=='3':
            print('Thank you for using our services.')  
            break
        else:
            print('Invalid Choice. Kindly re-Enter')  
