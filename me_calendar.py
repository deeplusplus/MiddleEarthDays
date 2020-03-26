import json

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