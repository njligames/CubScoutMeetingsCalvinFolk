from ics import Calendar, Event
from datetime import datetime
from pytz import timezone

# Schedule data
schedule = [
    {"date": "18 Sep 2024", "title": "Bobcat", "type": "Required", "agenda": "Bobcat Meeting Agenda"},
    {"date": "2 Oct 2024", "title": "Paws on the Path", "type": "Required", "agenda": "Paws on the Path Agenda"},
    {"date": "9 Oct 2024", "title": "Running with the Pack", "type": "Required", "agenda": None},
    {"date": "23 Oct 2024", "title": "Code of the Wolf", "type": "Elective", "agenda": None},
    {"date": "30 Oct 2024", "title": "Finding Your Way", "type": "Elective", "agenda": None},
    {"date": "13 Nov 2024", "title": "Air of the Wolf", "type": "Elective", "agenda": None},
    {"date": "20 Nov 2024", "title": "Paws of Skill", "type": "Elective", "agenda": None},
    {"date": "4 Dec 2024", "title": "Adventures in Coins", "type": "Elective", "agenda": None},
    {"date": "11 Dec 2024", "title": "Race Time Wolf", "type": "Elective", "agenda": None},
    {"date": "18 Dec 2024", "title": "Race Time Wolf", "type": "Elective", "agenda": None},
    {"date": "8 Jan 2025", "title": "Safety in Numbers", "type": "Required", "agenda": None},
]

# Time details for meetings (all meetings are 6:30 PM to 7:30 PM EST)
start_time = "18:30"
end_time = "19:30"
eastern = timezone('America/New_York')

# Initialize a calendar
calendar = Calendar()

# Generate events
for entry in schedule:
    event = Event()
    event.name = f"{entry['title']} ({entry['type']})"
    event.begin = eastern.localize(datetime.strptime(f"{entry['date']} {start_time}", "%d %b %Y %H:%M"))
    event.end = eastern.localize(datetime.strptime(f"{entry['date']} {end_time}", "%d %b %Y %H:%M"))
    event.description = entry['agenda'] if entry['agenda'] else f"{entry['title']} Meeting"
    event.location = "Online"
    calendar.events.add(event)

# Save the ICS file
with open("meeting_schedule.ics", 'w') as f:
    f.writelines(calendar)

print("ICS file created successfully with the correct time zone!")
