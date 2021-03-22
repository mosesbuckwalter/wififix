import time #used for the sleep function.
import os #used to run os commands
from datetime import datetime
from urllib.request import urlopen

def availablity(): #this function trys to connect to Google, and if it does successfully, then it returns true, otherwise it will return false.
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
        time.sleep(4.0)
    except:
        return False

def wifi(): #this function turns off and on the wifi again and prints status messages.
    print('Your computer will now turn the WiFi off and on again.')
    cmd = 'nmcli radio wifi off' #turn off WiFi
    os.system(cmd)
    time.sleep(2.0)
    cmd = 'nmcli radio wifi on' #turn on WiFi
    os.system(cmd)
    time.sleep(10.0)
    print('WiFi successfully turned off and on') #indication of it working

def reboot(): #this program restarts your computer when WiFi is detected to be not connected, and takes a yes or no input from the user.
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

def confirm(): #this function takes user input and requires a yes or no response and will loop until it receives such.
    global n
    n = 0
    while n != "no" or "yes":
        n = input()
        if n == "yes":
            break
        elif n == "no":
            exit()
        print('Please try again')

def guiconfirm():
    if gui == 0:
        exit()
    elif gui == 2:
        n = 'yes'

def GUI(): #this function starts an xmessage gui with 2 buttons
    global gui
    cmd = 'xmessage "This program will turn off and on your WiFi when it detects poor signal. Are you okay with this?" -buttons Yes:2,No:0'
    gui = os.system(cmd) >> 8

log = []
now = str(datetime.now())
connected = ('The WiFi was connected on, ' + now)
disconnected = ('The WiFi was not connected on, ' + now)

GUI()
guiconfirm()

print('This program will turn off and on your WiFi when it detects poor signal. Are you okay with this? Answer "yes" or "no".') #stating what the program will do when ran.
confirm() #confirms that the user would like to do this.

while n == "yes":
    if availablity() == False: #checks if WiFi connected is false.
        log.append(disconnected) #adds not connected time to log.
        wifi() #if the WiFi connected is false, it will restart the WiFi.
        log.append(connected) #adds connected time to log.
        print(log) #prints the log.
        availablity()
    else:
        availablity()
