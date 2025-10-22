import requests
from behave import given, when, then

BASE_URL = "http://localhost:8000"

@given("the API is running")
def step_api_running(context):
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200

@when('I send a GET request to "/tasks"')
def step_get_tasks(context):
    context.response = requests.get(f"{BASE_URL}/tasks")

@then("I receive a 200 status code")
def step_check_status(context):
    assert context.response.status_code == 200