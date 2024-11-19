from DatabaseConnector import get_connection

countEachMonth="select monthname(start_date) as Month, count(*) as Nummber_Of_Registered_Events from event_information WHERE YEAR(start_date) = %s group by monthname(start_date) order by month(start_date)"
countRegisteredEventTypeMonth="select et.event_type Event_Type,count(1) Register_count from event_information ei, event_types et where month(start_date) = %s and et.event_typeid = ei.event_typeid group by event_type,monthname(start_date) order by count(1) desc"
cancelationsReportQuery=""

#Prints the Number of registered events in each month month-wise
def monthwiseTotalCount(countEachMonth, year):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(countEachMonth, (year,))
    conn.commit()
    data=cursor.fetchall()
    print()
    print('-'*37)
    print('| {:<10} | {:<20} |'.format("Month", "Events Registered"))
    print('-'*37)
    for i in data:
        print('| {:<10} | {:^20} |'.format(i[0], i[1]))
    print('-'*37, end='\n')    

#Prints how many events were registered in each Registered Event Type in a given month
def registeredEventTypeMonth(countRegisteredEventTypeMonth, month):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(countRegisteredEventTypeMonth, (month,))
    conn.commit()
    data=cursor.fetchall()
    print()
    print('-'*37)
    print('| {:<23} | {:<7} |'.format("Event Types Registered", "Count"))
    print('-'*37)
    for i in data:
        print('| {:<23} | {:^7} |'.format(i[0], i[1]))
    print('-'*37, end='\n')  

def cancellationsReport(cancelationsReportQuery, year):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(cancelationsReportQuery, (year,))
    conn.commit()
    data=cursor.fetchall()
    print()
    print('-'*37)
    print('| {:<10} | {:<20} |'.format("Month", "Canelations Count"))
    print('-'*37)
    for i in data:
        print('| {:<10} | {:^20} |'.format(i[0], i[1]))
    print('-'*37, end='\n')  


def managerChoices():
    print('_'*172, end='\n')
    print('''1 - Report of number of registered events in each month in a particular year
2 - Report of number of each registered event in a particular month
3 - Back to Main Page''')
    print('_'*172)

def manager():
    while True:
        managerChoices()
        print('\n')
        managerch=input('Enter your choice : ')
        if managerch=='1':
            year=input('Enter Year to view report : ')
            monthwiseTotalCount(countEachMonth, year)
        elif managerch=='2':
            month=input('Enter Month Number to view report : ')
            if (month in ['1','2','3','4','5','6','7','8','9','10','11','12']) :
                registeredEventTypeMonth(countRegisteredEventTypeMonth, month)
            else:    
                print('Invalid Choice. Make sure you enter a valid Month Number')
        elif managerch=='3':
            break
        else:
            print('Invalid Choice.')
            print()



