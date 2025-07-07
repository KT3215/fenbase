#handles sync logic & refactoring from google calendar
import pandas as pd 
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
client_secrets_file = os.path.join(BASE_DIR, "credentials.json")

flow = InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, SCOPES
)

def fetch_calendar_events():
  """Basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  token_path = os.path.join(BASE_DIR, "token.json")

  if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          client_secrets_file, SCOPES
      )
      creds = flow.run_local_server(port=8000)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return
    event_list = []
    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      event_list.append({"start": start, "summary": event["summary"]})
      #print(start, event["summary"])
    print(event_list)
    event_dict = {event["start"]: event["summary"] for event in event_list}
    print(event_dict)
    return event_dict

  except HttpError as error:
    print(f"An error occurred: {error}")

def main():
    fetch_calendar_events()

if __name__ == "__main__":
  main()

