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
print("shape :", array_kita.shape)
print("tipe data :", array_kita.dtype)


print("=================================")
# simpan array dengan format tertentu

numpy.array([1,2,3,4], dtype=numpy.int32).tofile('data.bin') # buat data.bin
load_data = numpy.fromfile('data.bin', dtype=numpy.int32)
print(load_data)


print("=================================")
# membuat array dengan build in python (range)
array_kita = numpy.array(range(10))
print("array kita dengan range : ", array_kita)

print("=================================")
# membuat array dengan generator

def generator_data(n):
    for i in range(n):
        yield i ** 2

# array_kita = numpy.array(list(generator_data(5)))
array_kita = numpy.fromiter(generator_data(5), dtype=numpy.int32, count=5)
print("hasil dari array generator: ", array_kita)

print("=================================")
# membuat array berdasarkan  buffer

data_kita = b'\x00\x00\x00\x00\x00\xf0\x00@'
array_kita = numpy.frombuffer(data_kita, dtype=numpy.float64)
print("array_kita dari buffer : ", array_kita)

print("=================================")
# membuat array berdasarkan  dict
data_kita = {'x': [1,2], 'y': [3,4]}
values = list(data_kita.values())
array_kita = numpy.array(values)
print("array_kita dari dict: \n", array_kita)
print("dimensi array_kita: ", array_kita.shape)
