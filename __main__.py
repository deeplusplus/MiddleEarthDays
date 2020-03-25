import json
from calendar import Calendar


def main():
    calendar = Calendar("calendar.json")

    print(calendar.getTodaysDate())


if __name__ == "__main__":
    main()
