import numpy

# gabung array (dasar)

matriks_pertama = numpy.array([1,2,3])
matriks_kedua = numpy.array([4,5,6])
gabung_array = numpy.concatenate((matriks_pertama,matriks_kedua))
print("gabungan 2 array adalah : ", gabung_array)

# gabung dengan dimensi yang berbeda
matriks_pertama = numpy.array([1,2])
matriks_kedua = numpy.array([[3,4],[5,6]])
gabung = numpy.vstack((matriks_pertama,matriks_kedua))
print("gabungan 2 array yang berbeda ukuran (vertical):\n",gabung)

matriks_pertama = numpy.array([[1],[2]])
matriks_kedua = numpy.array([[3,4],[5,6]])
gabung = numpy.hstack((matriks_pertama,matriks_kedua))
print("gabungan 2 array yang berbeda ukuran (horizontal):\n",gabung)

print("=================================")
# d-stack (biasanya dipakai untuk RGB pada image processing)

matriks_pertama = numpy.array([[1,2],[3,4]])
matriks_kedua = numpy.array([[5,6],[7,8]])
gabung = numpy.dstack((matriks_pertama,matriks_kedua))
print("gabungan 2 array dstack:\n",gabung)



# pastikan dalam menggabungkan array memiliki dimensi yang sama !


