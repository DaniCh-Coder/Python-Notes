# Encapsulation Principle
"""
Idea: group data and behavior that are related within the same unit (class/object) and hide the internal details, exposing only what is necessary. 

An object maintains internal state (attributes). 

That state is managed through methods. 

From the "outside" the object's public interface is used, not its guts. 

In Python encapsulation is more by convention than by language restriction: 

"Public" attributes: self.name 

"Internal" or for internal use: _nombre or __nombre (convention, not an absolute wall). 
"""

class BankAccount:
    """Simple bank account with basic encapsulation."""

    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner              # public attribute
        self._balance = initial_balance # internal detail by convention

    def deposit(self, amount: float) -> None:
        """Increase balance by amount."""
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Decrease balance if enough funds are available."""
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self) -> float:
        """Return current balance (public way to read internal state)."""
        return self._balance

# Example usage
if __name__ == "__main__":  
    account = BankAccount("Alice", 100.0)
    account.deposit(50.0)
    print(f"Balance after deposit: {account.get_balance()}")
    account.withdraw(30.0)
    print(f"Balance after withdrawal: {account.get_balance()}")
    # Direct access to _balance is discouraged
    # print(account._balance)  # Not recommended

"""
What does the underscore mean?
In general, there are three levels of visibility in Python, by convention:
1 Public (Stable API):
    1.	balance, deposit, withdraw
    2.	No low score at the beginning.
    3.	It is considered part of the "official interface" of the class/module.
2 Internal / "protected" by convention:
    1.	_balance, _helper_method
    2.	Signifies:
        	"This is an internal detail. I can change it in a future version without telling you."
    3.	Used at:
        1.	Class Attributes/Methods
        2.	Module Functions/Variables (_helper_function)
3.	Pseudo-private / name mangling:
    1.	__balance inside the classroom.
    2.	Python lo manglea a _BankAccount__balance.
    3.	It serves to avoid collisions of names in inheritance, and to make accidental access difficult.
"""