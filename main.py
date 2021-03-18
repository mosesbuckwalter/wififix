from urllib.request import urlopen
def availablity():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
        time.sleep(5.0)
    except:
        return False
def wifi():
    print('Your computer will now turn the WiFi off and on again.')
    cmd = 'nmcli radio wifi off' #turn off WiFi
    os.system(cmd)
    time.sleep(5.0)
    cmd = 'nmcli radio wifi on'
    os.system(cmd)
    time.sleep(20.0)
    print('WiFi successfully turned off and on')
def reboot():
    print('Your computer will restart now, please answer yes or no to continue.')
    n = 0
    while n != "yes" or "no":
        n = input()
        if n == "no":
            print('Your computer will not restart.')
            exit()
        elif n == "yes":
            print('Your computer will now restart.')
            cmd = 'sudo reboot'
            os.system(cmd)
        print('Please try again')
import time
import os
print('This program will turn off and on your WiFi when it detects poor signal. Are you okay with this? Answer "yes" or "no".')
n = 0
while n != "no" or "yes":
    n = input()
    if n == "yes":
        x = 1
        break
    elif n == "no":
        exit
    print('Please try again')
while x == 1:
    if availablity() == False:
        wifi()
