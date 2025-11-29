"""
File: classmethod_examples.py

Purpose:
- Explain what a class and static methods is in Python.
- Provide concise examples and common use cases:
    1. Alternative constructors (factory methods)
    2. Accessing/modifying class-level state
    3. Polymorphic constructors with inheritance

Definition (short):
- A class method is a method bound to the class, not the instance.
- It receives the class as the first argument (conventionally named `cls`).
- Declared with the decorator: @classmethod
"""

from typing import Dict


class Person:
        # Class-level attribute (shared by all instances of Person and subclasses)
        species = "Homo sapiens"

        def __init__(self, name: str, age: int) -> None:
                self.name = name
                self.age = age

        def info(self) -> str:
                return f"{self.name}, {self.age} years old, species={self.species}"

        # 1) Alternative constructor / factory method: creates an instance from a string
        @classmethod
        def from_string(cls, data: str):
                # data expected in "Name-Age" format, e.g. "Alice-30"
                name, age_str = data.split("-")
                return cls(name, int(age_str))  # returns an instance of the class that called it

        # 2) Class method that modifies class state shared across instances
        @classmethod
        def set_species(cls, new_species: str) -> None:
                cls.species = new_species

        # 3) Example of a utility that doesn't need class or instance: staticmethod is more appropriate
        @staticmethod
        def is_adult(age: int) -> bool:
                return age >= 18


# Subclass to show polymorphic behavior of classmethod
class Employee(Person):
        def __init__(self, name: str, age: int, employee_id: str) -> None:
                super().__init__(name, age)
                self.employee_id = employee_id

        def info(self) -> str:
                return f"{self.name}, {self.age} y/o, id={self.employee_id}, species={self.species}"

        # Keep the same from_string format but include a fake employee id for demonstration
        @classmethod
        def from_string(cls, data: str):
                # Demonstrates that cls refers to the subclass when called on Employee
                person = super().from_string(data)  # this returns an instance of cls because Person.from_string uses cls
                # If super().from_string returned a Person, we'd convert; but because Person.from_string uses cls, we get correct type
                # Create an Employee instance using values from person
                return cls(person.name, person.age, employee_id="E-000")


if __name__ == "__main__":
        # Using Person alternative constructor
        p = Person.from_string("Alice-30")
        print(p.info())  # Alice, 30 years old, species=Homo sapiens

        # Using class method on subclass returns subclass instance (polymorphic factory)
        e = Employee.from_string("Bob-40")
        print(type(e).__name__, "-", e.info())  # Employee - Bob, 40 y/o, id=E-000, species=Homo sapiens

        # Class-level change reflected across instances and subclasses
        Person.set_species("Homo exemplar")
        print(p.info())       # species changed
        print(e.info())       # subclass sees the same class attribute (inherited)

        # Demonstrate staticmethod vs classmethod vs instance method
        print("Is 17 adult?", Person.is_adult(17))  # static utility, no cls or self needed
        print("Is 21 adult?", e.is_adult(21))       # callable from instance too

        # Showing that from_string called on Person returns Person, on Employee returns Employee
        p2 = Person.from_string("Carol-22")
        e2 = Employee.from_string("Dana-28")
        print(f"p2 type: {type(p2).__name__}, e2 type: {type(e2).__name__}")

"""
Key takeaways (short):
- Use @classmethod when you need a method that acts on the class itself (cls) rather than an instance (self).
- Common use cases: alternative constructors and class-level configuration or factories that should work correctly with subclasses.
- If you don't need cls or self, prefer @staticmethod. If you need instance data, use a normal instance method.
"""