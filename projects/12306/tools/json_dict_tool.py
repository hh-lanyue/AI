import json


def json_to_dict(my_json):
    return json.loads(my_json)


def dict_to_json(my_dict):
    return json.dumps(my_dict)
