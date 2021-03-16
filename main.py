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
