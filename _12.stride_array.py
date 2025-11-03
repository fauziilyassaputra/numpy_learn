import numpy

array_kita = numpy.array([1.0,2.0,3.0], dtype=numpy.float32) # float adalah 4 byte
print(F"stridenya adalah: {array_kita.strides}")

# contoh stride 2 dimensi
array_kita = numpy.array([[1,2,3],[4,5,6]], dtype=numpy.int32)
print(f"stride 2 dimanesinya adalah: {array_kita.strides}")


# contoh stride 3 dimensi
array_kita = numpy.array([[[1,2],[3,4],[5,6],[7,8]]],dtype=numpy.int32)
print(f"stride 2 dimanesinya adalah: {array_kita.strides}")
