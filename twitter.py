import tweepy

# Set up your Twitter API credentials
consumer_key = '<your_consumer_key>'
consumer_secret = '<your_consumer_secret>'
access_token = '<your_access_token>'
access_token_secret = '<your_access_token_secret>'
bearer_token = '<your_bearer_token>'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

def twitter_trends():
    # Get the top 10 trending topics worldwide
    trends = api.available_trends()
    trending_topics = trends[0]['trends']

    print("Top 10 Trending Topics Worldwide:")
    for topic in trending_topics[:10]:
        print(topic['name'])


def twitter_posts():
    hashtag = input("Enter the desired hashtag: ")
    print(hashtag)
    # Get tweets based on a particular hashtag
    tweets = api.search_tweets(q=f'#{hashtag}', count=10)
    print(f"\nRecent tweets with #{hashtag}:")
    for tweet in tweets:
        print(f"{tweet.user.screen_name}: {tweet.text}")


def menu():
    while True:
            print("""
            Choose from the below options:
            Press 1: To get twitter trends
            Press 2: To get posts with particular hashtag
            Press 0: Back to main menu    """)
            choice6 = input("Enter Choice: ")
            print(choice6)
            if int(choice6) == 1:
                twitter_trends()
            elif int(choice6) == 2:
                twitter_posts()
            elif int(choice6) == 0:
                break
            else:
                print("Invalid Entry")


if __name__ =="__main__":
    menu()
