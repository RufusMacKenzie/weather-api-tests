import pytest


@pytest.mark.parametrize(
    "field_name, expected_type",
    [
        ("name", str),
        ("region", str),
        ("country", str),
        ("lat", float),
        ("lon", float),
    ],
)
def test_location_field_is_expected_type(
    current_weather_json, field_name, expected_type
):
    field = current_weather_json.get("location").get(field_name)
    assert isinstance(field, expected_type)


@pytest.mark.parametrize(
    "field_name, expected_type",
    [
        ("temp_f", float),
        ("feelslike_f", float),
        ("wind_mph", float),
        ("humidity", int),
    ],
)
def test_current_field_is_expected_type(
    current_weather_json, field_name, expected_type
):
    field = current_weather_json.get("current").get(field_name)
    assert isinstance(field, expected_type)


def test_current_humidity_is_between_0_and_100(current_weather_json):
    humidity = current_weather_json.get("current").get("humidity")
    assert 0 <= humidity <= 100


@pytest.mark.parametrize(
    "field_name, expected_type",
    [
        ("text", str),
        ("code", int),
    ],
)
def test_current_condition_field_is_expected_type(
    current_weather_json, field_name, expected_type
):
    field = current_weather_json.get("current").get("condition").get(field_name)
    assert isinstance(field, expected_type)
