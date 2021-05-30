import os
import time


#Send message to telegram
def sendmessage(msg):
    cmd = 'mosquitto_pub -t test/1 -m '
    command = cmd + '"' + msg + '"'
    os.system(command)


#Detect If there are changes in the selected file
def detectchange(file):
    s_time = os.path.getmtime(file)
    while True:
        c_time = os.path.getmtime(file)
        if(c_time != s_time):
            print("File has changed")
            sendmessage('file: ' + file + ' has changed')
            s_time = c_time
        time.sleep(5)

#Main
detectchange('file.txt')
