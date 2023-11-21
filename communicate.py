import smtplib
import pywhatkit

def sms():
    # prerequisitive pip install twilio
    from twilio.rest import Client
    # setup your twilio account
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    recipient_phone_number = input("Enter Recipient_Phone_Number")
    twilio_phone_number = input("Enter your twilio phone_Number")
    message = input("Enter message to send")
    # Send a text message
    message = client.messages.create(
    to=recipient_phone_number,
    from_=twilio_phone_number,
    body=message)
    print(f"Message sent with SID: {message.sid}")

def whatsapp():
    # prerequisitive
    # pip install pywhatkit
    # sudo apt-get install python3-tk python3-dev

    # Get contact number and message from the user
    contact_number = input("Enter contact number to whom to send the message: ")
    message = input("\nEnter message to send: ")
    
    # Send the message at a specific time (e.g., 10:37 AM)
    pywhatkit.sendwhatmsg(contact_number, message, 10, 37)import pywhatkit


def email():
    # Your email configuration
    # Set up your email, password, and SMTP server
    email_address = "your_email@gmail.com"
    password = "your_password"
    smtp_server = "smtp.gmail.com"
    port = 587

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(email_address, password)

        to_address = input("Enter the recipient's email address: ")
        subject = input("Enter the email subject: ")
        message = input("Enter the email message: ")

        email_content = f"Subject: {subject}\n\n{message}"
        server.sendmail(email_address, to_address, email_content)
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        server.quit()

def options():
    while True:
            print("""
            Choose from the below options:
            Press 1: To communicate through whatsapp
            Press 2: To communicate through sms
            Press 3: To communicate through email
            Press 0: Back to main menu    """)
            choice2 = input("Enter Choice: ")
            print(choice2)
            if int(choice2) == 1:
                whatsapp()
            elif int(choice2) == 2:
                sms()
            elif int(choice2) == 3:
                email()
            elif int(choice2) == 0:
                break
            else:
                print("Invalid Entry")

if __name__== "__main__":
    options()
