import tweepy
import time

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
bearer_token = 'YOUR_BEARER_TOKEN'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# Predefined list of facts
facts = [
    # Add facts to the list
]

def tweet_fact(index):
    # Get the fact based on the index
    fact = facts[index]

    # Post the fact as a tweet
    api.update_status(fact)
    print("Tweeted fact:", fact)

# Run the bot
fact_index = 0
while True:
    tweet_fact(fact_index)
    fact_index = (fact_index + 1) % len(facts)  # Move to the next fact
    time.sleep(3600)  # Sleep for 1 hour (3600 seconds)