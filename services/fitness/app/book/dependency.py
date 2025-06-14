from .schemas import FitnessClass
from uuid import uuid4
from datetime import datetime, timedelta
from pytz import timezone, UnknownTimeZoneError
from fastapi import HTTPException

# In-memory databases
classes_db = []
bookings_db = []


IST = timezone("Asia/Kolkata")


def seed_classes():
    classes_db.clear()
    now = datetime.now(IST)
    classes_db.extend([
        FitnessClass(id=uuid4(), name="Yoga", date_time=now.replace(hour=7, minute=0) + timedelta(days=1), instructor="Ramesh", available_slots=5),
        FitnessClass(id=uuid4(), name="Zumba", date_time=now.replace(hour=10, minute=0) + timedelta(days=1), instructor="Suresh", available_slots=3),
        FitnessClass(id=uuid4(), name="HIIT", date_time=now.replace(hour=18, minute=0) + timedelta(days=1), instructor="Mahesh", available_slots=4),
    ])

def get_classes_with_timezone(tz_name: str):
    try:
        target_tz = timezone(tz_name)
    except UnknownTimeZoneError:
        raise HTTPException(status_code=400, detail="Invalid timezone")

    return [
        FitnessClass(
            id=c.id,
            name=c.name,
            date_time=c.date_time.astimezone(target_tz),
            instructor=c.instructor,
            available_slots=c.available_slots
        ) for c in classes_db
    ]

def get_current_time():
    return datetime.now(IST)

# Accessors for DBs
def get_classes_db():
    return classes_db

def get_bookings_db():
    return bookings_db
