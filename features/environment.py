import requests
from utilities.payload import *
from utilities.resources import *


def after_scenario(context, scenario):
    if "Library" in scenario.tags:
        url = getconfig()["API"]["endpoint"] + ApiResources.GetBook
        params = {"ID": context.book_ID}
        get_response = requests.get(url, params=params, )
        print("This is after Scenario")
        print("Getting Book details")
        print(get_response.status_code)
        print(get_response.text)

        # print("---------------deleting book-------------")
        url1 = getconfig()["API"]["endpoint"] + ApiResources.DeleteBook
        padLoad = {"ID": context.book_ID}
        deletebook_response = requests.post(url1, json=padLoad, headers=context.headers,)
        print("Deleting book-------------")
        print(deletebook_response.status_code)
        assert deletebook_response.status_code == 200
        json_deletebook = deletebook_response.json()
        print(type(json_deletebook))
        print(json_deletebook)
        assert json_deletebook["msg"] == "book is successfully deleted"
