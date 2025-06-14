from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime


class FitnessClass(BaseModel):
    """
    Fitness class model
    """
    id: UUID = Field(
        ...,
        title="Fitness ID",
        description="Unique ID of the fitness class"
    )
    name: str = Field(
        ...,
        title="Class Name",
        description="Name of the fitness class (e.g., Yoga, Zumba)"
    )
    date_time: datetime = Field(
        ...,
        title="Date & Time",
        description="Scheduled date and time of the class"
    )
    instructor: str = Field(
        ...,
        title="Instructor",
        description="Name of the class instructor"
    )
    available_slots: int = Field(
        ...,
        title="Available Slots",
        description="Number of available booking slots for the class"
    )

class BookingRequest(BaseModel):
    """
    Request model for booking a class
    """
    class_id: UUID = Field(
        ...,
        title="Class ID",
        description="ID of the class to be booked"
    )
    client_name: str = Field(
        ...,
        min_length=1,
        title="Client Name",
        description="Name of the client booking the class"
    )
    client_email: EmailStr = Field(
        ...,
        title="Client Email",
        description="Email address of the client booking the class"
    )

    model_config = {
        class_id: "f2b1c3d4-5678-90ab-cdef-1234567890ab",
        client_name: "sujith",
        client_email: "suji@gmail.com"
    }

class Booking(BaseModel):
    """
    Booking confirmation model
    """
    id: UUID = Field(
        ...,
        title="Booking ID",
        description="Unique ID of the booking"
    )
    class_id: UUID = Field(
        ...,
        title="Class ID",
        description="ID of the class booked"
    )
    client_name: str = Field(
        ...,
        title="Client Name",
        description="Name of the client"
    )
    client_email: EmailStr = Field(
        ...,
        title="Client Email",
        description="Email address of the client"
    )
    booked_at: datetime = Field(
        ...,
        title="Booked At",
        description="Timestamp when the booking was made"
    )
