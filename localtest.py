import requests
from requests_oauthlib import OAuth1
import os
import random

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

allquotes = list(open('quotes.txt'))

def random_quote():
  return random.choice(allquotes).rstrip()

def format_quote(quote):
  return {"text": "{}".format(quote)}

def connect_to_oauth(consumer_key, consumer_secret, access_token, access_token_secret):
  url = "https://api.twitter.com/2/tweets"
  auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
  return url, auth

def main():
  fact = random_quote()
  payload = format_quote(fact)
  url, auth = connect_to_oauth(
      consumer_key, consumer_secret, access_token, access_token_secret
  )
  request = requests.post(
      auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
  )

if __name__ == "__main__":
  main()
