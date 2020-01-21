#!/usr/bin/python3
import sys
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    if os.path.exists("add_item.json"):
        obj_json = load_from_json_file("add_item.json")
    else:
        obj_json = []

        argc = len(sys.argv)

        for i in range(1, argc):
            obj_json.append(sys.argv[i])

        save_to_json_file(obj_json, "add_item.json")
