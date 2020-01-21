#!/usr/bin/python3
def load_from_json_file(filename):
    import json
    with open(filename, mode='r', encoding='utf-8') as a_file:
        json_rep = a_file.read()
    return json.loads(json_rep)
