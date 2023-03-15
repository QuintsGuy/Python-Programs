# Tristan Knott
# Week 2 Lab 2A
#
# Variables Used:
# file              stores csv file from input into function
# rooms             stores organized list of values pulled from csv file
# room_counter      counts the number of rooms which have an overage
# room_name         stores name of room
# max_attendance    stores maximum attendance value of room
# cur_attendance    stores current attendance value
# result            stores returned value from check_room function
# room_overage      stores number of people over the room limit
# csv_file          stores inputed csv path
#
# =======================================================
import csv

def check_room(max_attendance, cur_attendance):
    if cur_attendance < max_attendance:
        return 1
    else:
        return cur_attendance - max_attendance

def get_list(csv_file):
    with open(csv_file) as f:
        file = csv.reader(f)
        rooms = list(file)
        room_counter=0
        print('{:<20}{:>10}{:>10}{:>10}'.format('Room', 'Max', 'Min', 'Over\n'))
        for row in rooms:
            room_name = row[0]
            max_attendance = int(row[1])
            cur_attendance = int(row[2])
            result=check_room(max_attendance, cur_attendance)
            if result == 1:
                continue
            else:
                room_overage = result
            room_counter+=1
            print('{:<20}{:>10}{:>10}{:>10}'.format(room_name, max_attendance, cur_attendance, room_overage))

        print('\nProcessed %s records' % len(rooms))
        print('There are %s rooms over the limit' % room_counter)
            
csv_file = str(input(r"Please enter a file path: "))
get_list(csv_file)