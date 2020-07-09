# 2020
# Operations json
# Designed and powered by LGleba

import json


# From json(string) to dictionary
def json_to_dict(string):
    # Example: string = '{"a": "b"}'
    return json.loads(string)


# From dictionary to json(string)
def dict_to_json(dictionary):
    # Example: d = {'a': 'b'}
    return json.dumps(dictionary)


# Save json(dictionary)
def save_json(filename, dictionary):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)


# Download json(dictionary)
def download_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)
