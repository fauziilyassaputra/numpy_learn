import numpy

data_kita = numpy.array([1,2,3,4,5])
masking = data_kita > 3
filtering = data_kita[masking]
print(masking)
print(filtering)
print("====================")

data_kita = numpy.array([1,2,3,4,5,6,7,8,9,10])
masking = (data_kita > 3) & (data_kita < 8)
filtering = data_kita[masking]
print(filtering)

print("====================")
data_kita = numpy.array([10, 20, 30, 40, 50])
data_indexing = numpy.array([0, 2, 4])
filtering = data_kita[data_indexing]
print(filtering)

print("====================")
matriks = numpy.array([[1,2],[3,4],[5,6],[7,8]])
baris_matriks = numpy.array([0,2])
filtering = matriks[baris_matriks]
print(filtering)

print("====================")
data = numpy.array([1,2,3,4,5])
hasil = numpy.where(data > 3, data * 2, data) # jika data > 3, maka kalikan 2
print(hasil)

print("====================")
data = numpy.array([1, 5, 3, 8, 2])
data_indeks = numpy.where(data > 4)
print(f"indeks yang lebih dari 4: {data_indeks[0]}")
print(f"data yang lebih dari 4: {data[data_indeks]}")


print("====================")

data_kita = numpy.array([0,1,0,3,0,5])
data_indeks = numpy.nonzero(data_kita)
print(f"indeks nonzero: {data_indeks[0]}")
print(f"data nonzero: {data_kita[data_indeks]}")

print("====================")
data_kita = numpy.array([1,2,3,4,5])
masking = data_kita > 3
indeks_data = numpy.nonzero(masking)
print("indeks: ",indeks_data[0])
print("data > 3 : ",data_kita[indeks_data])