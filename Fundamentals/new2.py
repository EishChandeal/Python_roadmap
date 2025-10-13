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

print()
try:
    print(10/0)
except Exception as e:
    print("This error: ", e, " \t occured!")
    print(e.args)
    print(type(e))


print("\n ***************** \n")
try:
    raise Exception("ramen", "noodles")
except Exception as inst:
    print(type(inst))
    print(inst.args)      # # __str__ allows args to be printed directly
    print(inst)
    a, b = inst.args
    print("a = ", a , "b = ", b)

print("\n ***************** \n")

