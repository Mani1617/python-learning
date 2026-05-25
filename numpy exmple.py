# numbers = [1,2,3,4]

# total = sum(numbers)

# print(total)

import numpy as np

numbers=np.array([1,2,3,4])
print(np.sum(numbers))
print(numbers * 2)
print(np.mean(numbers))
print(np.median(numbers))
print(np.min(numbers))
print(np.max(numbers))
matrix=np.array([[1,2],[3,4]])
print(matrix[matrix > 1])
a = np.array(10)
b = np.array([1,2,3])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
e=np.array([[[0.1,0.2,0.3],[1,2,3]],[[10,20,30],[12,13,14]],[[1.35,3.45,2.89],[1,10,100]]])
# print(a.shape)
# print(b.shape)
# print(c.shape)
# print(d.shape)
# print(e.shape)
# print(e)

# print(f"a demensions is:",a.ndim)
# print(f"b demensions is:",b.ndim)
# print(f"c demensions is:",c.ndim)
# print(f"d demensions is:",d.ndim)
# print(f"e demensions is:",e.ndim)
# print(a.dtype)
# print(d.dtype)
f=np.arange(1,11)
print(f)
f=np.arange(1,11,2)
print(f)
g=np.eye(5,dtype=int)
print(g)
h=np.zeros((5,5),dtype='int')
print(h)
i=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(i)
print(np.transpose(i))



