import os
import requests
import pytest


def test_missing_q_returns_400_1003():
    # Testing q param not specified
    url = os.environ.get("WEATHER_BASE_URL") + "/current.json"
    params = {"key": os.environ.get("WEATHER_API_KEY")}
    response = requests.get(url, params=params)
    assert response.status_code == 400
    response_json = response.json()
    error = response_json.get("error")
    assert error is not None, "Expected error object in response but got None"
    assert error.get("code") == 1003


@pytest.mark.parametrize(
    "location, expected_code",
    [
        ("xyzzy", 1006),
        ("", 1003),  # Testing empty q param
    ],
)
def test_invalid_location_returns_400(weather_client, location, expected_code):
    response = weather_client.get_current_weather(location)
    assert response.status_code == 400
    response_json = response.json()
    error = response_json.get("error")
    assert error is not None, "Expected error object in response but got None"
    assert error.get("code") == expected_code


def test_invalid_key_returns_401_2006():
    url = os.environ.get("WEATHER_BASE_URL") + "/current.json"
    params = {"key": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6"}
    response = requests.get(url, params=params)
    assert response.status_code == 401
    response_json = response.json()
    error = response_json.get("error")
    assert error is not None, "Expected error object in response but got None"
    assert error.get("code") == 2006
