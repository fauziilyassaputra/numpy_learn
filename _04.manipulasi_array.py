import numpy

# reshape (menguabh array ke dimensi lain)
array_kita = numpy.arange(6) # array 1 dimensi
reshaping = array_kita.reshape(2, 3) # array 2 dimensi
print(array_kita)
print("setelah di reshape: \n",reshaping)

print("=================================")
# resize (mengubah ukuran array)
array_kita = numpy.array([1, 2, 3])
hasil = numpy.resize(array_kita, (2,3))
print("resize array: \n", hasil)

print("=================================")
# Transpose
matriks = numpy.array([[1,2], [3,4]])
print("array sebelum transpose : \n", matriks)
print("transpos array : \n",matriks.T)

tensor = numpy.random.rand(2,3,4)
hasil = numpy.transpose(tensor, (2,0,1)) # 2 = 4, 0 = 2, 1 = 3
print("tensor sebelum transpose \n",tensor)
print("tensor setelah transpose \n",hasil)
print("shapenya adalah:")
print(tensor.shape)
print(hasil.shape)


print("=================================")
# flip
array_kita = numpy.array([1,2,3])
flipping = numpy.flip(array_kita)
print("array sebelum flip \n",array_kita)
print("array setelah flip \n",flipping)

matriks = numpy.array([[1,2], [3,4]])
print(f"matriks sebelum flip: \n", matriks)
print(f"matriks setelah flip: \n", numpy.flipud(matriks))

print("=================================")
# filtering dengan slicing
matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
subsetnya = matriks[0:2, 1:3] # 0:2 untuk baris, 1:3 untuk kolom
print("matriks: \n", matriks)
print("subsetnya adalah : \n", subsetnya)

array_kita = numpy.array([1,2,3,4,5])
filtering = array_kita > 3
hasil = array_kita[filtering]
print("array sebelum filtering: \n", array_kita)
print("array setelah filtering adalah : \n", hasil)

print("=================================")
# gabungkan matriks

matriks_a = numpy.array([[1,2],[3,4]])
matriks_b = numpy.array([[5,6], [7,8]])
hasil = numpy.concatenate((matriks_a, matriks_b), axis=0)
print( "gabung secara vertikal: \n",hasil)
hasil = numpy.concatenate((matriks_a, matriks_b), axis=1)
print( "gabung secara horizontal: \n",hasil)

print("=================================")
# split

array_kita = numpy.arange(8)
hasil = numpy.split(array_kita, 4)
print("array sebelum displit: \n",array_kita)
print("array setelah displit: \n",hasil)

print("=================================")
# menambahkan dimensi

array_kita = numpy.array([1,2,3])
print("array 1 dimensi : ",array_kita)
print("array 1 dimensi (shape): ",array_kita.shape)

hasil = numpy.expand_dims(array_kita, axis=0) # dari 1 dimensi ke 2 dimensi
print("array 2 dimensi: ",hasil)
print("array 2 dimensi (shape): ",hasil.shape)

print("=================================")
# boardcasting
matriks_a = numpy.array([[1,2,3],[4,5,6]])
matriks_b = numpy.array([10, 20, 30])
hasil = matriks_a + matriks_b
print("Boardcastingnya adalah :\n",hasil)


print("=================================")
# copy data
data_ori = numpy.array([1,2,3])
kopi = data_ori.copy()
kopi[0] = 90
print("data ori :", data_ori)
print("data kopi: ", kopi)

