from DatabaseConnector import get_connection

eventDetailsQuery = "SELECT UI.FIRST_NAME,UI.LAST_NAME, EI.EVENT_NAME,CONVERT(EI.START_DATE,DATE) AS START_DATE,CONVERT(EI.END_DATE,DATE) AS END_DATE,EI.ATTENDEE_COUNT,EI.ESTIMATED_COST,EI.EVENT_DESCRIPTION,EI.ADD_ONS,EI.EVENT_STATUS,EI.REGISTER_TIME,LOC.LOCATION_NAME,LOC.LOCATION_ADDRESS FROM EVENT_INFORMATION  EI JOIN LOCATIONS LOC ON EI.LOCATION_ID = LOC.LOCATION_ID JOIN USER_INFORMATION UI ON EI.USER_ID = UI.USER_ID WHERE EI.EVENT_ID = %s"
eventAddonDetailsQuery = "SELECT A.ADDON_TYPE , A.ADDON_SUBTYPE, A.ADDON_DESCRIPTION,AI.ADDON_COUNT,AI.ADDON_COST  FROM EVENT_ADDONS_INFORMATION AI JOIN ADD_ONS A ON AI.ADDON_ID = A.ADDON_TYPEID WHERE AI.EVENT_ID = %s"
userEventsQuery = "SELECT EVENT_ID, EVENT_NAME,START_DATE,END_DATE FROM EVENT_INFORMATION WHERE USER_ID=%s"
userDetailsQuery = "SELECT FIRST_NAME, LAST_NAME, EMAIL_ID, USER_ADDRESS, CONTACT_NUMBER, EVENT_COUNT FROM USER_INFORMATION WHERE USER_ID = %s"

#Returns event information and event addon information if exists for a given event id 
def getEventInformation(event_id):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(eventDetailsQuery,[event_id])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    event_information = data[0]
    eventAddons = None
    if(event_information['ADD_ONS']>0):
        eventAddons = getAddonInformation(event_id)
    cursor.close
    return event_information,eventAddons

#Returns the Add on information for a particular event for which addon exists
def getAddonInformation(event_id):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(eventAddonDetailsQuery,[event_id])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    eventAddons = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    cursor.close
    return eventAddons

#Returns the very basic details of all the events registered by a particular user_id
def getUserEvents(USER_ID):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(userEventsQuery,[USER_ID])
    userEvents=[]
    if(cursor.rowcount > 0):
        desc = cursor.description
        column_names = [col[0] for col in desc]
        userEvents = [dict(zip(column_names, row))  
            for row in cursor.fetchall()]
    return userEvents   

def getUserInformation(USER_ID):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(userDetailsQuery,[USER_ID])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    user_information = data[0]
    cursor.close
    return user_information