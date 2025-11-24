"""
Class general format.

class <name>(superclass):
    data = value
    def <method>(self, args):
        self.<attribute> = value
   """
   
# class example
class SharedData:
    data = 42

x = SharedData()
y = SharedData()

print(f"SharedData.data, x.data, y.data: {SharedData.data, x.data, y.data}")  # Output: (42, 42, 42)
x.data = 100
print(f"SharedData.data, x.data, y.data: {SharedData.data, x.data, y.data}")  # Output: (42, 100, 42) 
print("\n")

# Mixed Names implies different names in different scopes
class MixedNames:
    data = "class data"

    def __init__(self, value):
        self.data = value  # instance attribute
        print(f"Inside __init__: self.data = {self.data}, MixedNames.data = {MixedNames.data}")
        
        
obj = MixedNames("instance data")
print(f"Outside: object.data = {obj.data}, MixedNames.data = {MixedNames.data}")

print("That's all for now!")
  