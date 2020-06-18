# CLIF

A simple decorator for calling a function from the command-line in a type hinting-aware manner.


> :warning: This package is experimental and not all features are working.


## Quick start

Decorate function `add` in package.module:
```python
from clif import clif

@clif
def add(a: int, b: int) -> int:
    return a + b
```

Call it from the command-line:
```bash
$ python -m package.module.add 1 1
2
```

-------

Another example with more complex types:

```python
from typing import Tuple
from clif import clif

@clif
def represent_dot(pos: Tuple[float, float], name="point") -> int:
    return f"A Point '{name}' with coordinates '{pos[0]} -> {pos[1]}'"
```

```bash
$ python -m package.module.represent_dot "(1.0, 2.5)"
"A Point 'point' with coordinates '1.0 -> 2.5'"

$ python -m package.module.represent_dot "(0.0, 0.0)" origin
"A Point 'origin' with coordinates '0.0 -> 0.0'"
```

## Requirements and installation

Requires `Python >= 3.7`.

Install with `pip`:
```bash
pip install git+ssh://git@github.com/afrendeiro/clif.git
```
Make sure you have an up-to date version of `pip`.

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
