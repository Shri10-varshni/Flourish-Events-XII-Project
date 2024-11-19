# Database connection
import mysql.connector

conn = None

def get_connection():
    if(conn is None):
        get_connection()
    return conn

def establish_connection():
        conn = mysql.connector.connect(
            host="localhost",
            database="EVENT_MANAGER",
            user="ADMIN_USER",
            password="Shrikrishna@123" )
        if(conn.is_connected):
            print("Connection Established")
        return conn

def close_connection(conn):
    if(conn.is_connected):
        conn.close
    print("Connection Closed")






#User Login
from DatabaseConnector import *

userValidateQuery = "SELECT USER_ID FROM USER_REGISTRY WHERE USER_NAME=%s AND PASSWORD =%s"
newUserQuery = "INSERT INTO USER_INFORMATION(FIRST_NAME,LAST_NAME,EMAIL_ID,USER_ADDRESS,CONTACT_NUMBER) VALUES(%s,%s,%s,%s,%s)"

def validateUser(username,password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(userValidateQuery,[username,password])
    user_id = cursor.fetchone()
    cursor.close
    if user_id is not None:
        print("Login Successful")
        return user_id
    else:
        print("Invalid Credentials")
        return None

def registerNewUser(firstname,lastname,emailid,address,phonenumber):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(newUserQuery, [firstname,lastname,emailid,address,phonenumber])
    conn.commit()
    userCreated = None
    if(cursor.rowcount > 0):
        print("User Registered Successfully")
        userCreated = True
    else:
        print("Error in Registering User")
        userCreated = False

    return userCreated










#Event Page Load
from DatabaseConnector import *
import itertools

eventTypesQuery = "SELECT EVENT_TYPE, EVENT_TYPE_DESCRIPTION DESCRIPTION, BASE_COST FROM EVENT_TYPES"
eventConfigQuery = 'SELECT EVENT_TYPE_DESCRIPTION DESCRIPTION, BASE_COST FROM EVENT_TYPES WHERE EVENT_TYPE = %s'
eventLocationQuery = "SELECT LOC.LOCATION_TYPE,LOC.LOCATION_NAME,LOC.LOCATION_ADDRESS FROM EVENT_TYPES ET JOIN LOCATIONS LOC ON ET.EVENT_TYPEID = LOC.EVENT_TYPEID WHERE ET.EVENT_TYPE = %s"
eventAddonQuery = "SELECT A.ADDON_TYPE, A.ADDON_SUBTYPE, A.ADDON_DESCRIPTION, A.ADDON_COST FROM ADD_ONS A JOIN EVENT_TYPES ET ON A.EVENT_TYPE = ET.EVENT_TYPEID WHERE ET.EVENT_TYPE = %s"

def loadEventConfig(eventType):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(eventConfigQuery,[eventType])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    event_information = data[0]
    
    cursor.execute(eventAddonQuery,[eventType])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    eventAddons = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    
    cursor.execute(eventLocationQuery,[eventType])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    eventLocations = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    
    cursor.close
    return event_information,eventAddons,eventLocations
    
def displayEventTypes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(eventTypesQuery)
    desc = cursor.description
    column_names = [col[0] for col in desc]
    eventTypesInfo = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    cursor.close
    return eventTypesInfo    
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#Event Registration
from DatabaseConnector import *
import itertools

registerEventQuery = "INSERT INTO EVENT_INFORMATION(USER_ID,EVENT_TYPEID,EVENT_NAME,START_DATE,END_DATE,LOCATION_ID,ATTENDEE_COUNT,ADD_ONS,ESTIMATED_COST,EVENT_DESCRIPTION,EVENT_STATUS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)"
registerEventAddonQuery = "INSERT INTO EVENT_ADDONS_INFORMATION(EVENT_ID,ADDON_ID,ADDON,COUNT,ADDON_COST) VALUES (%s,%s,%s,%s)"

eventDetailsQuery = "SELECT UI.FIRST_NAME,UI.LAST_NAME, EI.EVENT_NAME,EI.STAR1T_DATE,EI.END_DATE,EI.ATTENDEE_COUNT,EI.ESTIMATED_COST,EI.EVENT_DESCRIPTION,EI.ADD_ONS,EI.EVENT_STATUS,EI.REGISTER_TIME,LOC.LOCATION_NAME,LOC.LOCATION_ADDRESS FROM EVENT_INFORMATION  EI JOIN LOCATIONS LOC ON EI.LOCATION_ID = LOC.LOCATION_ID JOIN USER_INFORMATION UI ON EI.USER_ID = UI.USER_ID WHERE EI.EVENT_ID = %s"
eventDAddonDetailsQuery = "SELECT A.ADDON_TYPE , A.ADDON_SUBTYPE, A.ADDON_DESCRIPTION,AI.ADDON_COUNT,AI.ADDON_COST  FROM EVENT_ADDONS_INFORMATION AI JOIN ADD_ONS A ON AI.ADDON_ID = A.ADDON_TYPEID WHERE AI.EVENT_ID = %s"


def registerEvent(USER_ID,EVENT_TYPEID,EVENT_NAME,START_DATE,END_DATE,LOCATION_ID,ATTENDEE_COUNT,ADD_ONS,ESTIMATED_COST,EVENT_DESCRIPTION):
    conn = get_connection()
    cursor = conn.cursor()
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

def registerEventAddons(eventAddons):
     conn = get_connection()
     cursor = conn.cursor()
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

def getEventInformation(event_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(eventDetailsQuery,[event_id])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    event_information = data[0]
    eventAddons = None
    if(event_information['ADD_ONS'] == 1):
        eventAddons = getAddonInformation(event_id)
    cursor.close
    return event_information,eventAddons

def getAddonInformation(event_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(eventDetailsQuery,[event_id])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    eventAddons = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    cursor.close
    return eventAddons
	
	
	
	
	







#Event Management Main
from DatabaseConnector import *
from UserLogin import *
from EventPageLoad import *
import itertools

def displayOptions():
    print('''1-Create New Account
    2-Login
    3-Exit''')

def userHomePage():
    print('''1-Register for an event
    2-Check registered event details
    3-Logout''')    

def getNewUserDetails():
    usercreated=False
    while usercreated==False:
        firstname=input('First Name: ')
        lastname=input('Last Name: ')
        emailid=input('E-Mail: ')
        address=input('Address: ')
        phonenumber=input('Contact: ')
        usercreated=registerNewUser(firstname,lastname,emailid,address,phonenumber)  
        if usercreated == False :
            print("Please Try Again")
    print("Your emailId is your UserId.")
    displayOptions()
    ch=input('Enter your choice: ')
    return ch

def getLoginInfo():
    print('Enter credentials to login')
    username=input('User Name: ')
    password=input('Password: ')
    userid=validateUser(username,password)    
    return userid  

def eventIDForEventType(eventTypesInfo):
    print('_'*120)
    print('Events available are displayed below')
    print('\n')
    print('_'*120)
    for eventType in eventTypesInfo:
        print(eventType) 
    eventType=input('Enter your Event Type: ')
    if eventType=='Birthday':
        EVENT_TYPEID=101
    elif eventType=='Wedding Anniversary':  
        EVENT_TYPEID=102
    elif eventType=='Wedding':  
        EVENT_TYPEID=103
    elif eventType=='Get-together':  
        EVENT_TYPEID=104
    elif eventType=='Alumini-Meet':  
        EVENT_TYPEID=105
    elif eventType=='Stand-up Comedy Show':  
        EVENT_TYPEID=106
    elif eventType=='Musical Concert ':  
        EVENT_TYPEID=107
    elif eventType=='Business Conference':  
        EVENT_TYPEID=108         
    return EVENT_TYPEID

def getEventRegisterDetails():
    eventTypesInfo=displayEventTypes()
    EVENT_TYPEID=eventIDForEventType(eventTypesInfo)
    EVENT_NAME=input('Event Name: ')
    START_DATE=input('Start Date: ')
    END_DATE=input('End Date: ')

    #EVENT_TYPEID,EVENT_NAME,START_DATE,END_DATE,LOCATION_ID,ATTENDEE_COUNT,ADD_ONS,ESTIMATED_COST,EVENT_DESCRIPTION

def userChoice(userid):
    userHomePage()
    userch=input('Enter your Choice: ')
    if userch=='1':
        print('Test') #To be Changed Later


def menu ():
    while True:
        ch=input('Enter your choice: ')
        if ch=='1':
            ch=getNewUserDetails()   
        elif ch=='2':
            userid=getLoginInfo()
        elif ch=='3':
            break
        else:
            print('Invalid Choice. Kindly re-enter.')    
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	