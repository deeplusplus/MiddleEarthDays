import json
from calendar import Calendar
from datetime import datetime
from random import randint

def main():
    calendar = Calendar("calendar.json")

    todaysEvents = calendar.getCurrentEvents(datetime.today())

    if len(todaysEvents) is 0:
        print('No events today')
    else:
        one_event = todaysEvents[randint(0, len(todaysEvents) - 1)])


if __name__ == "__main__":
    main()
