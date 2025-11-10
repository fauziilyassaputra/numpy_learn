import numpy

data_pertama = numpy.array([1,2,3,4])
data_kedua = numpy.array([3,4,5,6])
union_hasil = numpy.union1d(data_pertama, data_kedua)
print(f"hasil unionnya adalah: {union_hasil}")

data_kita = numpy.array([1,1,2,2,3])
data_kita_kedua = numpy.array([2,3,3,4,5])
union_hasil = numpy.union1d(data_kita, data_kita_kedua)
print(f"hasil unionnya adalah: {union_hasil}")

# menggunakan float
data_pertama = numpy.array([3.0, 4.0, 5.0], dtype=numpy.float32)
data_kedua = numpy.array([1,2,3], dtype=numpy.int32)

unionnya = numpy.union1d(data_pertama, data_kedua)
print(f"hasilnya berupa float : {unionnya}")
print(f"tipe data berupa float : {unionnya.dtype}")

print("====================")
# jika 2 dimensi, gunakan flatten() untuk meratakan menjadi 1D

matriks_pertama = numpy.array([[1,2],[3,4]])
matriks_kedua = numpy.array([[3,4],[5,6]])
unionnya = numpy.union1d(matriks_pertama.flatten(), matriks_kedua.flatten())
print(f"hasil union dari matriks: {unionnya}")

print("====================")
# jika ada 3 array yang digabung (nested)

vektor_pertama = numpy.array([1,2,3])
vektor_kedua = numpy.array([3,4,5])
vektor_ketiga = numpy.array([5,6,7])
hasil = numpy.union1d(numpy.union1d(vektor_pertama,vektor_kedua), vektor_ketiga)
print(f"union 3 vektor: {hasil}")

# menggunakan reduce()
from functools import reduce

vektor_pertama = numpy.array([1,2,3])
vektor_kedua = numpy.array([3,4,5])
vektor_ketiga = numpy.array([5,6,7])
union_hasil = reduce(numpy.union1d, [vektor_pertama, vektor_kedua,vektor_ketiga])
print(f"union 3 vektor dengan reduce: {hasil}")
