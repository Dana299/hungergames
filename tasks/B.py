def make_dict(list1: list, list2: list):
    """Return dict where keys are the elements of list1 and values are the elements of list2."""
    res = {key: value for key, value in zip(list1, list2)}
    return dict(sorted(res.items()))
