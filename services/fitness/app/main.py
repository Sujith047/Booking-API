from fastapi import FastAPI

from .book.api import router_booking
from .book.dependency import seed_classes

app = FastAPI(
    title="Fitness Studio Booking API",
    description="API for managing fitness class bookings"
)


@app.get(path="/")
def home():
    return {"message": "Welcome to the Fitness Studio Booking API"}


app.include_router(router_booking)

@app.on_event("startup")
def startup_event():
    seed_classes()

