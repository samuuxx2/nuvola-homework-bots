import requests
from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def get_homework():
    # esempio di compiti
    homework = [
        "Geografia - Asia fisica pp F4-F5 esercizi 22",
        "Inglese - pag 49 present perfect"
    ]
    return homework


def add_to_calendar(tasks):

    creds = Credentials.from_authorized_user_file("token.json")

    service = build("calendar", "v3", credentials=creds)

    for task in tasks:

        event = {
            "summary": task,
            "start": {
                "date": datetime.now().strftime("%Y-%m-%d")
            },
            "end": {
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        }

        service.events().insert(
            calendarId="primary",
            body=event
        ).execute()


if __name__ == "__main__":

    tasks = get_homework()
    add_to_calendar(tasks)
