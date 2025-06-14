from fastapi import APIRouter, HTTPException, Query, status
from typing import List
from uuid import uuid4
from .schemas import FitnessClass, BookingRequest, Booking
from .dependency import (
    get_classes_with_timezone,
    get_classes_db,
    get_bookings_db,
    get_current_time
)


router_booking = APIRouter()


@router_booking.get(
    path="/classes",
    status_code=status.HTTP_200_OK,
    response_model=List[FitnessClass]
)
def get_classes(timezone: str = Query(
    default="Asia/Kolkata",
    title="Timezone",
    description="Timezone to get fitness classes"
    )
):
    """
    Get fitness classes available in the specified timezone
    """
    return get_classes_with_timezone(timezone)


@router_booking.post(
    path="/book",
    response_model=Booking,
    status_code=status.HTTP_201_CREATED
)
def book_class(booking_req: BookingRequest):
    """
    Book a fitness class
    """
    classes = get_classes_db()
    fitness_class = next((c for c in classes if c.id == booking_req.class_id), None)
    
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No available slots")

    fitness_class.available_slots -= 1
    booking = Booking(
        id=uuid4(),
        class_id=fitness_class.id,
        client_name=booking_req.client_name,
        client_email=booking_req.client_email,
        booked_at=get_current_time()
    )
    get_bookings_db().append(booking)
    return booking


@router_booking.get(
    path="/bookings",
    status_code=status.HTTP_200_OK,
    response_model=List[Booking]
)
def get_bookings(email: str):
    """
    Get bookings for a specific client by email
    """
    return [b for b in get_bookings_db() if b.client_email == email]