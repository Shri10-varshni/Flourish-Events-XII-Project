import mysql.connector

global conn
conn=None
#Establishes connection with the SQL Server
def establish_connection():
    global conn
    conn = mysql.connector.connect(
            host="localhost",
            database="EVENT_MANAGER",
            user="ADMIN_USER",
            password="Srikrishna@123" )
    if(conn.is_connected):
        #print("Connection Established")
        print()
    return conn

#Establishes connection if not already established
def get_connection():
    global conn
    if(conn is None):
        conn=establish_connection()
    return conn

#Closes connection with the SQL server
def close_connection(conn):
    if(conn.is_connected):
        conn.close
    print("Connection Closed")


