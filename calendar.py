import json
from datetime import datetime

class Calendar:
    def __init__(self, filename):
        self._calendar = {}
        with open('calendar.json') as json_calendar:
            calendar = json.load(json_calendar)
            self._calendar = calendar


    def whatHappenedToday(self):
        todays_date = datetime.now()
        
        todays_month = todays_date.month
        todays_day = todays_date.day

        print(self._calendar['months'][todays_month - 1])