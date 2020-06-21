class British:
    """English Speaker"""
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"


class Korean:
    """Korean Speaker"""
    def __init__(self):
        self.name = "British"

    def speak_korean(self):
        return "An-neyong?"


class Adapter:
    def __init__(self, objects, **adapted_method):
        self._object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


british = British()
adapter = Adapter(british, speak=british.speak_english)
print(adapter.speak())

korean = Korean()
adapter2 = Adapter(korean, speak=korean.speak_korean)
print(adapter2.speak())