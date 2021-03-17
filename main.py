print('How would you like to handle poor connection? Say "reboot" if you would like to restart your computer if internet connection is bad. Say "reset" if you would like the WiFi connection to be turned off and on when the connection is poor.')
n = 0
while n != "reboot" or "reset":
    n = input()
    if n == "reboot":
        x = 1
        break
    elif n == "reset":
        x = 2
        break
    print('Please try again')
if x == 1:
    #forever if connection is detected to be poor
    #detect if connection is poor
    print('Your computer will restart now, please answer yes or no to continue.')
    n = 0
    while n != "yes" or "no":
        n = input()
        if n == "no":
            print('Your computer will not restart.')
            exit()
        elif n == "yes":
            print('Your computer will now restart.')
            from subprocess import call
            rc = call("./reboot.sh")
        print('Please try again')
elif x == 2:
    #forever if connection is detected to be poor
    #detect if connection is poor
    print()
