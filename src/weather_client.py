import requests


class WeatherClient:
    def __init__(self, api_key: str, base_url: str) -> None:
        self.api_key = api_key
        self.base_url = base_url

    def _get(
        self, endpoint: str, location: str, params: dict | None = None
    ) -> requests.Response:
        request_params = {
            "key": self.api_key,
            "q": location,
        }
        if params:
            request_params.update(params)

        response = requests.get(self.base_url + endpoint, params=request_params)
        return response

    def get_current_weather(
        self, location: str, params: dict | None = None
    ) -> requests.Response:
        return self._get("/current.json", location, params)

    def search(self, location: str, params: dict | None = None) -> requests.Response:
        return self._get("/search.json", location, params)
