import pytest
import pytest_check as check


EXPECTED_FIELDS = {"id", "name", "region", "country", "lat", "lon", "url"}


@pytest.mark.parametrize(
    "search_term",
    [
        "01748",
        "Hopkinton",
        "lon",
        "auto:ip",  # returns "Auto, West Virginia" - treated as text search, not IP lookup :)
    ],
)
def test_search_returns_200(weather_client, search_term):
    response = weather_client.search(search_term)
    assert response.status_code == 200


def test_valid_search_returns_results(search_results_json):
    assert search_results_json


def test_invalid_search_returns_empty_list(weather_client):
    response_list = weather_client.search("xyzzy").json()
    assert not response_list


def test_each_result_schema(search_results_json):
    for result in search_results_json:
        check.is_instance(result.get("name"), str, f"name should be str in {result}")
        check.is_instance(
            result.get("region"), str, f"region should be str in {result}"
        )
        check.is_instance(
            result.get("country"), str, f"country should be str in {result}"
        )
        check.is_instance(result.get("lat"), float, f"lat should be float in {result}")
        check.is_instance(result.get("lon"), float, f"lon should be float in {result}")
        check.is_instance(result.get("id"), int, f"id should be int in {result}")
        check.is_instance(result.get("url"), str, f"url should be str in {result}")


def test_no_unexpected_fields_in_search_results(search_results_json):
    for result in search_results_json:
        actual_fields = set(result.keys())
        unexpected_fields = actual_fields - EXPECTED_FIELDS
        check.is_false(
            unexpected_fields,
            f"found unexpected field in returned location {unexpected_fields}",
        )


def test_no_missing_fields_in_search_results(search_results_json):
    for result in search_results_json:
        actual_fields = set(result.keys())
        missing_fields = EXPECTED_FIELDS - actual_fields
        check.is_false(
            missing_fields,
            f"detected missing field in returned location {missing_fields}",
        )
