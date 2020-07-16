# -*- encoding: utf-8 -*-
# !/usr/bin/python3.7

"""Some helper functions."""

def get_value_if_not_none(value, get_value=lambda value: value, default_value=None):
    """
    Check if `value` is `None` and calls `get_value` if not.

    Arguments:
        value {[type]} -- the value which should be checked.

    Keyword Arguments:
        get_value {lambda} -- function which will be called if value is not None.
            (default: {lambda value:value})
        default_value -- return value if value is None. (default: {None})

    Returns:
        [type] -- returns the result of get_value or default_value if value is None.
    """
    return get_value(value) if value != None else default_value

def first_or_none(items, condition=lambda item: True):
    """
    Return the first item where result of `condition` is `True`.
    If no entry match the condition or the list is `None` the result will be None too.

    Arguments:
        items {[type]} -- List of elements which should be checked.

    Keyword Arguments:
        condition {[type]} -- unction which check if item is valid. (default: {lambda item:True})

    Returns:
        [type] -- First entry of items which passed the condition.
    """
    if not items:
        return None

    for item in items:
        if condition(item):
            return item

    return None
