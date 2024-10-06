from ics import Calendar, Event
from datetime import datetime
from pytz import timezone

# List of counseling appointment dates
counseling_dates = [
    "7 Oct 2024", "28 Oct 2024", "12 Nov 2024", "25 Nov 2024", "2 Dec 2024", "16 Dec 2024",
    "13 Jan 2025", "28 Jan 2025", "10 Feb 2025", "25 Feb 2025", "3 Mar 2025", "17 Mar 2025",
    "7 Apr 2025", "29 Apr 2025", "5 May 2025", "19 May 2025", "9 Jun 2025"
]

# Time details for appointments (8th period study hall: 12:35 PM to 1:16 PM EST)
start_time = "12:35"
end_time = "13:16"
eastern = timezone('America/New_York')

# Initialize a calendar
calendar = Calendar()

# Generate events for each counseling session
for date in counseling_dates:
    event = Event()
    event.name = "Logan's Counseling with Mrs. Candurra"
    event.begin = eastern.localize(datetime.strptime(f"{date} {start_time}", "%d %b %Y %H:%M"))
    event.end = eastern.localize(datetime.strptime(f"{date} {end_time}", "%d %b %Y %H:%M"))
    event.description = "Counseling session for Logan during 8th period study hall."
    event.location = "School Counseling Office"
    calendar.events.add(event)

# Save the ICS file
with open("logan_counseling_schedule.ics", 'w') as f:
    f.writelines(calendar)

print("ICS file created successfully!")
