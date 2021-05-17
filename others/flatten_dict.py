d = {'a': 1,
     'c': {'a': 2,
           'b': {'x': 5,
                 'y' : 10}},
     'd': [1, 2, 3]}


def flatten(d, parent_key=""):
    items = {}
    for k, v in d.items():
        if parent_key:
            new_key = parent_key + "_" + k
        else:
            new_key = k

        if isinstance(v, dict):
            cur_dict = flatten(v, new_key)
            items.update(cur_dict)
        else:
            items[new_key] = v
    return items


new_dict = flatten(d)
print(new_dict)
