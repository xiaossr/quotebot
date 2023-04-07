import requests
from requests_oauthlib import OAuth1
import os
import random
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# replace with your keys
consumer_key = "4LMobye9VTAnpAJCPND4OPZaJ"
consumer_secret = "HXJWaSdwTr4kil0yAJcZC7ZMabloAOclQPKyEAyneKKR0EkJ4k"
access_token = "1536161637358522368-Qu9v09dkDSHqNZLSqmME9l4ohsFCzp"
access_token_secret = "vKPlv2U1GiefzZOrvuxedM4SrLFSz4gp2OsK95A2KlXfH"

#allquotes = list(open("quotes.txt", encoding="utf-8"))
url = "https://txti.es/xiaoquoted"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

allquotes = []
for script in soup.find_all(text=True):
  s = script.get_text().encode("utf-8")
  allquotes.append(s)

allquotes = [s for s in allquotes if s != b" " and s != b"\n" and s != b""]
allquotes = allquotes[1:]

def random_quote():
  return random.choice(allquotes)

def format_quote(quote):
  return {"text": "{}".format(quote)}

def connect_to_oauth(consumer_key, consumer_secret, access_token, access_token_secret):
  url = "https://api.twitter.com/2/tweets"
  auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
  return url, auth

def main():
  #print(allquotes)
  fact = random_quote()
  payload = format_quote(fact)
  payload["text"] = payload["text"][2:-1]
  payload["text"] = payload["text"].replace('\\\\n', '\n')
  #print(payload)
  #url, auth = connect_to_oauth(
  #    consumer_key, consumer_secret, access_token, access_token_secret
  #)
  #request = requests.post(
  #    auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}, verify=False
  #)

if __name__ == "__main__":
  main()
