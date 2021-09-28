import os
import xlwt
import xlrd
import random
import datetime
import pandas as pd
from collections import Counter


def path():
    # Creates an initial .txt file on the user's desktop.

    global f, username, dups
    username = os.getlogin()
    f = f'C:/Users/{username}/Desktop/lottomat.txt'


class giveMeMyMoney():

    def __init__(self):
        self.user = user
        self.now = now
        self.num = num
        self.f = f
        self.l = l
        self.p = p
        self.dups = dups
        self.yes = yes

    def getInput():
        # The user choose a number between 1-14.
        # Any wrong input will prompt an error message and return
        # to the question.
        # Function then returns the user's input.

        while True:
            try:
                user = int(input("[?]How many lines? "))
            except ValueError:
                print("[!]Numbers Only!")
                continue

            if user > 14:
                print("[!]Max 14!")
                continue
            elif user == 0:
                quit()

            else:
                return user

    def aboveNineInput():
        while True:

            try:
                yes = str(input("Do you want only numbers above 9? [Y/n] "))
            except ValueError:
                print("[!]Type Y/n or N/n")
                continue

            if yes == "Y" or yes == "y" or yes == "N" or yes == "n":
                return yes
            else:
                print("[!]Wrong input! try again... ")
                continue

    def aboveNineGo(user):
        # Start process of writing to file with the current date.
        # Write 6 random numbers between 10-37 then adds to list.
        # Write 1 random strong number between 1-7 then adds to strong list.
        # Then calculates the duplicated numbers in the results and writes them to the file.

        now = datetime.datetime.now()
        num = 0
        num2 = []
        num2_appearance = []
        dups = []
        strong_dups = []
        rows = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                'K': 11, 'L': 12, 'M': 13, 'N': 14,
                }
        row_num = 0
        while True:
            try:
                clear = str(input("[?]Clear File? [Y/n]"))
            except ValueError:
                print("[!]Wrong input! Try again. ")
                continue

            if clear == "Y" or clear == "y":
                with open(f, 'a') as file:
                    # Clear file
                    file.truncate(0)

                    # Write the current date to file.
                    file.write(f'{now.strftime("[Date] %d.%m.%y")}\n\n')
                    file.write(f'===============================\n')

                    while num < user:
                        rand = random.sample(range(10, 37), 6)
                        rand.sort()
                        s = random.sample(range(1, 8), 1)

                        for x, y in rows.items():
                            if y == num + 1:
                                row_num = x

                        dups.append(rand)
                        #strong_dups.append(s)
                        file.write(f'{row_num},{rand},{s} \n')
                        print(f'{row_num},{rand},{s} \n')
                        num += 1

                    # Get duplicated values and write to file + print to screen.
                    dup_counter = Counter((n for a in dups for n in a))
                    duptofile = ({num: count for num, count in dup_counter.items() if count > 1})
                    #file.write(f'===============================\nDuplicated Numbers:\n\r{duptofile}')
                    file.write('===============================\nDuplicated Numbers:\n')
                    #print(f'Duplicated Numbers:\n{duptofile}')
                    for x,y in duptofile.items():
                        num2.append(x)
                        num2_appearance.append(y)
                        print(f'Number: {x} appears {y} times.')
                        file.write(f'\nNumber: {x} appears {y} times.')
                    file.write('\n###############################\n\n')
                    file.close()
                    break

            elif clear == "N" or clear == "n":
                with open(f, 'a') as file:
                    file.write(f'{now.strftime("[Date] %d.%m.%y")}\n\n')
                    file.write(f'===============================\n')

                    while num < user:
                        rand = random.sample(range(10, 37), 6)
                        rand.sort()
                        s = random.sample(range(1, 8), 1)

                        for x, y in rows.items():
                            if y == num + 1:
                                row_num = x

                        dups.append(rand)
                        #strong_dups.append(s)
                        file.write(f'{row_num},{rand},{s} \n')
                        print(f'{row_num},{rand},{s} \n')
                        num += 1

                    # Get duplicated values and write to file + print to screen.
                    dup_counter = Counter((n for a in dups for n in a))
                    duptofile = ({num: count for num, count in dup_counter.items() if count > 1})
                    # file.write(f'===============================\nDuplicated Numbers:\n\r{duptofile}')
                    file.write('===============================\nDuplicated Numbers:\n')
                    #print(f'Duplicated Numbers:\n{duptofile}')
                    for x,y in duptofile.items():
                        num2.append(x)
                        num2_appearance.append(y)
                        print(f'Number: {x} appears {y} times.')
                        file.write(f'\nNumber: {x} appears {y} times.')
                    file.write('\n###############################\n\n')
                    file.close()
                    break
            else:
                print("Wrong clear input! type Y/y or N/n.")
                continue

    def go(user):
        # Start process of writing to file with the current date.
        # Write 6 random numbers between 1-37 then adds to list.
        # Write 1 random strong number between 1-7 then adds to strong list.
        # Then calculates the duplicated numbers in the results and writes them to the file.

        now = datetime.datetime.now()
        num = 0
        num2 = []
        num2_appearance = []
        dups = []
        strong_dups = []
        rows = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                'K': 11, 'L': 12, 'M': 13, 'N': 14,
                }
        row_num = 0

        while True:
            try:
                clear = str(input("[?]Clear File? [Y/n]"))
            except ValueError:
                print("[!]Wrong input! Try again. ")
                continue

            if clear == "Y" or clear == "y":
                with open(f, 'a') as file:
                    file.truncate(0)
                    file.write(f'{now.strftime("[Date] %d.%m.%y")}\n\n')
                    file.write(f'===============================\n')

                    while num < user:
                        rand = random.sample(range(10, 37), 6)
                        rand.sort()
                        s = random.sample(range(1, 8), 1)

                        for x, y in rows.items():
                            if y == num + 1:
                                row_num = x

                        dups.append(rand)
                        #strong_dups.append(s)
                        file.write(f'{row_num},{rand},{s} \n')
                        print(f'{row_num},{rand},{s} \n')
                        num += 1

                    # Get duplicated values and write to file + print to screen.
                    dup_counter = Counter((n for a in dups for n in a))
                    duptofile = ({num: count for num, count in dup_counter.items() if count > 1})
                    # file.write(f'===============================\nDuplicated Numbers:\n\r{duptofile}')
                    file.write('===============================\nDuplicated Numbers:\n')
                    #print(f'Duplicated Numbers:\n{duptofile}')
                    for x,y in duptofile.items():
                        num2.append(x)
                        num2_appearance.append(y)
                        print(f'Number: {x} appears {y} times.')
                        file.write(f'\nNumber: {x} appears {y} times.')
                    file.write('\n###############################\n\n')
                    file.close()
                    break

            elif clear == "N" or clear == "n":
                with open(f, 'a') as file:
                    file.write(f'{now.strftime("[Date] %d.%m.%y")}\n\n')
                    file.write(f'===============================\n')

                    while num < user:
                        rand = random.sample(range(10, 37), 6)
                        rand.sort()
                        s = random.sample(range(1, 8), 1)

                        for x, y in rows.items():
                            if y == num + 1:
                                row_num = x

                        dups.append(rand)
                        #strong_dups.append(s)
                        file.write(f'{row_num},{rand},{s} \n')
                        print(f'{row_num},{rand},{s} \n')
                        num += 1

                    # Get duplicated values and write to file + print to screen.
                    dup_counter = Counter((n for a in dups for n in a))
                    duptofile = ({num: count for num, count in dup_counter.items() if count > 1})
                    # file.write(f'===============================\nDuplicated Numbers:\n\r{duptofile}')
                    file.write('===============================\nDuplicated Numbers:\n')
                    #print(f'Duplicated Numbers:\n{duptofile}')
                    for x,y in duptofile.items():
                        num2.append(x)
                        num2_appearance.append(y)
                        print(f'Number: {x} appears {y} times.')
                        file.write(f'\nNumber: {x} appears {y} times.')
                    file.write('\n###############################\n\n')
                    file.close()
                    break
            else:
                print("Wrong clear input! type Y/y or N/n.")
                continue


