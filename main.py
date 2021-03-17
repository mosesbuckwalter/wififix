print('How would you like to handle poor connection? Say "reboot" if you would like to restart your computer if internet connection is bad. Say "reset" if you would like the WiFi connection to be turned off and on when the connection is poor.')
n = 0
while n != "reboot" or "reset":
    n = input()
    print('Please try again')
    if n == "reboot":
        x = 1
        break
    elif n == "reset":
        x = 2
        break
if x == 1:
    #detect if connection is poor
    print('Your computer will restart now, please answer yes or no to continue.')
    n = 0
    while n != "yes" or "no":
        n = input()
        print('Please try again')
        if n == "no":
            print('Your computer will not restart.')
            exit()
        elif n == "yes":
            print('Your computer will now restart.')
            from subprocess import call
            rc = call("./reboot.sh")
elif x == 2:
    #detect if connection is poor
    print()
