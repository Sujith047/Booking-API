"""
Test cases for booking fitness classes
"""
from pytest import mark
from fastapi import status
from fastapi.testclient import TestClient
from uuid import uuid4
from datetime import datetime

from app.book.schemas import FitnessClass

from app.main import router_booking
from app.main import app


client = TestClient(app)


@mark.parametrize(
    "timezone, expected_status",
    [
        ("Asia/Kolkata", status.HTTP_200_OK)
    ]
)
def test_get_classes(timezone, expected_status):
    route = router_booking.url_path_for("get_classes")
    response = client.get(route, params={"timezone": timezone})
    assert response.status_code == expected_status

def test_book_class_success(monkeypatch):
    """
    Test successful booking of a fitness class
    """
    class_id = uuid4()
    booking_req = {
        "class_id": str(class_id),
        "client_name": "Test User",
        "client_email": "testuser@example.com"
    }

    mock_class = FitnessClass(
        id=class_id,
        name="Yoga",
        start_time=datetime.now(),
        end_time=datetime.now(),
        available_slots=5,
        instructor="Instructor Name",
        date_time=datetime.now()
    )

    def mock_get_classes_db():
        return [mock_class]

    def mock_get_bookings_db():
        return []

    monkeypatch.setattr("app.book.api.get_classes_db", mock_get_classes_db)
    monkeypatch.setattr("app.book.api.get_bookings_db", mock_get_bookings_db)
    monkeypatch.setattr("app.book.api.get_current_time", lambda: datetime.now())

    route = router_booking.url_path_for("book_class")
    response = client.post(route, json=booking_req)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["class_id"] == str(class_id)
    assert data["client_name"] == "Test User"
    assert data["client_email"] == "testuser@example.com"

def test_book_class_class_not_found(monkeypatch):
    """
    Test booking when class is not found
    """
    booking_req = {
        "class_id": str(uuid4()),
        "client_name": "Test User",
        "client_email": "testuser@example.com"
    }

    def mock_get_classes_db():
        return []

    monkeypatch.setattr("app.book.api.get_classes_db", mock_get_classes_db)

    route = router_booking.url_path_for("book_class")
    response = client.post(route, json=booking_req)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Class not found"

def test_book_class_no_slots(monkeypatch):
    """
    Test booking when no slots are available
    """
    class_id = uuid4()
    booking_req = {
        "class_id": str(class_id),
        "client_name": "Test User",
        "client_email": "testuser@example.com"
    }

    mock_class = FitnessClass(
        id=class_id,
        name="Yoga",
        start_time=datetime.now(),
        end_time=datetime.now(),
        available_slots=0,
        instructor="Instructor Name",
        date_time=datetime.now()
    )

    def mock_get_classes_db():
        return [mock_class]

    monkeypatch.setattr("app.book.api.get_classes_db", mock_get_classes_db)

    route = router_booking.url_path_for("book_class")
    response = client.post(route, json=booking_req)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "No available slots"

def test_book_class_invalid_payload(monkeypatch):
    """
    Test booking with invalid payload
    """
    route = router_booking.url_path_for("book_class")
    response = client.post(route, json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_get_bookings():
    """
    Test get_bookings route
    """
    route = router_booking.url_path_for("get_bookings")
    response = client.get(route, params={"email": "sujith@gmail.com"})
    assert response.status_code == status.HTTP_200_OK
