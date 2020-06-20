# Creational Patterns

## Factory 

class Cat:
    """A simple cat class"""
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "moew"
    
class Dog:
    """A simple dog class"""
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "bark"
    
def get_pet(pet="dog"):
    """The factory method"""
    fact = dict(dog=Dog("Bob"), cat=Cat("Peace"))
    return fact[pet]
    
        
a = get_pet("dog")
a.speak()
a._name

b = get_pet("cat")
b.speak()
b._name