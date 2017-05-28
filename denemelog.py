import os
import serial
import time
import datetime

repeatTime = 1  # 30data per second
timer = 0
def  writeData(value):
    # Get the current data
    today = datetime.date.today()
    logtime = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    # Open log file 2012-6-23.log and append
    with open(str(today) + '.csv', 'ab') as f:
        #f.write(logtime+','+value)
        f.write(value)
        # Write our integer value to our log
        f.write('\n')
        # Add a newline so we can retrieve the data easily later, could use spaces too.

################################################################################################
def LogTemp():
    # Get the current data
    today = datetime.date.today()
    #os.remove(str(today) + ".csv")
    logtime = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    # Open log file 2012-6-23.log and append
    with open(str(today) + '.csv', 'ab') as f:
        f.write("TIME,IP1,IP2,IP3,IP4,IP5,IP6,IP7,IP8,IP9,IP10,IP11,IP12,IP13,IP14,IP15,IP16,IP17,IP18,IP19,IP20")
        # Write our integer value to our log
        f.write('\n')
        # Add a newline so we can retrieve the data easily later, could use spaces too.
################################################################################################


def Initializing():
    LogTemp()
    timer = time.time()  # Timer to see when we started
    print "Init OK"

#Initializing()

x = 12
today = datetime.date.today()
with open(str(today) + '.csv', 'ab') as f:

    f.write("," + str(x))
    f.write('\n')


# while True:
#     if time.time() - timer > repeatTime: # If the current time is greater than the repeat time, send our 'get' command again
#         writeData(data)
#         timer = time.time()  # start the timer over
