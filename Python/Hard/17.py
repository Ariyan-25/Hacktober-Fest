class Animal:
 def __init__(self, name):
    self.name = name
 def __repr__(self):
    return f"Animal(name={self.name})"
dog = Animal('Rex')
print(dog)
