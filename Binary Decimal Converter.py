#ideas for improvement:
#use len() to measure how many binary places so input doesn't have to be 8 long

import os

def binary(dec_num):  
    binary=""
    while dec_num>0:
        remainder = dec_num % 2
        binary = str(remainder)+binary
        dec_num=dec_num//2
    return binary

def decimal(bin_num):     
    decimal = 0
    bin_num=bin_num[::-1]
    for i in range(len(bin_num)):
        decimal+=int(bin_num[1])*(2**i)
    return decimal

def run_again():
  while True:
    check_again=input("\nDo you want to run the program again (y/n)? ")
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
    print("Hello! I convert Binary & Decimal numbers to their respective counterparts!")
    print("1 - Convert from Binary to Decimal")
    print("2 - Convert from Decimal to Binary")
    select_option=input("\nPlease select an option above: ")
    try:
        select_option=int(select_option)
    except ValueError:
        print("Invalid input -- Please select either option 1 or option 2\n")
        continue
    if select_option==1:
        while True:
            bin_num=input("Please enter a binary number: ")
            while True:
                try:
                    bin_num=int(bin_num)
                    break
                except ValueError:
                    print("Invalid input -- try entering a binary number\n")
                    continue
            bin_num=str(bin_num)
            new_dec=decimal(bin_num)
            print(f"{bin_num} in binary is decimal number {new_dec}")
            break
            
    elif select_option==2:
        while True:
            dec_num=input("Please enter a decimal number greater than 0: ")
            try:
                dec_num=int(dec_num)
                break
            except ValueError:
                print("Invalid input -- try entering an integer\n")
        if dec_num>0:
            new_bin=binary(dec_num)
            print(f"The decimal number {dec_num} is {new_bin} in binary")
        else:
            print("Invalid input -- please enter a decimal number greater than 0: ")
    else:
        print("Invalid input -- Please select either option 1 or option 2\n")
    
    returned_option=run_again()
    
    if returned_option==1:
        os.system('clear')
        continue
    else:
        print("Goodbye...")
        break
    