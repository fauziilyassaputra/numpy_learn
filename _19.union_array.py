import numpy

data_pertama = numpy.array([1,2,3,4])
data_kedua = numpy.array([3,4,5,6])
union_hasil = numpy.union1d(data_pertama, data_kedua)
print(f"hasil unionnya adalah: {union_hasil}")

data_kita = numpy.array([1,1,2,2,3])
data_kita_kedua = numpy.array([2,3,3,4,5])
union_hasil = numpy.union1d(data_kita, data_kita_kedua)
print(f"hasil unionnya adalah: {union_hasil}")