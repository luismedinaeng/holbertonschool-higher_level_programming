#!/usr/bin/python3
def inherits_from(obj, a_class):
    if issubclass(obj.__class__, a_class):
        return True
    else:
        return False
