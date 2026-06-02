import pytest


@pytest.mark.parametrize(
    "location",
    [
        "01748",
        "Hopkinton",
        "48.8567,2.3508",
        "auto:ip",
    ],
)
def test_valid_location_returns_200(weather_client, location):
    response = weather_client.get_current_weather(location)
    assert response.status_code == 200
