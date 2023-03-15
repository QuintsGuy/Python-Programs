import csv

numberVoted=0
notEligibleToVote=0
oldEnoughNotReg=0
eligibleToVoteNoVote=0
numberVoted=0
numRecords=0

with open("C:\Intermediate Python Class\example.csv") as csvfile:
    file=csv.reader(csvfile)
    for row in file:
        id=row[8]
        age=int(row[1])
        registered=row[2]
        voted=row[3]

        if age<18:
            notEligibleToVote+=1

        if age>=18 and
            oldEnoughNotReg
        
        if registered

        if voted == "Y"
            numberVoted+=1

        numRecords