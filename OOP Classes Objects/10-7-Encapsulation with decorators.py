
"""
encapsulation_example.py

Concise examples demonstrating encapsulation in Python:
- public attributes (no protection)
- protected attributes (convention: single underscore)
- private attributes (name mangling: double underscore)
- property getters/setters for controlled access and validation
- subclass behavior
"""
from dataclasses import dataclass


# Public attributes: no access control; easy but unsafe
@dataclass
class UserPublic:
    username: str
    email: str


# Protected attribute (convention): "internal use" but still accessible
class Person:
    def __init__(self, name: str, age: int):
        self.name = name        # public
        self._age = None        # protected convention
        self.age = age          # use setter for validation

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("age must be a non-negative integer")
        self._age = value


# Private attribute with name mangling this prevents accidental access
class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.__balance = 0.0           # private: name-mangled to _BankAccount__balance
        if initial_balance:
            self.deposit(initial_balance)

    # read-only property exposing balance safely
    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance -= amount


# Subclass demonstrating protected vs private behavior
class SavingsAccount(BankAccount):
    def apply_interest(self, rate: float):
        # Cannot access __balance directly because of name mangling in parent
        # self.__balance += self.__balance * rate  # would raise AttributeError
        # But can use public API (good encapsulation)
        if rate < 0:
            raise ValueError("rate must be non-negative")
        new_balance = self.balance * (1 + rate)
        # Update via deposit/withdraw to preserve parent class invariants
        self.deposit(new_balance - self.balance)


if __name__ == "__main__":
    # Public example: no enforcement
    u = UserPublic("alice", "alice@example.com")
    u.email = "hacked@example.com"   # nothing stops this

    # Protected: convention-based, validated via property
    p = Person("Bob", 30)
    print(f"{p.name} is {p.age} years old")
    try:
        p.age = -5
    except ValueError as e:
        print("Protecting invariants for Person.age:", e)

    # Private: controlled via methods / properties
    acct = BankAccount("Chris", 100)
    acct.deposit(50)
    acct.withdraw(25)
    print(f"{acct.owner} balance (property): {acct.balance}")

    # Attempt direct access to private attribute fails normally
    try:
        print(acct.__balance)  # AttributeError
    except AttributeError:
        print("Direct access to __balance prevented (AttributeError).")

    # But name mangling allows access if you really want to break encapsulation:
    print("Access via name-mangling (discouraged):", acct._BankAccount__balance)

    # Subclass uses public API to modify balance
    s = SavingsAccount("Dana", 100)
    s.apply_interest(0.05)
    print("Savings account balance after 5% interest:", s.balance)