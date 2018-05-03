#!/usr/bin/python3
"""Convert arguments."""

import re
from typing import List
import itertools

from helper import utils
from converter.argument import argument

def get_clean_argument_value(args: List[str], argument: argument) -> str:
    """Combination of `get_argument` and `remove_argument_prefix`.

    Arguments:
        args {List[str]} -- List of arguments.
        argument {argument} -- Argument which will be used for matching.

    Returns:
        str -- The full argument value which matched the short or the long argument prefix.
    """
    return remove_argument_prefix(get_argument(args, argument), argument)

def get_argument(args: List[str], argument: argument) -> str:
    """Check if the argument match one entry inside the `args` list.

    Arguments:
        args {List[str]} -- List of arguments.
        argument {argument} -- Argument which will be used for matching.

    Returns:
        str -- The full argument value which matched the short or the long argument prefix.
    """
    return get_argument_base(args, argument.short_arg_key, argument.long_arg_key)

def get_argument_base(args: List[str], short_arg: str, long_arg: str) -> str:
    """Basic function to check if the short or the long argument is inside the args list
    and return the full matching argument.

    Arguments:
        args {List[str]} -- List of arguments.
        short_arg {str} -- The short prefix of the searched argument.
        long_arg {str} -- The long prefix of the searched argument.

    Returns:
        str -- The full argument value which matched the short or the long argument prefix.
    """
    if not args:
        return None

    short_arg = short_arg.lower()
    long_arg = long_arg.lower()
    result = utils.first_or_none(
        args,
        lambda arg: arg.lower().startswith(short_arg) or arg.lower().startswith(long_arg)
    )
    return result

def remove_argument_prefix(arg: str, argument: argument) -> str:
    """Removes the prefix of the argument.

    Arguments:
        arg {str} -- Argument with prefix.
        argument {argument} -- Argument object with short and long prefix information.

    Returns:
        str -- Clean argument value.
    """
    return remove_argument_prefix_base(arg, argument.short_arg_key, argument.long_arg_key)

def remove_argument_prefix_base(arg: str, short_arg: str, long_arg: str) -> str:
    """Removes the prefix of the argument.

    Arguments:
        arg {str} -- Argument with prefix.
        short_arg {str} -- Short prefix which should be removed.
        long_arg {str} -- Long prefix which should be removed.

    Returns:
        str -- Clean argument value.
    """
    if not arg or not short_arg or not long_arg:
        return None

    cleared_short_arg = short_arg.lower().replace(' ', '')
    cleared_long_arg = long_arg.lower().replace(' ', '')

    regular_expression = '^{0}\\s+|^{1}\\s+'.format(cleared_short_arg, cleared_long_arg)
    return re.sub(regular_expression, '', arg)

def valid_argument_text(args: List[argument]) -> str:
    """Create a text with all valid arguments.

    Arguments:
        args {List[argument]} -- List with valid arguments.

    Returns:
        str -- Text with valid arguments.
    """
    sorted_args = sorted(args, key=lambda arg: len(arg.short_arg_key), reverse=True)
    first_arg = utils.first_or_none(sorted_args)
    arg_short_key_len = len(first_arg.short_arg_key)

    sorted_args = sorted(args, key=lambda arg: len(arg.long_arg_key), reverse=True)
    first_arg = utils.first_or_none(sorted_args)
    arg_long_key_len = len(first_arg.long_arg_key)

    result = ''
    for arg in args:
        short_arg_key_format = '{:' + str(arg_short_key_len) + 's}'
        long_arg_key_format = '{:' + str(arg_long_key_len) + 's}'
        result += '{0}    {1}    Mandatory:{2:5s}    {3}\n'.format(
            short_arg_key_format.format(arg.short_arg_key),
            long_arg_key_format.format(arg.long_arg_key),
            str(arg.is_mandatory),
            arg.description
        )

    return result
