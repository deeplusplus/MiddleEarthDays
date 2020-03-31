import json
from random import randint

class Calendar:
    def __init__(self, filename):
        self._calendar = {}
        with open('calendar.json') as json_calendar:
            calendar = json.load(json_calendar)
            self._calendar = calendar


    def getCurrentEvents(self, date):
        events = []

        query_month = date.month
        query_day = date.day

        month = self._calendar['months'][query_month - 1]

        for day in month['days']:
            if day['day'] is query_day:
                events = day['events']

        return events

    def getRandomEventOnDate(self, date):
        todaysEvents = self.getCurrentEvents(date)

        if len(todaysEvents) is not 0:
            return todaysEvents[randint(0, len(todaysEvents) - 1)]
        else:
            return ''