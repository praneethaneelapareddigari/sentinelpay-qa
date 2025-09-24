import os, pytest, requests, random, string
from faker import Faker

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://httpbin.org")

@pytest.fixture(scope="session")
def api_key():
    return os.getenv("API_KEY", "demo-key")

@pytest.fixture
def faker():
    return Faker()

@pytest.fixture
def session(api_key):
    s = requests.Session()
    s.headers.update({"x-api-key": api_key})
    return s
