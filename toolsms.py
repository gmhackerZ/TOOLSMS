import os, sys

print "                                                                           "
print "                                                                           "
print "                                                                           "
print "                                                                           "
print "                                                                           "
print "             /$$$$$$$$ /$$$$$$   /$$$$$$  /$$              /$$$$$$  /$$      /$$  /$$$$$$       "
print "             |__  $$__//$$__  $$ /$$__  $$| $$             /$$__  $$| $$$    /$$$ /$$__  $$     "
print "             | $$  | $$  \ $$| $$  \ $$| $$            | $$  \__/| $$$$  /$$$$| $$  \__/        "
print "             | $$  | $$  | $$| $$  | $$| $$             \____  $$| $$  $$$| $$ \____  $$        "
print "             | $$  | $$  | $$| $$  | $$| $$             /$$  \ $$| $$\  $ | $$ /$$  \ $$        "
print "             | $$  | $$  | $$| $$  | $$| $$             /$$  \ $$| $$\  $ | $$ /$$  \ $$        "
print "             | $$  | $$  | $$| $$  | $$| $$             /$$  \ $$| $$\  $ | $$ /$$  \ $$        "
print "             | $$  | $$  | $$| $$  | $$| $$             /$$  \ $$| $$\  $ | $$ /$$  \ $$        "
print "             | $$  |  $$$$$$/|  $$$$$$/| $$$$$$$$      |  $$$$$$/| $$ \/  | $$|  $$$$$$/        "     
print "             |__/   \______/  \______/ |________/       \______/ |__/     |__/ \______/         "
                                                                              
                                                                              
                                                                              

print "                                                                           "
print "                                     tool by : GMHACKERZ                      "
print "                                     group : MALWARE                       "
print "                              "
print "     [01]>[SMSTBOMB]          "
print "                              "
print "     [00]>[EXIT]              "
A = raw_input("MTW==>")
   
if  A == "1" or A == "01":
     print "         [01] sms "
     print "         [00] back to main menu"
 
     SMSTBOMB = raw_input("MTW==> ")

     if SMSTBOMB == "01" or SMSTBOMB == "1":
                        os.system ("clear")
                        os.system ("apt-get install python python2 ")
                        os.system ("git clone https://github.com/TheSpeedX/TBomb")
                        os.system ("mv TBomb /$HOME")
                        os.system ("clear")
                        os.system ("python2 toolsms.py")
     elif A == "00" or A == "0":
                         os.system ("python2 toolsms.py")
     else:
                        print "\nERROR: Wrong Input"
                        os.system ("python2 toolsms.py")

























































































































































































































































