#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    import json
    json_rep = json.dump(my_obj, filename)
