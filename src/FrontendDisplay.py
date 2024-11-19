from UserLogin import registerNewUser
from EventDetails import getEventInformation, getUserInformation 
from Validations import string_validation, numeric_validation, date_validation, email_validation, mobileNo_Validation, password_validation

#Gets details from user and inserts the user details in the table - USER_INFORMATION
def getNewUserDetails():    
    usercreated=False
    while usercreated==False:
        firstname=string_validation(input('First Name: ').strip())
        lastname=string_validation(input('Last Name: ').strip())
        emailid=email_validation(input('E-Mail: ').strip())
        address=input('Address: ').strip()
        phno=input('Contact: ').strip()
        phonenumber=mobileNo_Validation(phno)
        password=password_validation(input('Enter Password: ').strip())
        usercreated=registerNewUser(firstname,lastname,emailid,address,phonenumber,password)  
        if usercreated == False :
            print("Please Try Again")    
    print("Your emailId is your UserId.", end='\n\n')


#Returns particular EVENT_TYPEID for user chosen EVENT_TYPE 
def eventTypeIDForEventType(eventTypesInfo):
    print('Available Events'.center(39))
    print('-'*39)
    EVENT_TYPEID=None
    print('| {:<22} | {:<10} |'.format("EVENT TYPE", "BASE COST"))
    print('-'*39)
    for eventType in eventTypesInfo:    
        print('| {:<22} | {:<10} |'.format(eventType['EVENT_TYPE'], eventType['BASE_COST']))
    print('-'*39, end='\n')   
    eventType=input('Enter your Event Type: ').lower().title().strip()
    if eventType=='Birthday':
        EVENT_TYPEID=101
    elif eventType=='Wedding Anniversary':  
        EVENT_TYPEID=102
    elif eventType=='Wedding':  
        EVENT_TYPEID=103
    elif eventType=='Get-Together':  
        EVENT_TYPEID=104
    elif eventType=='Alumini-Meet':  
        EVENT_TYPEID=105
    elif eventType=='Stand-Up Comedy Show':  
        EVENT_TYPEID=106
    elif eventType=='Musical Concert':  
        EVENT_TYPEID=107
    elif eventType=='Business Conference':  
        EVENT_TYPEID=108   
    else:
        print('Invalid Choice. Kindly Re-enter!')      
        EVENT_TYPEID=eventTypeIDForEventType(eventTypesInfo)
    print('\n\n')
    return EVENT_TYPEID

#Returns All_Add_Ons applied by the User for a particular Event_ID as a list[list]
def addonsForAnEvent(EVENT_ID,eventAddons):
    print('\n')
    print('Add-Ons available for your event are displayed below')
    print('\n\n')
    inviID={}
    I=[]
    decoID={}
    foodID={}
    F=[]
    print('-'*63)
    print('| {:<10} | {:^10} | {:<20} | {:<10} |'.format('AddOn ID', 'Type', 'Sub Type', 'Base Cost'))
    print('-'*63)
    for addon in eventAddons:
        atype='ADDON_TYPE'
        if addon[atype]=='Food':          #Populating all ADDON_TYPEID of food available for event-type 
            foodID[addon['ADDON_TYPEID']]=addon['ADDON_COST']
        elif addon[atype]=='Invitation':  #Populating all ADDON_TYPEID of Invitation available for event-type 
            inviID[addon['ADDON_TYPEID']]=addon['ADDON_COST']
        elif addon[atype]=='Decoration':  #Populating all ADDON_TYPEID of Decoration available for event-type 
            decoID[addon['ADDON_TYPEID']]=addon['ADDON_COST']     
        print('| {:<10} | {:^10} | {:<20} | {:<10} |'.format(addon['ADDON_TYPEID'], addon['ADDON_TYPE'] , addon['ADDON_SUBTYPE'], addon['ADDON_COST']))   
    print('-'*63)    
    print()
    present=input('Do you want to avail addons? Enter yes or No : ').lower().capitalize()
    addons=[]                              #List containing Addons that the user avails for
    if present=='Yes':                                         
        invitation=input('Enter 1 if you want to avail invitaion service: ')
        inviloop=0
        while invitation=='1' and inviloop<=len(inviID):             #InvitaionAddOn         
            ADDON_TYPEID=numeric_validation(input('Enter Invitation ID you want to avail:'))
            if ADDON_TYPEID in inviID.keys():
                ADDON_COUNT=numeric_validation(input('Enter Invitation Count: '))
                ADDON_COST=inviID[ADDON_TYPEID]*ADDON_COUNT
                addons.append([EVENT_ID, ADDON_TYPEID, ADDON_COUNT, ADDON_COST])
                inviloop+=1
                x=inviID.pop(ADDON_TYPEID)
                I.append(ADDON_TYPEID) 
                invitation=input('Enter 1 to avail another invitaion service: ')
                print()
            elif ADDON_TYPEID not in inviID.keys() and ADDON_TYPEID in I:
                print('You can avail one Add-On Service only once for a particular Event.') 
                invitation=input('Enter 1 to avail another invitaion service: ')
            else:
                invitation=input("Invalid ID for Invitation. If you want to Re-enter ID - Enter 1 : ")
        foodloop=0        
        food=input('Enter 1 if you want to avail Food service: ')        
        while food=='1' and foodloop<len(foodID):                   #Food AddOn 
            ADDON_TYPEID=numeric_validation(input('Enter Food ID you want to avail:'))
            if ADDON_TYPEID in foodID.keys():
                ADDON_COUNT=numeric_validation(input('Enter Head Count for Food: '))
                ADDON_COST=foodID[ADDON_TYPEID]*ADDON_COUNT
                addons.append([EVENT_ID, ADDON_TYPEID, ADDON_COUNT, ADDON_COST])
                foodloop+=1
                X=foodID.pop(ADDON_TYPEID)
                F.append(ADDON_TYPEID) 
                food=input('Enter 1 to avail another food service: ')
                print()
            elif ADDON_TYPEID not in foodID.keys() and ADDON_TYPEID in F:
                print('You can avail an Add-On Service only once for a particular Event.') 
                food=input('Enter 1 to avail another food service: ')    
            else:
                food=input("Invalid ID for Food. If you want to Re-enter ID - Enter 1 : ")  

        decoloop=0          
        decoration=input('Enter 1 if you want to avail Decoration service: ')        
        while decoration=='1' and decoloop<1:             #Decoration AddOn 
            ADDON_TYPEID=numeric_validation(input('Enter Decoration ID you want to avail:'))
            if ADDON_TYPEID in decoID.keys():
                ADDON_COST=decoID[ADDON_TYPEID]
                addons.append([EVENT_ID, ADDON_TYPEID, 1 , ADDON_COST])
                decoloop+=1
            else:
                decoration=input("Invalid ID for Decoration. If you want to Re-enter ID - Enter 1 : ")
        print()
        print('_'*172, end='\n\n\n')        
    return addons

