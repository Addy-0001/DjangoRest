from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    # request.body
    body = request.body  # we're assuming that this is going to be a byte string of json data
    data = {}

    try:
        data = json.loads(body) # Takes a string of JSON data and turns it into a python dictionary
    except:
        pass
    print(body)

    print(data)

    return JsonResponse({"message": "Hi there, this is your django api response!"})
