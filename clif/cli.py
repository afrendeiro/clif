#!/usr/bin/env python

"""
A type hinting aware package for calling a function from the command-line.
"""


import re
import sys
import argparse
from importlib import import_module
from typing import Callable, Dict, Union
from inspect import signature, _empty as empty

from clif.docstring import parse_docstring


TYPE_REPRS = {"": "", int: "int", float: "float", list: "list", set: "set"}


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=__name__, description=__doc__, add_help=False)

    _help = "The function to be called. Try for example 'clif.add'."
    parser.add_argument(dest="function", help=_help)
    return parser


def get_function_metadata(function: Callable) -> Dict:
    meta = dict()
    meta["params"] = signature(function).parameters
    # types = typing.get_type_hints(function)

    meta["name"] = function.__name__
    doc = parse_docstring(function.__doc__)
    doc["params"] = {p["name"]: p["doc"].strip() for p in doc["params"]}
    meta["docstring"] = doc
    return meta


def build_cli(parser, meta) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=meta["name"], description=meta["docstring"]["long_description"]
    )

    for arg, param in meta["params"].items():
        cliarg = arg.replace("_", "-")
        kwargs = dict()
        for p, v in [("default", "default"), ("annotation", "type")]:
            _p = getattr(param, p)
            if _p is not empty:
                kwargs[v] = _p

        # check if positional only (this should be taken into account later calling the func)

        # if type hint is not available, get type of default argument if available

        # parse complex types into a str

        # add cli option
        args = [f"-{cliarg[0]}", f"--{cliarg}"] if "default" in kwargs else []
        # # add type first
        desc = kwargs.get("type", str).__name__ + ": "
        desc += meta["docstring"]["params"][arg]
        parser.add_argument(*args, help=desc, dest=arg, **kwargs)
    return parser


def main() -> int:
    parser = get_parser()
    args, f_args = parser.parse_known_intermixed_args()

    # Manually handle help in order to allow help of function being called

    module = ".".join(args.function.split(".")[:-1])
    function_name = args.function.split(".")[-1]
    try:
        function = getattr(import_module(module), function_name)
        metadata = get_function_metadata(function)
    except TypeError:
        return parser.error("`function` argument points to module and not function.")
    except ValueError:
        return parser.error("Cannot find module/function: '" + function_name + "'")

    f_parser = build_cli(parser, metadata)
    r_args = f_parser.parse_args(f_args).__dict__

    # if any([a in r_args for a in ["-h", "--help"]]):
    #     f_parser.print_help()
    #     return 1
    # coherce the
    res = function(**r_args)

    # If the result is a simple type, print it out to sys.stdout
    print(res)
    return 0


if __name__ == "__name__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(1)
