import numpy


# mengubah tipe data
data_list: list[int] = [1,2,3,4,5]
array_kita= numpy.array(data_list, dtype=numpy.int16) # : NDArray[signedinteger[_16bit]] 
print("tipe data data_list sebelum diubah: ", data_list)
print("tipe data data_list setelah diuabh: ", array_kita.dtype)

print("---")
# mengubah tipe data ke float
data_list: list[int] = [1,2,3,4,5]
array_kita= numpy.array(data_list, dtype=numpy.float64) # : NDArray[signedinteger[float64]] 
print("tipe data data_list sebelum diubah: ", data_list)
print(" data data_list setelah diuabh: ", array_kita)
print("tipe data data_list setelah diubah: ", array_kita.dtype)
print("---")
# mengubah tipe data matriks
matriks_kita = [[1,2,3],[4,5,6],[7,8,9]]
array_kita= numpy.array(matriks_kita, dtype=numpy.int32) # : NDArray[signedinteger[float64]] 
print("data matriks_kita setelah diubah: \n", array_kita)
print("tipe data matriks_kita setelah diubah: ", array_kita.dtype)

print("---")
# mengubah tipe data tuple
tuple_kita = (10,20,30,40,50)
array_kita= numpy.array(tuple_kita) # : default
print("data tuple_kita setelah diubah: ", array_kita)
print("tipe data tuple_kita setelah diubah: ", array_kita.dtype)

print("=================================")
# as array (agar hemat memori dan lebih cepat)
data_kita = numpy.array([1,2,3])
data_view =numpy.asarray(data_kita)
print("as array : ", data_view)


print("=================================")
# mengambil data yang sudah ada
array_kita = numpy.loadtxt('data.csv', delimiter=',', dtype=numpy.float32)
print(array_kita)

