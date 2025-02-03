#FutureTime.py
#Name: Megann Wegner
#Date: 1/28/2025
#Assignment: Lab 2 - Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  #TODO:
  #Ask user for hours
  hours = input("How many hours? ")
  hours = int(hours) # change from text to numbers

  #Ask user for minutes
  minutes = input("How many minutes? ")
  minutes = int(minutes)
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.
  futureMinute = currentMinute + minutes
  futureHour = currentHour + hours + (futureMinute // 60)
 
# make sure not to forget additional hours from minutes
  futureMinute = futureMinute % 60
  futureHour = futureHour % 24

  futureHour1 = futureHour // 10
  futureHour2 = futureHour % 10
  futureMinute1 = futureMinute // 10
  futureMinute2 = futureMinute % 10

  print("Future Time: " + str(futureHour1) + str(futureHour2) + ":" + str(futureMinute1) + str(futureMinute2))
  #Output the future time in standard format "HH:MM" my single digits dont have a zero in front

if __name__ == '__main__':
  main()