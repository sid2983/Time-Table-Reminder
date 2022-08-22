#Importing all modules
import time
import pyttsx3 #For text-to-audio recognition
from re import X
import pandas as pd #For importing csv data
from time import sleep #Halt the execution of program for n seconds
from notifypy import Notify #To get notification
from datetime import datetime #For current time

start = time.time()
#Creating object of notify class
notification = Notify()
# notification.title = "Remainder"

#For Text-to-audio
engine = pyttsx3.init() #Intialisation

def speak(message): #To speak the message via audio (text spoke by os)
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('rate',rate-50)
    engine.say(message)
    engine.runAndWait()

# Current location of file
location = "time_table.csv"



# Read data from location and Fetching data from csv file
table = pd.read_csv(location)

#Formatting time
timing = table['Time']
work = table['Work']

# Getting current time
def get_current_time():
    current_time = datetime.now().strftime("%H:%M")

    hours,minutes = current_time.split(":")
    hours,minutes = int(hours), int(minutes)

    return hours,minutes

# hours,minutes = get_current_time()
def csv_final_timing(timing): # timing --> Time column in csv
    final_timing = {}
    index_for_work = 0
    for i in timing:
        x = i[:5]#timing in strings
        x = x.split(":")
        Hr = int(x[0])
        Min = int(x[1])
        final_timing[work[index_for_work]] = [Hr,Min]
        index_for_work+=1
    return final_timing

final_timing = csv_final_timing(timing)
# print(final_timing)

# print(type(hours), type(minutes)) --> checking type of hours and minutes
# print(hours,minutes)

def What_Work():
    for keys in final_timing:
        if (final_timing[keys][0]==hours and final_timing[keys][1]==minutes):
            current_time = datetime.now().strftime("%H:%M")
            salutation = ""
            if ((hours>12 and minutes>1) and (hours<16 and minutes<59)):
                salutation = "Good Afternoon Sir,\n"
            elif ((hours>=16 and hours<20)):
                salutation = "Good Evening Sir,\n"
            elif ((hours<12 and minutes<59)):
                salutation = "Good Morning Sir,\n"
            else:
                salutation = "Good Night Sir,\n"
            # print(f"You have to {keys} and {current_time}")
            end = time.time()
            current_process_time = end-start
            message = f"Now You have to do {keys} at {current_time}"
            notification.message = salutation+message+f"\nTotal time taken : {current_process_time} seconds"
            notification.send() # Sending notification message
            print(message)
            speak(message)
            # print(end-start)
            return 1
    return 0

print("----Please select one of these options----\n")
print("1. Add a reminder to ur list")
print("2. Initiate the reminder ")

quest = int(input())
if quest==1:
    # entering new time and work for reminder
    time = input("Input the new reminder time in HH:MM format:\n")
    task = input("Input the task u wanna get reminder for:\n")
    with open("time_table.csv","a+") as cf:
        cf.write("\n"+time+","+task)
elif quest==2:
    count=0
    while True:
        hours,minutes = get_current_time()
        is_called = What_Work()
        # this piece of code will run the reminder two times at an interval of 30 seconds and then abort the execution.
        if (is_called):
            if count==1:
                exit()
            else:
                count+=1
                sleep(30)
                
            
            
            
            
            
            




# hours,minutes = get_current_time()
# is_called = What_Work()
# if (is_called):
#     sleep(60)