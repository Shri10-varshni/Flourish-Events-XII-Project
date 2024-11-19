from DatabaseConnector import get_connection

userValidateQuery = "SELECT USER_ID FROM USER_REGISTRY WHERE USER_NAME=%s AND PASSWORD =%s"
newUserQuery = "INSERT INTO USER_INFORMATION(FIRST_NAME,LAST_NAME,EMAIL_ID,USER_ADDRESS,CONTACT_NUMBER) VALUES(%s,%s,%s,%s,%s)"
fetchUserIDQuery="SELECT USER_ID FROM USER_INFORMATION WHERE EMAIL_ID=%s"
userRegistryQuery="INSERT INTO USER_REGISTRY(USER_ID, USER_NAME, PASSWORD) VALUES(%s,%s,%s)"

#Validates the username and password entered by the user with the data in the table USER_REGISTRY
def validateUser(username,password):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(userValidateQuery,[username,password])
    user_id = cursor.fetchone()
    cursor.close
    if user_id is not None:
        user_id = int(user_id[0])
        print("Login Successful")
        print('_'*172, end='\n\n')
        return user_id
    else:
        print("Invalid Credentials")
        return None

#Registers the details of a new user in USER_INFORMATION and USER_REGISTRY table
def registerNewUser(firstname,lastname,emailid,address,phonenumber, password):
    conn = get_connection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(newUserQuery, [firstname,lastname,emailid,address,phonenumber])
    conn.commit()
    userCreated = None
    if(cursor.rowcount > 0):
        cursor.execute(fetchUserIDQuery, [emailid])
        userID=cursor.fetchone()[0]
        cursor.execute(userRegistryQuery, [userID, emailid, password])
        conn.commit()
        print("User Registered Successfully")
        userCreated = True    
    else:
        print("Error in Registering User")
        userCreated = False
    return userCreated



        
