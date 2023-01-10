import os

def capacity():
  return input("What is the capacity of the room? ")

def attendees():
  return input("\nHow many people want to attend the event? ")

def register(room_capacity, event_attendance):
  return room_capacity-event_attendance

def check_again():
  while True:
    check_again=input("\nDo you want to check anymore rooms (y/n)? ")
    try:
      check_again=str(check_again)
    except ValueError:
      print("Invalid input -- try again\n")  
    if check_again=="y" or check_again=="Y":
      return 1
    elif check_again=="n" or check_again=="N":
      return 2
    else:
      print("Invalid input -- try again")
    
while True:
  while True:
    room_capacity=capacity()
    try:
      room_capacity=int(room_capacity)
      break
    except ValueError:
      print("Invalid input -- try again")
  while True:
    event_attendance=attendees()
    try:
      event_attendance=int(event_attendance)
      break
    except ValueError:
      print("Invalid input -- try again")
  check_room=register(room_capacity, event_attendance)
  if check_room<0:
    extra_attendees=event_attendance-room_capacity
    print("%s people have to be told they cannot attend the meeting due to fire regulations" % extra_attendees)
  elif check_room>=0:
    print("The conference can be held. %s more people can attend" % check_room)
  returned_option=check_again()
  if returned_option==1:
    os.system('clear')
    continue
  else:
    print("Goodbye...")
    break