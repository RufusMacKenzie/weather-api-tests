import pytest
import os
from dotenv import load_dotenv
from src.weather_client import WeatherClient


load_dotenv()


@pytest.fixture(scope="module")
def weather_client():
    api_key = os.environ.get("WEATHER_API_KEY")
    base_url = os.environ.get("WEATHER_BASE_URL")
    if not api_key:
        raise ValueError("WEATHER_API_KEY not set — check your .env file")
    if not base_url:
        raise ValueError("WEATHER_BASE_URL not set — check your .env file")
    return WeatherClient(api_key=api_key, base_url=base_url)


@pytest.fixture(scope="module")
def current_weather_json(weather_client):
    return weather_client.get_current_weather("01748").json()
