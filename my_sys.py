import subprocess

def menu():
    while True:
            print("""
            Choose from the below options:
            Press 1: To open Text Editor 
            Press 2: To open Chrome
            Press 3: To open Firefox
            Press 0: Back to main menu    """)
            choice1 = input("Enter Choice: ")
            print(choice1)
            if int(choice1) == 1:
                subprocess.run(['gedit'])
            elif int(choice1) == 2:
                subprocess.run(['google-chrome'])
            elif int(choice1) == 3:
                subprocess.run(['firefox'])
            elif int(choice1) == 0:
                break
            else:
                print("Invalid Entry")


if __name__ == "__menu__":
    menu()
