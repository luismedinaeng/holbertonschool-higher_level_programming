#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return a_dictionary
    ks = list(a_dictionary.keys())
    vs = list(a_dictionary.values())
    name, score = ks[0], vs[0]
    for i, j in zip(ks, vs):
        if score < j:
            score = j
            name = i
    return name
