# Inheritance Overload Interface Techniques
"""
This file contains exercises that define multiple classes that illustrate a variety of common technique to overload inheritaed atrributes
"""
class Base:
    def greet(self):
        return "Hello from Base"
class DerivedA(Base):
    def greet(self):
        return "Hello from DerivedA"
class DerivedB(Base):
    def greet(self):
        return "Hello from DerivedB"
class MultiDerived(DerivedA, DerivedB):
    def greet(self):
        return "Hello from MultiDerived"
# Testing the classes
if __name__ == "__main__":
    base = Base()
    derived_a = DerivedA()
    derived_b = DerivedB()
    multi_derived = MultiDerived()

    print(base.greet())          # Output: Hello from Base
    print(derived_a.greet())     # Output: Hello from DerivedA
    print(derived_b.greet())     # Output: Hello from DerivedB
    print(multi_derived.greet()) # Output: Hello from MultiDerived
# This script demonstrates different techniques for overloading inherited attributes through class inheritance
# and method overriding in Python.
# It defines a base class and multiple derived classes that override the greet method to provide specific implementations.

class Super:
    def info(self):
        return "Info from Super"
    def delegate(self):
        return self.action()
    
class Iheritor(Super):
    pass
    

class Overloader(Super):
    def info(self):
        return "Info from Overloader"
    
class Customizer(Super):
    def info(self):
        base_info = super().info()
        return f"{base_info} - Customized in Customizer"

class Provider(Super):
    def info(self):
        return "Info from Provider"
    def action(self):
        return "Action performed by Provider but call by Super.delegate()"


class Combiner(Iheritor, Overloader, Customizer):
    def info(self):
        return "Info from Combiner"
    super_instance = Super()
    def combined_info(self):
        info_parts = [
            self.super_instance.info(),
            Iheritor().info(),
            Overloader().info(),
            Customizer().info(),
            self.info()
        ]
        return " | ".join(info_parts)  


# Testing the additional classes
if __name__ == "__main__":
    for klass in (Super, Iheritor, Overloader, Customizer, Provider, Combiner):
        instance = klass()
        print(f"{klass.__name__}: {instance.info()}")
        
# Special test for Provider's delegate method
    provider = Provider()
    print(f"Provider Delegate Action: {provider.delegate()}")
    
# Special test for Combiner's combined_info method
combiner = Combiner()
print(f"Combiner Combined Info: {combiner.combined_info()}")

print("All classes tested successfully.")
# This additional code defines more classes that illustrate different inheritance overload techniques,
