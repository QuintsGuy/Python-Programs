import csv

class Voter:
    all = []
    def __init__(self, firstName, lastName, age):
        assert age >= 18, f""

        self.firstName = firstName
        self.lastName = lastName
        self.age = age

        Voter.all.append(self)

    def instantiate_from_csv():
        with open (r"C:\Users\knott\OneDrive\Documents\GitHub\Python-Programs\Voted Registration from CSV\example.csv") as csvfile:
            file=csv.reader(csvfile)
            print("First Name \t Last Name \t Age")
            for row in file:
                firstName=row[0]
                lastName=row[1]
                age=int(row[2])
                print(firstName, "\t\t", lastName, "\t\t", age)
                
Voter.instantiate_from_csv()

print("\n")
print("Processing has finished.")