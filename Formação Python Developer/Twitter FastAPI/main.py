from secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from fastapi import FastAPI

import uvicorn
import tweepy


BRAZIL_WOE_ID = '26062'


def get_tweet_trends(woe_id: int):
    """
    Getting trend topics.

    :param woe_id: trends id
    :return: dictionary
    """
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    trends = api.trends_place(BRAZIL_WOE_ID)

    return [trend for trend in trends]


app = FastAPI()

@app.get("/trends")
def get_treds_route():
    trends = get_tweet_trends()
    return trends


# para rodar o código via FASTAPI deve executar o comando:
# uvicorn main:app --reload

# http://127.0.0.1:8000/docs
#http://localhost:8000/docs

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

