# In This Project we will learn use of Various operators in python

# 01)Arithmetic operators: +, -, *, / etc
a = 10
b = a+20
c = b-10
d = c*2
e = d/4
print("\n", "a =", a, "\n", "b =", b, "\n", "c =", c, "\n", "d =", d, "\n", "e =", int(e))

# 02)Assignment operators: =, +=, -= etc.
f = 5
f += 3  # equivalent to f = f + 3
print("\n", "f =", f)
g = 10
g -= 2  # equivalent to g = g - 2
print("\n", "g =", g)

# 03)Comparison operators: ==, !=, >, <, >=, <=
h = 15
print(h==15) # True
print(h!=10) # True
print(h<10) # False
print(h>10) #True
print(h<=10) # False
print(h>=10) #True

# 04)Logical operators: and, or, not.
# Truth Table Of Or
print("True or False Is " , True or False)
print("True or True Is " , True or True)
print("False or True Is " , False or True)
print("False or False Is " , False or False)

# Truth Table Of and
print("True and False Is " , True and False)
print("True and True Is " , True and True)
print("False and True Is " , False and True)
print("False and False Is " , False and False)

print(not(False))
print(not(True))