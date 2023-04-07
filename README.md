# Quote bot automation!

Since cheap bots done quick has been suspended, I coded up a method to use Twitter for Developers and Google Cloud to automatically tweet quotes/similar every hour! It's completely free and I've detailed the steps to take below.

## Setup Twitter for Developers

The first step is to set up a Twitter Developer account, and this can be done with just the bot account you have in mind. Go to [the developer platform](https://developer.twitter.com/en) and register for an account. It'll require you to enter what you will be using the API for. Since we don't need to use the bot for anything else, type out something that states you will be using the bot only to post quotes and similar, not for accessing or collecting other users' data. Getting past 250 characters is arguably the hardest part :)

After you have registered, create a project on the platform. Name your project and its app whatever you deem fit. In the settings of the app, set up `User authentication settings`. Select `Read and write` for app permissions, `Web App, Automated App or Bot` for Type of App, and enter any Callback URI / Redirect URL in App Info. After you finish this, go to Keys and tokens in your app.

Click Generate (or Regenerate) in `API Key and Secret` and `Access Token and Secret`. Save all four of these codes.

## Authentication

To allow your app access to the bot account, we need to allow authentication. Download [insomnia](https://insomnia.rest/) and create an account. If a document hasn't been created automatically, create one. 

Go to the DEBUG tab and change the `GET` option to `POST` in the dropdown of the middle bar. Paste https://api.twitter.com/oauth/request_token into the text box next to the dropdown. Then, below the text box, choose `OAuth 1` from the Authentication tab, which should initially read "No Authentication". 

In the OAuth 1 section, Paste your Consumer (API) Keys and your Token Keys into the corresponding boxes, including the secret keys as well. Then, click `Send`. 

This should create a white box on the right side of Insomnia, something that looks similar to the one below.
```
oauth_token=zlgW3QAAAAAA2_NZAAABfxxxxxxk&oauth_token_secret=pBYEQzdbyMqIcyDzyn0X7LDxxxxxxxxx&oauth_callback_confirmed=true
```
Copy the contents of the box. 

Copy the oauth_token value (`zlgW3QAAAAAA2_NZAAABfxxxxxxk` in the example) and paste it after https://api.twitter.com/oauth/authenticate?oauth_token=. Visit this link on your bot account; notice that it redirects you, and the website link now has `oauth_verifier=` in it. Copy this value.

Now, go back to Insomnia. Make another `POST` request, this time with the link below. 
```
https://api.twitter.com/oauth/access_token?oauth_verifier=(the verifier in the link)&oauth_token=(your previous oauth_token value)
```
Hit `Send`. You should recieve a response like below: 
```
oauth_token=62532xx-eWudHldSbIaelX7swmsiHImEL4KinwaGloxxxxxx&oauth_token_secret=2EEfA6BG5ly3sR3XjE0IBSnlQu4ZrUzPiYxxxxxx&user_id=1458900662935343104&screen_name=FactualCat
```
Verify that these are the Access and Access Secret tokens for your bot.

## Google Cloud Functions

Create an account and [set up](https://cloud.google.com/run/docs/setup) the environment as described here. You will need to enter card information, but you will not be billed for the bot as the posting is well beneath the free tier limit. 

Create a project, if it hasn't been automatically created already. You will need to enable the necessary APIs [here](https://console.cloud.google.com/flows/enableapi?apiid=cloudfunctions,cloudbuild.googleapis.com&redirect=https://cloud.google.com/functions/docs/quickstart-nodejs). 

Go to the [Cloud Functions Overview page](https://console.cloud.google.com/functions/list). Click **Create function**. For Environment, select 1st gen. Name your function, and select the trigger as "Cloud Pub/Sub" with a new topic name. Set your cloud region to your location. Expand the Runtime option, and add 4 different variables: `"CONSUMER_KEY"` (your api key), `"CONSUMER_SECRET"` (your secret api key), `"ACCESS_TOKEN"`, and `"ACCESS_TOKEN_SECRET"`. Paste your keys into these different runtime environment variables. Click next.

Copy `main.py` from this github into the one on your project. Additionally, paste `requirements.txt` exactly into the file with the same name. Add a file called `quotes.txt` and put all of your quotes, each on a **new line**, into the quotes file. 

Alternatively, make a txti.es file, put each of your quotes on a new line, and save it. Replace link displayed in `main.py`. This will allow you to print new lines in different quotes.

Click deploy. The function should successfully deploy within a minute.

## Google Cloud Scheduler

Lastly, the [Cloud Scheduler](https://console.cloud.google.com/cloudscheduler) can be used to time your bot tweets. Enable the two APIS linked [here](https://console.cloud.google.com/marketplace/product/google/pubsub.googleapis.com) and [here](https://console.cloud.google.com/marketplace/product/google/cloudscheduler.googleapis.com). 

In the [Cloud Scheduler Page](https://console.cloud.google.com/cloudscheduler?project=xiaoquotedbot), click `Create Job`. Enter an arbitrary name and `0 */1 * * *` in `Frequency` (hourly tweets). Choose an arbitrary timezone. Click `Continue`. 

Choose `Pub/Sub` as the Target type and select the topic that you previously created. Enter anything in `Message body`. 

Click `Create`. Once the job has been successfully deployed, you can test it out by going to the three dots under `Actions` and choosing `Force Run`. The bot should now be set up and running!