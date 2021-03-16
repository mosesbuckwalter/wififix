print('Your computer will restart now, please answer yes or no to continue.')
n = input()
if n == "no":
    print('Your computer will not restart.')
elif n == "yes":
    print('Your computer will now restart.')
    from subprocess import call
    rc = call("./reboot.sh")
elif n != "yes" or "no":
    print('Please try again')
