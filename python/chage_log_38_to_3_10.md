# Python Version Changes: 3.8 to 3.10

This document outlines the major changes and new features introduced between Python 3.8 and Python 3.10.

## New Features and Enhancements

### Python 3.9

1. **Dictionary Merge & Update Operators**
   ```python
   a = {'key1': 'value1'}
   b = {'key2': 'value2'}
   c = a | b  # {'key1': 'value1', 'key2': 'value2'}

2. **String Methods for Removing Prefixes and Suffixes**
```s = "HelloWorld"
s.removeprefix("Hello")  # 'World'
s.removesuffix("World")  # 'Hello'
```

3. **Type Hinting Generics in Standard Collections**
```
def greet(names: list[str]) -> None:
    for name in names:
        print(f"Hello, {name}")
```

4. **New Parser (PEG)**
 -- Python 3.9 introduced a new parser based on PEG (Parsing Expression Grammar), which aims to improve performance and maintainability.

#Python 3.10
1. **Pattern Matching**
```def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```
2. **Parenthesized Context Managers**

```
with (open('file1.txt') as f1, 
      open('file2.txt') as f2):
    pass
```
3. **Precise Syntax Errors**

``` # Before
#   File "<stdin>", line 1
#     x = (1, 2, 3
#                ^
# SyntaxError: unexpected EOF while parsing

# After
#   File "<stdin>", line 1
#     x = (1, 2, 3
#          ^
# SyntaxError: '(' was never closed ```

5. **Type Hints Enhancements**
-Union Types

```def foo(x: int | str) -> None:
    pass
```
-Parameter Specification Variables
```from typing import Callable, TypeVar, ParamSpec

P = ParamSpec('P')
R = TypeVar('R')

def logged(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper
```

5. **str Enum Members**

```from enum import Enum

class Color(str, Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

print(Color.RED)  # Output: Color.RED
print(Color.RED.value)  # Output: 'red'

```
#Deprecations and Removals

1. **Removal of __import__() Function**
```import importlib

module = importlib.import_module('module_name')

```
2. **Removed collections ABCs in Favor of collections.abc**
```from collections.abc import MutableMapping

```

3. **Removed isAlive Method**
-The isAlive method of threading.Thread has been removed in favor of is_alive.



