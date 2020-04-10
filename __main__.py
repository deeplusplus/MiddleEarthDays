import json
import sys
from me_calendar import Calendar
from datetime import datetime, timezone
from twitter_client import getTwitterClient
from dateutil.parser import parse

calendar = Calendar("calendar.json")

def main():
    twitter_client = getTwitterClient()

    handleDailyTweet(twitter_client)

    handleNewQueries(twitter_client)


def handleNewQueries(client):
    new_mentions = client.GetMentions(count=20, return_json=True)
    timing_interval = 300

    if len(sys.argv) > 1:
        timing_interval = int(sys.argv[1])
    

    for mention in new_mentions:
        time_since_tweet =  datetime.now(timezone.utc) - parse(mention['created_at'])

        if time_since_tweet.seconds <= timing_interval:
            parsed_tweet_text = ''
            
            unparsed_tweet_text = mention['text']
            tweet_id = mention['id']

            tweet_as_list = unparsed_tweet_text.split()

            for split_item in tweet_as_list: 
                if split_item[0] is not '@':
                    parsed_tweet_text += split_item + ' '
            
            try:
                query_date = parse(parsed_tweet_text)
                event_text = calendar.getRandomEventOnDate(query_date)
                client.PostUpdate(event_text, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
            except:
                print('Something went horribly wrong')


def handleDailyTweet(client):
    event_text = calendar.getRandomEventOnDate(datetime.now())

    if event_text is not Calendar.CONST_DEFAULT_RESPONSE:
        client.PostUpdate(event_text)


if __name__ == "__main__":
    main()
