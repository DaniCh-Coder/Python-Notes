# Example showing purpose and advantages of the @property decorator in Python.
# Advantages demonstrated:
#  - clean attribute-style access for computed values
#  - validation on assignment
#  - keeping a stable public API while changing internals

class Temperature:
    def __init__(self, celsius: float):
        # use the property setter to validate on construction
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        # simple stored value (accessed like an attribute)
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        # validation: prevent temperature below absolute zero
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        # computed property, still accessed like an attribute
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, f_value: float) -> None:
        # setting fahrenheit updates internal celsius via conversion
        self.celsius = (f_value - 32) * 5 / 9

    @property
    def is_boiling(self) -> bool:
        # read-only computed boolean property
        return self.celsius >= 100.0


# Usage examples:

t = Temperature(25.0)
print("Celsius:", t.celsius)          # 25.0
print("Fahrenheit:", t.fahrenheit)    # 77.0
print("Boiling?", t.is_boiling)       # False

# Change via fahrenheit property (transparent conversion)
t.fahrenheit = 212.0
print("After setting fahrenheit=212 -> Celsius:", t.celsius)  # 100.0
print("Boiling now?", t.is_boiling)                          # True

# Validation enforced by setter
try:
    t.celsius = -300
except ValueError as e:
    print("Validation error:", e)  # blocked: below absolute zero

# Read-only property example: assignment to is_boiling raises AttributeError
try:
    t.is_boiling = False
except AttributeError as e:
    print("Can't assign to read-only property:", e)