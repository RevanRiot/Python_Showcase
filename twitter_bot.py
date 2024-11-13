# File: twitter_bot.py

import tweepy

def create_api():
    """Authenticate and create the API object."""
    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"
    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def tweet_message(api, message):
    """Posts a tweet."""
    try:
        api.update_status(message)
        print("Tweet sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    api = create_api()
    message = input("Enter your tweet: ")
    tweet_message(api, message)
