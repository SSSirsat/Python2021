import numpy as np
# x = range(16)
#
# x= np.reshape(x,(4,4))
# print(x)
# print("Shape", x.shape)
#
# #
# list1 = [[1,4,56,8],[85,6,9,66]]
# print("List 1: ", list1)
#
# y = np.array(list1)
#
# print("Y Matrix: \n", y)
#
# import matplotlib.pyplot as plt
# x = np.arange(0,3*np.pi, 0.8)
# y=np.cosh(x)
# plt.plot(x,y)
# plt.show()

M = [[2,3],[4,5]]
M=np.array(M)
C=[[20],[30]]
C =  np.array(C)
print("The Corfficient Matrix of C is :\n", M)
print("The Corfficient Matrix of C is :\n", C)

det_M = np.linalg.det(M)
print("Detrnament of Coefficient Matrix is :\n",det_M)

Inv_M= np.linalg.inv(M)
print("Inverse if Matrix M is ;\n", Inv_M)

sol_M= Inv_M@C
print("Soluction for the linear equation is :\n", sol_M)

print(M.flags)
