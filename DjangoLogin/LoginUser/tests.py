from django.test import TestCase
# list1=data[data]
# list1={"1":[{1:"a"},{2:"b"}]}
# for i in list1["1"]:
#     print(i)
#     # c=list1[i]

# def add(x):
# #     return x+3
# # map=map(add,[1,2,3])
# # print(list(map))

# def add(x,y):
#     return x+y
# from functools import reduce
# ax=reduce(add,[1,2,3,4,5])
# print(ax)

def fil(x):
    return x%3
xb=filter(fil,[1,2,3,4,5])
print(list(xb))


# Create your tests here.
