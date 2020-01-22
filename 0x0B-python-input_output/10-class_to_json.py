#!/usr/bin/python3
def class_to_json(obj):
    import json
    return obj.__dict__
