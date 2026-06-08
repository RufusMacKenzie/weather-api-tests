# WeatherAPI pytest Test Suite

A pytest-based test suite validating the [WeatherAPI](https://www.weatherapi.com) REST API, 
built as a portfolio project to demonstrate Python test automation practices.

## What's tested
- Current weather endpoint — valid location types, error handling, response schema
- Search endpoint — valid searches, empty results, schema validation, field completeness

## Tech stack
- Python / pytest
- pytest-check for soft assertions
- GitHub Actions CI/CD

## Running the tests
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your WeatherAPI key:
```
WEATHER_API_KEY=your_key_here
WEATHER_BASE_URL=http://api.weatherapi.com/v1
```
4. Run: `pytest`

## CI
Tests run automatically on every push via GitHub Actions.