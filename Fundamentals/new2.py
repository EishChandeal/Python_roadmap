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

import sys

try: 
    file = open('../Files/new.txt')
    line = file.readline()
    l = line.strip()
except OSError as o:
    print(f"{o} just occured! ")
except ValueError as v:
    print(f"could not convert the value, {v} \t occured!")
except Exception as e:
    print(f"unexpected {e=} , {type(e)=}")
    raise

print("\n ***************** \n")

for arg in sys.argv[1:]:
    try:
        f  = open(arg , "r")
    except OSError:
        print(f" cannot open arg: {arg}")
    else:
        print(arg, "has length: ", len(f.readlines()), 'lines')
        f.close()

print(sys.argv[0])