def convert():
    # Function to convert the txt file to .xls for use with Excel
    # With input validation

    while True:
        try:
            ask = input(str("[?]Would you like to convert to csv? [Y/n] "))
        except ValueError:
            print("[!]Please select Y/y or N/n")
            continue

        if ask == 'Y' or ask == 'y':
            # Convert file to .xls
            read_file = pd.read_csv(rf'C:/Users/{username}/Desktop/lottomat.txt', sep='\t')
            read_file.to_excel(rf'C:/Users/{username}/Desktop/lottomat.xls', 'Sheet 1')
            print("[!]All Done! :)")
            print(f'[!]File {f} has been converted!')
            break

        elif ask == 'N' or ask == 'n':
            print("[V]All Done!")
            break

        else:
            print("[!]Please select Y/y or N/n")
            continue


def tryAgain():
    # Function to get user input to restart the script
    # With input validation.

    while True:
        try:
            run = input(str("[?]Try Again? [Y/n] "))
        except ValueError:
            print("[!]Type Y/n or N/n")
            continue

        if run == "y" or run == "Y":
            main()
            break

        elif run == "n" or run == "N":
            run = False
            break

        else:
            print("[!]Type Y/n or N/n ")
            continue

    return run


def main():
    # Main function.
    # Starts with asking for number of lines.

    path()

    while True:
        user = giveMeMyMoney.getInput()
        yes = giveMeMyMoney.aboveNineInput()

        if yes == "y" or yes == "Y":
            giveMeMyMoney.aboveNineGo(user)
            break
        elif yes == "n" or yes == "N":
            giveMeMyMoney.go(user)
            break
        elif yes == 'Q' or yes == 'q':
            exit()
        else:
            print("[!]Wrong Input! Try again...")
            continue

    t = tryAgain()
    if t == False:
        convert()

main()
