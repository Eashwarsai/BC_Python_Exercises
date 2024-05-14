valid_username="Eashwarsai"
valid_password="1234"
username=str(input('Enter Username : '))
password= str(input('Enter password: '))

if username==valid_username and password==valid_password :
    print('Welcome '+username+'!')
else:
    print('Invalid credentials! Try Again!')