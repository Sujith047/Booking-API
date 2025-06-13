# Fitness Class Booking-API

A FastAPI-based backend service for managing fitness class schedules and bookings.


## Project Structure

```
Booking-API/
├── .github/
│   └── workflows/
│       └── fitness.yml
├── services/
│   └── fitness/
│       ├── .gitignore
│       ├── README.md
│       └── app/
│           ├── main.py
│           ├── requirements-dev.txt
│           ├── pytest.ini
│           ├── book/
│           │   ├── __init__.py
│           │   ├── api.py
│           │   ├── schemas.py
│           │   ├── dependency.py
│           │   └── tests/
│           │       ├── __init__.py
│           │       └── test_book.py
│           └── __init__.py
├── .gitignore
└── README.md
```

# Notes

- The `main.py` file in `services/fitness/app/` is the FastAPI entry point.
- The `book/` directory contains booking-related logic, schemas, dependencies, and tests.
- Workflow automation is managed by `.github/workflows/fitness.yml`.
- Root-level and service-level `.gitignore` and `README.md` files help organize the project.
