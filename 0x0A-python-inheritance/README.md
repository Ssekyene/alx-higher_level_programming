# 0x0A. Python - Inheritance

|File				|Description					|
|-----------------------|-----------------------------------------|
|0-lookup.py		| a function that returns the list of available attributes and methods of an object|
|1-my_list.py, tests/1-my_list.txt|a class MyList that inherits from list	|
|2-is_same_class.py	|a function that returns `True` if the object is _exactly_ an instance of the specified class ; otherwise `False`|
|3-is_kind_of_class.py	|a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False` |
|4-inherits_from.py	|a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`. In simple terms returns `True` when the object is only a sub class of the specified class |
|5-base_geometry.py	|an empty class `BaseGeometry`	|
|6-base_geometry.py	|a class `BaseGeometry` with instance method: `def area(self):`	|
|7-base_geometry.py, tests/7-base_geometry.txt|a class `BaseGeometry` with `def integer_validator(self, name, value):` that validates `value` |
|8-rectangle.py		|a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`) with instantiation of `width` and `height`: `def __init__(self, width, height):` |
|9-rectangle.py		|a class Rectangle that inherits from BaseGeometry (7-base_geometry.py) with `area()` and `__str()__` methods implemented	|
|10-square.py		|a class `Square` that inherits from `Rectangle` (`9-rectangle.py`) with instantiation of  `size`: `def __init__(self, size):` |
|11-square.py		|a class `Square` that inherits from `Rectangle` (`9-rectangle.py`) with `__str()__` implemented	|
|100-my_int.py		|a class `MyInt` that inherits from `int`. `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted |
|101-add_attribute.py	|a function that adds a new attribute to an object if it’s possible	|
