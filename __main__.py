import json
from calendar import Calendar


def main():
    calendar = Calendar("calendar.json")

    thisHappenedToday = calendar.whatHappenedToday()


if __name__ == "__main__":
    main()
