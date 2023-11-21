print("\t\t\tWelcome to my Unique Project..")
print("\t\t\t------------------------------")


import alsaaudio
import pygame

while True:
    print("""
    Press 1: To open Notepad / Chrome / Firefox
    Press 2: To Send message using whatsapp / sms / email
    Press 3: To control features of speakers
    Press 4: To post on Insta / Twitter / Facebook / Linkedin
    Press 5: To fetch longitude and latitude values and show the map link
    Press 6: To play with tweets (getting twitter trends, posts with hashtag)
    Press 7: To get answer from ChatGPT
    Press 8: To get web_scrapping from wikipedia
    Press 0: To exit    """)

    choice = input("Enter your choice :")
    print(choice)

    # To open Notepad / Chrome / Firefox
    if int(choice) == 1:
        from my_sys import menu
        menu()

    # To Send message using whatsapp / sms / email
    elif int(choice) == 2:
        from communicate import options
        options()

    # To control features of speakers
    elif int(choice) == 3:
        from speaker import speaker_control_menu
        speaker_control_menu()


    # To post on Insta / Twitter / Facebook / Linkedin
    elif int(choice) == 4:
        from posts import platform
        platform()

    # To fetch longitude and latitude values and show the map link
    elif int(choice) == 5:
        from geo import geo_in_map
        geo_in_map()


    # To play with tweets (getting twitter trends, posts with hashtag)
    elif int(choice) == 6:
        from twitter import menu
        menu()

    # To get answer from ChatGPT
    elif int(choice) == 7:
        from ai import chatgpt
        chatgpt()
        
    # To get web_scrapping from wikipedia
    elif int(choice) == 8:
        from scrap import wiki
        wiki()

    elif int(choice) == 0:
        print("\t\t\tThanks!!! Visit Again...")
        break

    else:
        print("Not Supported")

