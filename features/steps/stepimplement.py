import requests
from behave import *
from utilities.resources import *
from utilities.payload import *


@given("The Book details which need to be added to Library")
def step_imp(context):
    context.url = getconfig()["API"]["endpoint"] + ApiResources.AddBook
    context.payload = addbookPayload("adrc", "200")
    context.headers = {"Content-Type": "application/json"}


@when("We execute the AddBook API post method")
def step_imp(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers,)


@then("Book is successfully added")
def step_imp(context):
    print(context.response.status_code)
    json_resopnse = context.response.json()
    context.book_ID = json_resopnse["ID"]
    print("jason response is :", json_resopnse)
    print(type(json_resopnse))
    print("Book ID is :", context.book_ID)


@given("The Book details with {isbn} and {aisle}")
def step_imp(context, isbn, aisle):
    context.url = getconfig()["API"]["endpoint"] + ApiResources.AddBook
    context.payload = addbookPayload(isbn, aisle)
    context.headers = {"Content-Type": "application/json"}


@given("I have GitHub credentials")
def step_impl(context):
    context.url2 = getconfig()["API"]["GitHubendpoint"] + ApiResources.GitHubListRepo
    context.se = requests.session()
    context.se.auth = (getUsername(), getToken())


@when("I hit getRepo API of GitHub")
def step_impl(context):
    print("Hitting Github Url and with session manager")
    context.response = context.se.get(context.url2)


@then("Status code of response should be {statusCode:d}")
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
