from EventRegistration import customerMenu
from Reports import manager

#Choice Execution at User Home Page      
global conn
conn = None

def mainChoice():
    print('_'*172)
    print('Flourish Events'.center(172, '_'))
    print('_'*172, '\n')
    print('''1 - Manager
2 - Customer
3 - Close Application''')
    print('_'*172, end='\n\n')

def finalCall():
    while True:
        mainChoice()
        ch=input('Enter choice : ')
        print('\n')
        if ch=='1':
            manager()
        elif ch=='2':
            customerMenu()
        elif ch=='3':
            print('\nThank you for using our services!\n')
            break
        else:
            print('Invalid Choice.')
finalCall()

       

