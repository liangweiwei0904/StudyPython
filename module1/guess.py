import numpy
# import torch

x = numpy.random.randint(0,100)
# y = torch.randint(0,100,(1,))
# print(x,int(y.data))
y = int(input("input a number:"))
# if x == y :
#     print("win!")
# elif y < x :
#     y = input("small")
# else:
#     y = input("big")
while x!=y:
    if y<x :
        y = int(input("small"))
    else :
        y = int(input("big"))
print("you win!")
