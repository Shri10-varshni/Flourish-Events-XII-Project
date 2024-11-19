import datetime
import re

def date_validity(input_date):                                                       # Checks if a given date is valid (Backend Perspective)
  flag=None
  try:   
    date_split=input_date.split('/')
    date=datetime.datetime(day=int(date_split[2]),month=int(date_split[1]),year=int(date_split[0]))
    if date<datetime.datetime.today():
      flag = 0
    else: 
      flag =  date 
  except: 
    flag = -1
  return flag

def date_validation(input_date):  
  validDate=None                                                           # Makes user enter the date until he enters a valid one (Backend Perspctive)
  while True:    
    date_print=date_validity(input_date)
    if date_print==0:
      print("Date out of range. Kindly Re-enter a valid date.")
      input_date=input('Re-enter Valid Date : ')
    elif date_print==-1:
      print('Date Invalid. Kindly Re-enter a valid date in the format (yyyy/mm/dd)')
      input_date=input('Re-enter Valid Date : ')
    else:
      validDate=date_print
      break
  return validDate


def string_validation(string):
  validstring=''
  if str(string).isalpha():
    validstring=string
  else:
    print('This Data must contain only text. Kindly check your entry and Re-enter a valid text information.')
    string=input('Re-enter Value: ')    
    validstring=string_validation(string)
  return validstring  

def numeric_validation(number):
    validnum=None
    if str(number).isdigit():
        validnum=int(number)
        if validnum<0:
          print('This value must be positive')
          validnum=numeric_validation(number)
    else:    
        print('This Data must contain only Numeric Value. Kindly check your entry and Re-enter a valid Numeric information.')
        number=input('Re-enter Value: ') 
        print('\n')   
        validnum=numeric_validation(number) 
    return validnum       

def email_validation(email):
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  validEmail = ""
  if(re.fullmatch(regex, email)):
      validEmail =  email
  else:
      print("Invalid Email")
      emailid=input('Enter a valid E-mail ID : ')
      validEmail = email_validation(emailid)
  return validEmail
 
def mobileNo_Validation(phno):
  validPhone=''
  try:
    if len(phno)==10 and phno.isdigit():
      validPhone = str(phno)      
    else:
      print('Invalid Mobile Number')
      phno=input('Enter Valid mobile Number consisting of 10 digits : ')
      validPhone=mobileNo_Validation(phno)
  except TypeError:
    print('Invalid Mobile Number')
    phno=input('Enter Valid mobile Number consisting of 10 digits : ')
    validPhone=mobileNo_Validation(phno)
  return validPhone  

def password_validation(password):
  l, u, p, d = 0, 0, 0, 0
  capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  smallalphabets="abcdefghijklmnopqrstuvwxyz"
  specialchar="$@_%"
  digits="0123456789"
  if (len(password) >= 8):
    for i in password:
      # counting lowercase alphabets
      if (i in smallalphabets):
        l+=1           
      # counting uppercase alphabets
      if (i in capitalalphabets):
        u+=1            
      # counting digits
      if (i in digits):
        d+=1           
      # counting the mentioned special characters
      if(i in specialchar):
        p+=1       
  if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
    validpassword=password 
  else:
    print("Please set a strong password to ensure more security. A strong password must contain a least one upper case character, one digit and one special character (with length at least 8).")
    pas=input('Enter 1 to set a new strong password or enter 2 to continue with the same password: ')
    while True:
      if pas=='1':
        password=input('Enter Strong Password: ')
        validpassword=password_validation(password)
        break
      elif pas=='2':
        validpassword=password
        break
      else:   
        pas=input('Invalid Choice. Kindly re-enter: ')  
  return validpassword
      
