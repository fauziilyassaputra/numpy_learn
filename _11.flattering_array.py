# semnjadikan array multidimensi menjadi satu dimensi
import numpy 

# ravel

matriks = numpy.array([[1,2],[3,4],[5,6]])
flattening = numpy.ravel(matriks)
print("array dari 2D adalah :")
print(flattening)

flattening = numpy.ravel(matriks, order='F')
print("array dari 2D (F) adalah :")
print(flattening)


print("=================================")
# flatten
matriks = numpy.array([[1,2],[3,4],[5,6],[7,8]])
flattening = matriks.flatten()
print("array dari 2D adalah :")
print(flattening)

# dengan F
matriks = numpy.array([[1,2],[3,4],[5,6],[7,8]])
flattening = matriks.flatten(order='F')
print("array dari 2D(F) adalah :")
print(flattening)


print("=================================")
# dengan reshape -1 (2D)

matriks = numpy.array(([1,2],[3,4],[5,6],[7,8],[9,10]))
flattening = matriks.reshape(-1)
print("mengubah dimensi dengan shape -1 adalah :")
print(flattening)

# dengan reshape -1 (3D)

matriks = numpy.array(([[1,2],[3,4],[5,6],[7,8],[9,10]]))
flattening = matriks.reshape(-1)
print("mengubah dimensi dengan shape -1 3D adalah :")
print(flattening)
