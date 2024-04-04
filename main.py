import os
from image import picture
from real_time import realTime


def title_bar():
    os.system("cls")
    print("\t**********************************************")
    print("\t    ***** Face Recognition System *****")
    print("\t**********************************************")


def mainMenu():
    while True:
        title_bar()
        print(10 * "*", "WELCOME MENU", 10 * "*")
        print("[1] Detect Face in Image")
        print("[2] Detect Real Time Face")
        print("[3] Quit")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            picture()
        elif choice == 2:
            realTime()
        elif choice == 3:
            print("Thank you")
            break
        else:
            print("Invalid Choice. Enter 1-3")
            mainMenu()

        anotherChance = input("Do you want to perform another operation? (yes/no): ")
        if anotherChance != 'yes':
            break


mainMenu()
