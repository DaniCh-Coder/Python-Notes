"""
properties_and_setters_demo.py

This module explains:

1) What @property does in its simplest form.
   - It turns a method into a read-only *computed attribute*.
   - It is used without parentheses: obj.attribute instead of obj.method().

2) Why @property is useful:
   - To represent attributes that are derived from other attributes (computed attributes).
   - To keep code natural and expressive: obj.area instead of obj.get_area().
   - To avoid storing redundant state: only base attributes are stored, the property is computed.

3) What @<name>.setter does:
   - It connects an assignment like obj.attribute = value to a *setter method*.
   - That setter method can validate, normalize or transform the value before storing it.
   - It is always associated with an existing @property of the same name.

The examples below are:

- Rectangle: shows a read-only computed property (area) with @property only.
- Person: shows a read-write property (age) with @property + @age.setter.
"""


class Rectangle:
    """Rectangle with width and height, and a computed read-only area property."""

    def __init__(self, width: float, height: float) -> None:
        # These are the real stored attributes.
        # They live in the instance dictionary as plain data.
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        """
        Computed property.

        This method is decorated with @property, which means:
        - From the outside, it is used as if it were an attribute: r.area
        - Internally, Python calls this method (area(self)) each time r.area is read.
        - No value named "area" is stored on the instance; the value is computed on demand.
        """
        return self.width * self.height


class Person:
    """
    Person with an internal _age attribute and a public age property.

    Here we show:
    - @property: defines how age is *read* (the getter).
    - @age.setter: defines how age is *assigned* (the setter), with validation.
    """

    def __init__(self, age: int) -> None:
        # Internal storage for age.
        # By convention, the leading underscore means "internal use".
        self._age: int | None = None

        # This line does NOT write directly to _age.
        # Instead, it calls the property setter defined below (age.setter).
        self.age = age

    @property
    def age(self) -> int:
        """
        Property getter for age.

        When client code does:

            value = p.age

        Python executes this method internally and returns its result.

        Notice:
        - From the outside, p.age *looks* like a normal attribute.
        - In reality, reading p.age is a function call to this getter.
        """
        return self._age  # type: ignore[return-value]

    @age.setter
    def age(self, value: int) -> None:
        """
        Property setter for age.

        When client code does:

            p.age = value

        Python does NOT assign directly to p.__dict__["age"].
        Instead, Python calls this method:

            Person.age.__set__(p, value)

        which is wired to this function by the @age.setter decorator.

        This is the place where we can:
        - Validate the value.
        - Normalize or transform it.
        - Decide what to store internally.

        In this example, we simply check that the age is not negative and
        then store it in the internal attribute self._age.
        """
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


if __name__ == "__main__":
    # --- Rectangle example: @property as a read-only computed attribute ---

    r = Rectangle(2, 3)

    # These are real stored attributes.
    print("Rectangle width:", r.width)    # 2
    print("Rectangle height:", r.height)  # 3

    # area is NOT stored; it is computed each time through the @property method.
    print("Rectangle area:", r.area)      # 6 (no parentheses, looks like a normal attribute)

    # If we change width, area will be recomputed the next time we read r.area.
    r.width = 10
    print("Rectangle area after width change:", r.area)  # 30

    # --- Person example: @property + @age.setter for controlled assignment ---

    p = Person(30)

    # Reading p.age uses the getter (the @property method).
    print("Person age:", p.age)  # 30

    # Assigning to p.age uses the setter (the @age.setter method).
    p.age = 40
    print("Person age after update:", p.age)  # 40

    # This would trigger the validation in the setter and raise ValueError:
    # p.age = -5
