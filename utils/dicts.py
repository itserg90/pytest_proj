def get_val(collection, key, default='git'):
    if not collection or key not in collection:
        return default
    return collection[key]