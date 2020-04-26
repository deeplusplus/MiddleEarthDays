import json
import sys
from code_retriever import CodeRetriever
from datetime import datetime, timezone
from twitter_client import getTwitterClient
from dateutil.parser import parse

code_retriever = CodeRetriever()

def main():
    twitter_client = getTwitterClient()

    handleNewQueries(twitter_client)


def handleNewQueries(client):
    new_mentions = client.GetMentions(count=20, return_json=True)
    timing_interval = 60    

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
                query_code_number = parsed_tweet_text.strip()
                lamc_section = code_retriever.getCodeByNumber(query_code_number)
                tweet_text = make_tweet_content_from_section_number(lamc_section)
                client.PostUpdate(tweet_text, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
            except:
                print('Something went horribly wrong')

def make_tweet_content_from_section_number(code_object):
    tweet_text  = "LA Municipal Code " + code_object["number"] + "\n" + code_object["Text"] + "\n" + code_object["Link"]
    return tweet_text

if __name__ == "__main__":
    main()
