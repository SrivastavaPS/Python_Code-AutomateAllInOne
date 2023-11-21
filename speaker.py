import alsaaudio
import pygame
import pyttsx3

def adjust_volume():
    # prerequisite - pip install pyalsaaudio
    volume = int(input("Enter the desired Volume: "))
    mixer = alsaaudio.Mixer()
    mixer.setvolume(volume)
    print(f"Volume is set to {volume}")

def mute_speaker():
    mixer = alsaaudio.Mixer()
    mixer.setmute(1)

def unmute_speaker():
    mixer = alsaaudio.Mixer()
    mixer.setmute(0)

def play_audio():
    # prerequisite - pip install pygame
    # Initialize pygame
    pygame.init()
    # load the audio file
    audio_file = "song.mp3"
    # set the speaker as the audio output device
    pygame.mixer.init(frequency=1000, size=16, channels=2, buffer=4096)
    pygame.mixer.music.load(audio_file)
    # play the audio file
    pygame.mixer.music.play()

def text_to_speach():
    # Initialize the TTS engine
    speaker = pyttsx3.init()
    # Set properties (optional)
    speaker.setProperty('rate', 150)  # Speed of speech (words per minute)
    speaker.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    # Text to be converted to speech
    text = input("Enter text to listen: ")
    # Convert text to speech and play it
    speaker.say(text)
    # Wait for the speech to finish
    speaker.runAndWait()

def speaker_control_menu():
    while True:
        print("""
        Choose from the below options:
        Press 1: To Adjust Speaker Volume
        Press 2: To Mute
        Press 3: To Unmute
        Press 4: To Play audio file
        Press 5: To Play the text
        Press 0: Back to the main menu    """)

        choice = input("Enter Choice: ")
        print(choice)

        if int(choice) == 1:
            adjust_volume()
        elif int(choice) == 2:
            mute_speaker()
        elif int(choice) == 3:
            unmute_speaker()
        elif int(choice) == 4:
            play_audio()
        elif int(choice) == 5:
            text_to_speach()
        elif int(choice) == 0:
            break
        else:
            print("Invalid Entry")

if __name__ == "__main__":
    speaker_control_menu()

