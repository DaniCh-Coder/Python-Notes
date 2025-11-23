class Person:
    """Simple Person class with name, job and pay attributes."""
    def __init__(self, name: str, job: str = None, pay: float = 0.0):
        self.name = name
        self.job = job
        self.pay = float(pay)

    # def __repr__(self):
    #    return f"Person(name={self.name!r}, job={self.job!r}, pay={self.pay!r})"

    def give_raise(self, percent: float):
        """Increase pay by percent (e.g., 10 for 10%)."""
        if percent:
            self.pay *= (1 + percent / 100)

    def last_name(self) -> str:
        """Return the last name part of full name."""
        return self.name.split()[-1] if self.name else ""

# python test code
if __name__ == "__main__":
    # self-test code 
    p = Person("Chris Jones", "dev", 50000)
    # print(repr(p))   # Person(name='Chris Jones', job='dev', pay=50000.0)
    print(p)         # same as repr() unless __str__ is defined separately
    
    # other way of creating an instantce of Person
    bob = Person(name="Bob Smith", job="dev", pay=60000)
    sue = Person(name="Sue Jones", job="hdw", pay=70000)
    
    print(bob.name, bob.pay)  # Bob Smith 60000.0
    print(sue.name, sue.pay)  # Sue Jones 70000.0
    print(repr(bob))          # Person(name='Bob Smith', job='dev', pay=60000.0)
    
    sue.give_raise(10)
    print(Person.__dir__)  # shows all attributes of Person class
    print(dir(sue))        # shows all attributes of sue instance
    
    

    