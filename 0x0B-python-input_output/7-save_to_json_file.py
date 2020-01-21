#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    import json
    json_rep = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as a_file:
        n_byt = a_file.write(json_rep)
