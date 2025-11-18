def flatten_json(obj):
    ret = {}

    def flatten(x, flattened_key=""):
        if type(x) is dict:
            for current_key in x:
                flatten(x[current_key], flattened_key + current_key + ".")
        else:
            ret[flattened_key[:-1]] = x

    flatten(obj)
    return ret
