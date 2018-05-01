#!/usr/bin/python3

class argument:
    def __init__(
        self,
        short_arg_key: str,
        long_arg_key: str,
        is_mandatory: bool,
        description: str
    ):
        self.short_arg_key = short_arg_key
        self.long_arg_key = long_arg_key
        self.is_mandatory = is_mandatory
        self.description = description