#Displays all the applicable locations for the event type and returns the User's choice of LOCATION_ID 
def locationForAnEvent(EVENT_ID,eventLocations):
    print('\n')
    print('Locations available for your event are displayed below')
    print('\n\n') 
    locID=[]   
    print('-'*118)
    print('| {:^20} | {:^20} | {:^20} | {:^45} |'.format('Location ID', 'Type', 'Name', 'Address'))
    print('-'*118, end='\n')
    for location in eventLocations:
        print('| {:^20} | {:^20} | {:^20} | {:^45} |'.format(location['LOCATION_ID'], location['LOCATION_TYPE'], location['LOCATION_NAME'], location['LOCATION_ADDRESS'])) 
        locID.append(location['LOCATION_ID'])
    print('-'*118, end='\n')    
    LOCATION_ID=numeric_validation(input('Enter the location ID for your Event: '))
    print('\n')
    if LOCATION_ID not in locID:
        print('Invalid LOCATION_ID. Kindly Check Once and Re-Enter.')    
        LOCATION_ID=locationForAnEvent(EVENT_ID,eventLocations)
    else:
        print('_'*172,'\n')
    return LOCATION_ID

    
#Displays Estimated Cost for a given Event along with the AddOns applies by the user and returns the estimated cost
def displayEstimatedCost(event_information, ALL_ADD_ONS):
    BASE_COST=event_information['BASE_COST']
    ESTIMATED_COST=BASE_COST
    if len(ALL_ADD_ONS)>0:    
        ADD_ONS_COST=sum(addon[3] for addon in ALL_ADD_ONS)
        ESTIMATED_COST=BASE_COST+ADD_ONS_COST
        print('_'*60,'Estimated Cost Distribution for your event','_'*60, end='\n')
        print('_'*172)
        print('Base Cost                                    :', BASE_COST)
        print('Total Addon Cost                             :', ADD_ONS_COST)
        print('Payable Amount                               :', ESTIMATED_COST)
        print('_'*172, end='\n\n')
    else:
        print('_'*60,'Estimated Cost Distribution for your event','_'*60, end='\n')
        print('_'*172)  
        print('Payable Amount                               :', ESTIMATED_COST)
        print('_'*172, end='\n\n')    
    return ESTIMATED_COST

#Confirms the Registration with the User Once Again
def confirmRegistration():
    flag=None
    confirm=input("Do you want to confirm registration? Enter Yes (or) No : ").lower().capitalize()
    if confirm=='Yes':
        flag=True
    elif confirm=='No':
        flag=False
    else:
        print('Invalid Choice. Kindly Re-enter')
        print('\n')
        flag=confirmRegistration()   
    return flag           

#Displays the Details of the given Event_ID       
def displayEventDetails(EVENT_ID,USER_ID):
    event_information,eventAddons=getEventInformation(EVENT_ID)  
    print('\n\n','_'*172, '\n\n') 
    x=str(event_information['EVENT_NAME'])+' Details' 
    print(x.center(100))
    print('-'*107)
    for detail in event_information:
        print("| {:20} | {:<80} |".format(detail,str(event_information[detail])))
    print('-'*107)
    print('\n\n')    
    if eventAddons!=None:
        print("Applied Addons".center(58))
        print('-'*68)
        print("| {:20} | {:<20} | {:<5} | {:^10} |".format("Type","Sub Type","Count","Cost"))
        print('-'*68)
        for addon in eventAddons:
            print("| {:<20} | {:<20} | {:<5} | {:^10} |".format(addon['ADDON_TYPE'], addon['ADDON_SUBTYPE'], addon['ADDON_COUNT'], addon['ADDON_COST']))
        print('-'*68)
        print('\n\n')
    print('_'*172)       

def displayUserDetails(USER_ID):
    userInformation = getUserInformation(USER_ID)
    print('-'*72)
    print('Your Profile'.center(72))
    print('-'*72)
    print('| {:<15} | {:<50} |'.format("First Name ", userInformation['FIRST_NAME']))
    print('| {:<15} | {:<50} |'.format("Last Name ", userInformation['LAST_NAME']))
    print('| {:<15} | {:<50} |'.format("Email ", userInformation['EMAIL_ID']))
    print('| {:<15} | {:<50} |'.format("Contact Number ", userInformation['CONTACT_NUMBER']))
    print('| {:<15} | {:<50} |'.format("User Address  ", userInformation['USER_ADDRESS']))
    print('| {:<15} | {:<50} |'.format("Event Count ", userInformation['EVENT_COUNT']))
    print('-'*72)
    print('\n\n')