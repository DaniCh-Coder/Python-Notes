class Person:
    """
        Simple Person class with name, job and pay attributes.
        Class Manager will inherit from this class and augment give_raise method.
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
    
class Manager(Person):
    """A Manager is a Person with special give_raise behavior."""
    def give_raise(self, percent: float, bonus: float = 15):
        """Increase pay by percent plus bonus."""
        total_increase = percent + bonus
        super().give_raise(total_increase)
    
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
    dani = Manager(name="Dani", job="mgr", pay=100000)
    
# Polimorphism in action
    for obj in (p, bob, sue, dani):
        obj.give_raise(10)  # all objects respond to give_raise
        print(f"{obj.name}: {obj.pay}")    
    print("That's all!")
    
    

    