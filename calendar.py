import json
from datetime import date

class Calendar:

    def __init__(self, filename):
        calendar = {}
        json_calendar = open('calendar.json')
        calendar = json.load(json_calendar)
        self._calendar = calendar

    def getTodaysDate(self):
        return date.today()