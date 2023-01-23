# Tristan Knott
# Week 2 Lab 2B
#
# Variables Used:
# file              stores csv file from input into function
# report            stores organized list of values pulled from csv file
# computer_type     stores type of computer
# computer_brand    stores brand of computer
# cpu_type          stores type of cpu
# amount_ram        stores the amount of ram
# disk1             stores size of hdd1
# num_hdd           stores number of hdd 
# disk2             stores size of hdd2
# operating_system  stores type of operating system
# man_year          stores manufactured year
# csv_file          stores inputed csv_file to be used in function
#
# =======================================================
import csv

def get_file(csv_file):
    with open(csv_file) as f:
        file = csv.reader(f)
        report = list(file)
        print('{:<10}{:<10}{:<5}{:<5}{:<10}{:<10}{:<10}{:<5}{:<5}'.format('Type', 'Brand', 'CPU', 'RAM', '1st Disk', 'No HDD', '2nd Disk', 'OS', 'YR'))
        for row in report:
            computer_type = row[0]
            computer_brand = row[1]
            cpu_type = row[2]
            amount_ram = row[3]
            disk1 = row[4]
            num_hdd = row[5]
            if num_hdd == "1":
                disk2 = row[8]
                operating_system = row[6]
                man_year = row[7]
            else:
                disk2 = row[6]
                operating_system = row[7]
                man_year = row[8]
            if computer_type == 'D':
                computer_type = 'Desktop'
            elif computer_type == 'L':
                computer_type = 'Laptop'
            if computer_brand == 'DL':
                computer_brand = 'Dell'
            elif computer_brand == 'GW':
                computer_brand = 'Gateway'
            print('{:<10}{:<10}{:<5}{:<5}{:<10}{:^10}{:<10}{:^5}{:^5}'.format(computer_type, computer_brand, cpu_type, amount_ram, disk1, num_hdd, disk2, operating_system, man_year))

csv_file = str(input(r"Please enter a file path: "))
get_file(csv_file)