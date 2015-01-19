import numpy as np 
# one dimentional array
a = np.array([1, 0, 0], float)
print 'Here is a 1-dimentional array ' 
print a
b = np.array([[1, 0, 0], [0, 1, 0]], float)
print 'Here is a 2-dimensional array ' 
print b
c = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], float)
print 'Here is 3-dimensional array' 
print c
print 'The shape of c is', c.shape
print 'The type of elements in the array is', c.dtype
print 'The square of the ideal matrix is' 
print np.dot(c,c)
print 'Dimension', c.ndim