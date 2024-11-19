from DatabaseConnector import get_connection

eventTypesQuery = "SELECT EVENT_TYPE, EVENT_TYPE_DESCRIPTION DESCRIPTION, BASE_COST FROM EVENT_TYPES"
eventConfigQuery = 'SELECT EVENT_TYPE_DESCRIPTION DESCRIPTION, BASE_COST FROM EVENT_TYPES WHERE EVENT_TYPEID = %s'
eventLocationQuery = "SELECT LOCATION_ID, LOCATION_TYPE, LOCATION_NAME, LOCATION_ADDRESS FROM LOCATIONS WHERE EVENT_TYPEID = %s"
eventAddonQuery = "SELECT ADDON_TYPEID, ADDON_TYPE, ADDON_SUBTYPE, ADDON_DESCRIPTION, ADDON_COST FROM ADD_ONS WHERE EVENT_TYPEID = %s"

#Returns the Event_Type details (event_information); AddOns available for Event_Type, Locations applicable for Event_Types
def loadEventConfig(eventTypeID):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(eventConfigQuery,[eventTypeID])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cursor.fetchall()] 
    event_information = data[0]
    
    cursor.execute(eventAddonQuery,[eventTypeID])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    eventAddons = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    
    cursor.execute(eventLocationQuery,[eventTypeID])
    desc = cursor.description
    column_names = [col[0] for col in desc]
    eventLocations = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    
    cursor.close
    return event_information,eventAddons,eventLocations

#Returns all the available Event_Types as a list[Dict]    
def displayEventTypes():
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(eventTypesQuery)
    desc = cursor.description
    column_names = [col[0] for col in desc]
    eventTypesInfo = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    cursor.close
    return eventTypesInfo    


    

    