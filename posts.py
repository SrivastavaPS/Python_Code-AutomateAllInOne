import tweepy
import facebook
from linkedin import linkedin

def insta():
    print("Instagram's API is more restrictive, and direct posting is not supported for personal accounts.")

def twitter():
    # prerequisitive pip install tweepy
    # Set up your Twitter API credentials
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Post a tweet
    tweet_text = "Hello, Twitter!"
    api.update_status(status=tweet_text)

def fb():
    #prerequisitive pip install facebook-sdk
    
    # Set up your Facebook API credentials
    access_token = 'YOUR_ACCESS_TOKEN'

    # Authenticate with Facebook API
    graph = facebook.GraphAPI(access_token)

    # Post to your Facebook page
    post_message = "Hello, Facebook!"
    graph.put_object(parent_object='me', connection_name='feed', message=post_message)

def linkedin():
    #prerequisitive pip install python-linkedin

    # Set up your LinkedIn API credentials
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    user_token = 'YOUR_USER_TOKEN'
    user_secret = 'YOUR_USER_SECRET'

    # Authenticate with LinkedIn API
    authentication = linkedin.LinkedInDeveloperAuthentication(api_key, api_secret, user_token, user_secret, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    application = linkedin.LinkedInApplication(authentication)
    
    # Post on LinkedIn
    share_message = {
         "comment": "Hello, LinkedIn!",
         "visibility": {"code": "anyone"}
    }
    application.submit_share(share_message)

def platform():
    while True:
            print("""
            Choose from the below options:
            Press 1: To post on Insta
            Press 2: To post on Twitter
            Press 3: To post on Facebook
            Press 4: To post on Linkedin
            Press 0: Back to main menu    """)
            choice4 = input("Enter Choice: ")
            print(choice4)
            if int(choice4) == 1:
                insta()
            elif int(choice4) == 2:
                twitter()
            elif int(choice4) == 3:
                fb()
            elif int(choice4) == 4:
                linkedin()
            elif int(choice4) == 0:
                break
            else:
                print("Invalid Entry")

if __name__=="__main__":
    platform()
