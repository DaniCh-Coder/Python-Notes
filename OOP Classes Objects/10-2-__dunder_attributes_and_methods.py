class Person:
    """
        Simple Person class with name, job and pay attributes.
        Note that __str__ method is defined here to provide an example of overloading.
    """
    def __init__(self, name: str, job: str = None, pay: float = 0.0):
        self.name = name
        self.job = job
        self.pay = float(pay)

    def give_raise(self, percent: float):
        """Increase pay by percent (e.g., 10 for 10%)."""
        if percent:  # type: ignore # noqa: F821
            self.pay *= (1 + percent / 100)

    def last_name(self) -> str:
        """Return the last name part of full name."""
        return self.name.split()[-1] if self.name else ""
    
    def __str__(self):
        """Return a user-friendly string representation of the Person."""
        return f"Person(name={self.name!r}, job={self.job!r}, pay={self.pay!r})"
    
    # note: __repr__ can be defined similarly if needed but is omitted here on purpose

# python test code
if __name__ == "__main__":
    # self-test code 
    p = Person("Chris Jones", "dev", 50000)
    # print(repr(p))   # Person(name='Chris Jones', job='dev', pay=50000.0)
    print(p)         # same as repr() unless __str__ is defined separately
    
    # other way of creating an instantce of Person
    bob = Person(name="Bob Smith", job="dev", pay=60000)
    sue = Person(name="Sue Jones", job="hdw", pay=70000)
    

    print(sue.name, sue.pay)  # Sue Jones 70000.0
    print(repr(bob))          # Person(name='Bob Smith', job='dev', pay=60000.0)
    print(str(bob))           # same as repr() unless __str__ is defined separately
    
    
    

    