import os

def binary(dec_num):  
    new_bin=[0,0,0,0,0,0,0,0]
    if (dec_num-128)>=0:
        dec_num-=128
        new_bin[0]="1"
    if (dec_num-64)>=0:
        dec_num-=64
        new_bin[1]="1"
    if (dec_num-32)>=0:
        dec_num-=32
        new_bin[2]="1"
    if (dec_num-16)>=0:
        dec_num-=16
        new_bin[3]="1"
    if (dec_num-8)>=0:
        dec_num-=8
        new_bin[4]="1"
    if (dec_num-4)>=0:
        dec_num-=4
        new_bin[5]="1"
    if (dec_num-2)>=0:
        dec_num-=2
        new_bin[6]="1"
    if (dec_num-1)>=0:
        dec_num-=1
        new_bin[7]="1"
    return (f"{new_bin[0]}{new_bin[1]}{new_bin[2]}{new_bin[3]}{new_bin[4]}{new_bin[5]}{new_bin[6]}{new_bin[7]}")

def decimal(bin_list):     
    return bin_list[0]*128 + bin_list[1]*64 + bin_list[2]*32 + bin_list[3]*16 + bin_list[4]*8 + bin_list[5]*4 + bin_list[6]*2 + bin_list[7]*1

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
    select_option=input("""Hello! I convert Binary & Decimal numbers to their respective counterparts!
1 - Convert from Binary to Decimal
2 - Convert from Decimal to Binary
    
Please select an option above: """)
    try:
        select_option=int(select_option)
    except ValueError:
        print("Invalid input -- Please select either option 1 or option 2\n")
        continue
    if select_option==1:
        while True:
            bin_num=input("Please enter a binary number with 8 digits: ")
            while True:
                try:
                    bin_num=int(bin_num)
                    break
                except ValueError:
                    print("Invalid input -- try entering a binary number\n")
                    continue
            bin_list=[int(i) for i in str(bin_num)]
            if len(bin_list)==8:
                new_dec=decimal(bin_list)
                print(f"{bin_num} in binary is decimal number {new_dec}")
                break
            else:
                print("Invalid input -- Please enter a binary number 8 digits long\n")
                continue
    elif select_option==2:
        while True:
            dec_num=input("Please enter a number between 0 and 255: ")
            try:
                dec_num=int(dec_num)
                break
            except ValueError:
                print("Invalid input -- try entering an integer\n")
        if 0<=dec_num<255:
            new_bin=binary(dec_num)
            print(f"The decimal number {dec_num} is {new_bin} in binary")
        else:
            print("Invalid input -- please enter a number between 0 and 255")
    else:
        print("Invalid input -- Please select either option 1 or option 2\n")
    
    returned_option=run_again()
    
    if returned_option==1:
        os.system('clear')
        continue
    else:
        print("Goodbye...")
        break
    