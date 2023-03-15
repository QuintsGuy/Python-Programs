# Work on this later

import csv

class Room:
    all = []
    def __init__(self, room_name, max_people, currently_registered):
        assert max_people > 0
        assert currently_registered >= 0

        self.roomName = room_name
        self.max_people = max_people
        self.currently_registered = currently_registered

        Room.all.append(self)

    def instantiate_from_csv():
        with open(r"C:\Users\knott\OneDrive\Documents\GitHub\Python-Programs\Event Attendance\Roomlist.csv") as f:
            file = csv.reader(f)
            rooms = list(file)
            print(rooms)

