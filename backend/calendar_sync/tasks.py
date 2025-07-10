#asynchronous tasks with Hatchet
#asynchronously fetch data from calendar
#from there create reminders, alerts, update weekly schedule summary
#as well as update schedule long term in case of any flash changes
#then upload to supabase db
#future might need asynchronous fetching from dropbox
#TASKS NOT COMPLETING RN!

from hatchet_sdk import Context, EmptyModel, Hatchet
from pydantic import BaseModel
from .google_api import fetch_calendar_events
 
hatchet = Hatchet(debug=True)
 
class SimpleInput(BaseModel):
    message: str
 
@hatchet.task(name="FetchCalendar", input_validator=SimpleInput)
def simple(input: SimpleInput, ctx: Context) -> dict[str, str]:
    events = fetch_calendar_events()

    return {"status": "success", "fetched_events_count": len(events)}

def main() -> None:
    hatchet = Hatchet()
    worker = hatchet.worker("calendar-worker", workflows=[simple])
    worker.start()

    response = hatchet.run(
        workflow="FetchCalendar",
        input={"message": "run"}  # might need to change
    )
 
if __name__ == "__main__":
    main()