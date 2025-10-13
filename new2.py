class B(Exception):
    pass
class D(B):
    pass
class C(D):
    pass

for cls in [D,B, C]:
    try:
        raise cls()
    except C:
        print("C")
    except D:
        print("D")
    except B:
        print("B")

'''
A class in an except clause matches exceptions which are instances of the class itself 
or one of its derived classes (but not the other way around — an except clause listing 
a derived class does not match instances of its base classes). 
'''

