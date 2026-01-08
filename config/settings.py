import os

BASE_URL = os.getenv(
    "BASE_URL",
    "https://jsonplaceholder.typicode.com"
)

AUTH_TOKEN = os.getenv(
    "AUTH_TOKEN",
    "dummy-token-for-local"
)
