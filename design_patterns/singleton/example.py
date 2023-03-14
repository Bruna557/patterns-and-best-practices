"""
The Singleton Pattern ensures that a class has only one instance and provides
global point of access to it.
"""
class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

s1 = SingletonClass()
s2 = SingletonClass()

print(s1 is s2)

s1.some_variable = "some value"
print(s2.some_variable)
