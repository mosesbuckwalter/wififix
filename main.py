from urllib.request import urlopen
def availablity():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
        time.sleep(5.0)
    except:
        return False
print('How would you like to handle poor connection? Say "reboot" if you would like to restart your computer if internet connection is bad. Say "reset" if you would like the WiFi connection to be turned off and on when the connection is poor.')
   def fixwifi():        
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
import time
if x == 1:
    while x == 1:
        if availablity() == False:
            print('Your computer will restart now, please answer yes or no to continue.')
            n = 0
            while n != "yes" or "no":
                n = input()
                if n == "no":
                    print('Your computer will not restart.')
                    exit()
                elif n == "yes":
                    print('Your computer will now restart.')
                    import os
                    cmd = 'sudo reboot'
                    os.system(cmd)
                print('Please try again')
elif x == 2:
    while x == 2:
        if availablity() == False:
            print('Your computer will now turn the WiFi off and on again.')
            import os
            cmd = 'nmcli radio wifi off' #turn off WiFi
            os.system(cmd)
            time.sleep(5.0)
            cmd = 'nmcli radio wifi on'
            os.system(cmd)
            time.sleep(20.0)
            print('WiFi successfully turned off and on')
