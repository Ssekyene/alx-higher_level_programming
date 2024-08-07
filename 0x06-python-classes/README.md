# Python - Classes and Objects
|File				|Description					|
|-----------------------|-----------------------------------------|
|0-square.py		|an empty class `Square` that defines a square|
|1-square.py		|a class `Square` that defines a square by; Private instance attribute: `size`; Instantiation with `size` |
|2-square.py		|a class `Square` that defines a square by `size` which is private field and must be an integer >= 0 |
|3-square.py		|a class `Square` that defines a square and clculates its area	|
|4-square.py		|a class `Square` that defines a square, sets and retrieves `size` which is a private field	|
|5-square.py		|a class `Square` that defines a square and prints in stdout the square with the character `#`	|
|6-square.py		|a class `Square` that defines a square with its `size` and `position`		|
|100-singly_linked_list.py |a class `Node` that defines a node of a singly linked list and  a class `SinglyLinkedList` that defines a singly linked list |
|101-square.py		|a class `Square` that defines a square and enables the class instances to be well formatted in `print()` with the same behavior as `my_print()`|
|102-square.py		|a class `Square` that defines a square and answers to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area	|

- 103-magic_class.py: Python class `MagicClass` that does exactly the same as the following [Python bytecode](https://docs.python.org/3.4/library/dis.html);

```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```
**Note:** The main.py files are for testing the respective module files they import eg `./2-main.py` tests `2-square.py`.
