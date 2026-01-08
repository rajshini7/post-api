import requests
from config.settings import BASE_URL, AUTH_TOKEN

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AUTH_TOKEN}"
        })

    def get(self, endpoint):
        return self.session.get(f"{BASE_URL}{endpoint}")

    def post(self, endpoint, payload):
        return self.session.post(f"{BASE_URL}{endpoint}", json=payload)

    def put(self, endpoint, payload):
        return self.session.put(f"{BASE_URL}{endpoint}", json=payload)

    def patch(self, endpoint, payload):
        return self.session.patch(f"{BASE_URL}{endpoint}", json=payload)

    def delete(self, endpoint):
        return self.session.delete(f"{BASE_URL}{endpoint}")
