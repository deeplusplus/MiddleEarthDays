import json
from me_calendar import Calendar
from datetime import datetime
from random import randint
from twitter_client import getTwitterClient

def main():
    calendar = Calendar("calendar.json")

    todaysEvents = calendar.getCurrentEvents(datetime.today())

    if len(todaysEvents) is 0:
        print('No events today')
    else:
        twitter_client = getTwitterClient()

        one_event = todaysEvents[randint(0, len(todaysEvents) - 1)]

        twitter_client.PostUpdate(one_event)


if __name__ == "__main__":
    main()
