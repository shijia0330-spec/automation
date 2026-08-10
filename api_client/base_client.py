import requests


class ApiClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.request(
            method=method,
            url=url,
            timeout=self.timeout,
            **kwargs,
        )

    def get(self, path: str, params=None) -> requests.Response:
        return self.request("GET", path, params=params)

    def post(self, path: str, json=None) -> requests.Response:
        return self.request("POST", path, json=json)

    def put(self, path: str, json=None) -> requests.Response:
        return self.request("PUT", path, json=json)

    def delete(self, path: str) -> requests.Response:
        return self.request("DELETE", path)

    def patch(self, path: str, json=None) -> requests.Response:
        return self.request("PATCH", path, json=json)