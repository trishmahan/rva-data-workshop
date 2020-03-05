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


@pytest.mark.parametrize(
    "not_a_number",
    ["here are some words", "!", {"a": "dictionary"}, ("a", "tuple"), ["a", "list"]],
)
def test_get_double_handles_non_numeric_input(client, not_a_number):
    not_a_number = "this is a string and should not be multiplied by two"
    response = client.get(f"/v1/double/{not_a_number}")
    json_response = response.json
    assert json_response["code"] == "400"
    assert json_response["type"] == "BAD REQUEST"
    assert json_response.get("result") is None
