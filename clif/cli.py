#!/usr/bin/env python

"""
A simple type hint aware package for calling a function from the command-line.
"""

import sys
import argparse
from functools import wraps
from typing import Callable, NoReturn
from inspect import signature, _empty as empty


def clif(function: Callable) -> Callable:
    """
    The main clif decorator - make any function callable from the command line.
    """

    @wraps(function)
    def inner() -> NoReturn:
        """
        1. Get function signature, argument types and docstring.
        2. Make argparse.ArgumentParser with those.
        3. Parser the args from CLI.
        4. Run the function.
        5. Terminate program.
        """
        params = signature(function).parameters
        # types = typing.get_type_hints(function)

        name = function.__name__
        docstring = function.__doc__
        # Parse docstring to extract argument description
        descriptors = {k: "" for k in docstring.split()} if docstring is not None else {}

        parser = argparse.ArgumentParser(prog=name, description=docstring)

        for arg, param in params.items():
            cliarg = arg.replace("_", "-")
            kwargs = dict()
            for p, v in [("default", "default"), ("annotation", "type")]:
                _p = getattr(param, p)
                if _p is not empty:
                    kwargs[v] = _p

            # parse complex types into a str

            args = [f"-{cliarg[0]}", f"--{cliarg}"] if "default" in kwargs else []
            desc = descriptors[arg]
            parser.add_argument(*args, description=desc, dest=arg, **kwargs)

        kwargs = parser.parse_args().__dict__

        # parse the simple string arguemnts to their complex types

        function(**kwargs)

        sys.exit(0)

    return inner
