# CLIF

Calling a function from the command-line in a type hint-aware manner.


## Quick start

Let's say we have a type-hinted function `add` in [`clif.demo`](clif/demo.py):
```python
def add(a: int, b: int) -> int:
    """
    Add two integers.

    Get the sum of two integers.

    :param a: Integer to be added.
    :param b: Integer to be added.

    :returns: Integer sum.
    """
    return a + b
```

Use `clif` to call the function from the command-line:
```bash
$ clif clif.demo.add 1 2
3
```

Use the help to see what the parameters and their types are:
```bash
$ clif clif.demo.add -h
usage: add [-h] a b

Add integers and return the sum.

positional arguments:
  a           int: Integer to be added.
  b           int: Integer to be added.

optional arguments:
  -h, --help  show this help message and exit
```

-------


> :warning: This package is experimental and not all complex types are implemented yet.


Another example with more complex types:

```python
from typing import Tuple

def represent_dot(pos: Tuple[float, float], name="point") -> int:
    return f"A Point '{name}' with coordinates '{pos[0]} -> {pos[1]}'"
```

```bash
$ clif package.module.represent_dot "(1.0, 2.5)"
"A Point 'point' with coordinates '1.0 -> 2.5'"

$ clif package.module.represent_dot "(0.0, 0.0)" origin
"A Point 'origin' with coordinates '0.0 -> 0.0'"
```

## Requirements and installation

Requires `Python >= 3.7`.

Install with `pip`:
```bash
pip install git+ssh://git@github.com/afrendeiro/clif.git
```
Make sure you have an up-to date version of `pip`.

<!--
## Documentation

Documentation is for now mostly a skeleton but will be enlarged soon:

```bash
make docs
```

## Testing

Tests are still very limited, but you can run tests this way:

```bash
python -m pytest --pyargs imc
```
-->
