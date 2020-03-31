import json
from me_calendar import Calendar
from datetime import datetime
from random import randint
from twitter_client import getTwitterClient
from dateutil.parser import parse

calendar = Calendar("calendar.json")

def main():
    twitter_client = getTwitterClient()

    handleDailyTweet(twitter_client)

    handleNewQueries(twitter_client)


def handleNewQueries(client):
    new_mentions = client.GetMentions(count=20, return_json=True)

    for mention in new_mentions:
        unparsed_tweet_text = mention['text']
        parsed_tweet_text = ''
        sender = mention['user']['screen_name']
        tweet_as_list = unparsed_tweet_text.split()

        for split_item in tweet_as_list: 
            if split_item[0] is not '@':
                parsed_tweet_text += split_item + ' '
        
        try:
            query_date = parse(parsed_tweet_text)
            print('Parse of date worked')
            event_text = calendar.getRandomEventOnDate(query_date)
            print(event_text)
            if len(event_text) is not 0:
                client.PostUpdate('@' + sender + ' ' + event_text)
        except:
            print('Something went horribly wrong')


def handleDailyTweet(client):
    event_text = calendar.getRandomEventOnDate(datetime.now())

    if len(event_text) is not 0:
        client.PostUpdate(event_text)


if __name__ == "__main__":
    main()
