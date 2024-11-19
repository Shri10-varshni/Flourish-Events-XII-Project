import mysql.connector
import config # For credentials

global conn
conn=None
#Establishes connection with the SQL Server
def establish_connection():
    global conn
    conn = mysql.connector.connect(
            host=config.DB_HOST,
            database=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD)
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


