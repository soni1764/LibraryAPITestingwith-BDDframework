from utilities.configuration import *


def addbookPayload(isbn, aisle):
    body = {

            "name":"Learn New Books to get knowledge",
            "isbn": isbn,
            "aisle": aisle,
            "author":"SoniG"

            }

    return body


def buildPayloadFromDB(query):
    AddBody = {}
    tp = getQuery(query)
    AddBody["name"] = tp[0]
    AddBody["isbn"] = tp[1]
    AddBody["aisle"] = tp[2]
    AddBody["author"] = tp[3]
    print(AddBody)
    print(type(AddBody))
    return AddBody
