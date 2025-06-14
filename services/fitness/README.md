# Fitness Service

The API to support Fitness class booking and checking

## Requirements

- git
- python 3.10


## Deployment -CI/CD

A GitHub Action Pipeline defined in the  `.github/workflows/fitness.yl` is used to deploy the service.


## Testing

Unit testing using `pytest`

1. Navigate to service directory

```sh
cd services/fitness
```

2. Create Virtual Environment

```sh
python -m venv venv
```

3. Activate Virtual Environment

```sh
venv/scripts/activate
```

4. Install Dependemcies

```sh
pip install -r app/requirements-dev.txt
```

5. Run Unit Tests

```sh
pytest -c app/pytest.ini --cov --cov-report term-missing
```

### Running the FastAPI

```bash
uvicorn app.main:app --reload
```