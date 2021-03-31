import datetime
now= datetime.datetime.now()
print(now.strftime("%Y-%d-%m"))
print(now.strftime("%H %M: %S"))

name = input ("What's your name\n")
allowedUsers = ['Seyi', 'Makinde', 'Matthew']
allowedPassword = ['password','password', 'password']

if (name in allowedUsers):
    Password= input ("What's your password \n")
    userId = allowedUsers.index(name)

    if (Password == allowedPassword[userId]):

        print(f'Welcome home {name}')
        print('These are the available options: ')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedoption = int(input('Please select an option: '))
        deposit = 250
        deposit1 = deposit + int(input() )

        if (selectedoption == 1):
             withdrawal= int(input ('How much would you like to withdraw \n'))
             print('Take your cash')

        elif (selectedoption == 2):
             deposit= int(input ('How much would you like to deposit \n'))
             print(f'Current balance is {deposit1}')

        else:
             complaint= (input ('What issue will you like to report \n'))

             print('Thank you for contactacting us')
    else:
        print("Password incorrect, try again")
else:
    print("Invalid name")
