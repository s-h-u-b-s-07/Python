import re

username = input("Enter username:")
usr = "Hello " + username + ",How are you?" .format(username)

match = re.match('^[A-Z]{1}[a-z]{2,}$',username)

if match :
    print(usr)
else :
    print('Invalid User Name')
