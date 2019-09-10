from django.test import TestCase

# Create your tests here.
# class Acx():
#
#     def Xcd(self):
#         self.a=1
#         self.b=2
#
#
#     def Xdd(self):
#        self.a
#
#
# print( Xcd() )

# def hi(name="yasoob"):
#     return "hi " + name
#
#
# print(hi())
#
# greet = hi
#
# print(greet())

import copy
a=[1,2,3,4,5,[6,7,8,9]]
b=a.copy()
c=copy.deepcopy(a)
a.remove(3)
# a.append(10)
print(id(a),a)
print(id(b),b)
print(id(c),c)
print(id(3))
print(id(3))

print(id("3"))
print(id("3"))