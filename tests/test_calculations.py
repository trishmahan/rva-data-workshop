from calculations import calculations

import pytest


@pytest.fixture
def client():
    calculations.app.config["TESTING"] = True
    yield calculations.app.test_client()


def test_get_double_returns_expected_response(client):
    number = 1
    response = client.get(f"/v1/double/{number}")
    json_response = response.json
    assert json_response["code"] == "200"
    assert json_response["type"] == "OK"
    assert json_response["result"] == number * 2
