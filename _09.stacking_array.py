# menggabungkan data namun dimensinya berbeda

import numpy

# dari vektor ke matriks
data_a = numpy.array([1,2,3])
data_b = numpy.array([4,5,6])
hasil = numpy.stack((data_a,data_b))
print("hasil gabung 2 vektor menjadi matriks :\n",hasil)

data_a = numpy.array([1,2,3])
data_b = numpy.array([4,5,6])
hasil = numpy.stack((data_a,data_b), axis=1)
print("hasil gabung 2 vektor menjadi matriks (2 kolom) :\n",hasil)


print("=================================")
# vertical stack

data_a = numpy.array([1,2,3])
data_b = numpy.array([4,5,6])
hasil = numpy.vstack((data_a,data_b))
print("hasil gabung 2 vektor menjadi matriks (vertical) :\n",hasil)


# axis 1 (horizontal)
data_a = numpy.array([1,2,3])
data_b = numpy.array([4,5,6])
hasil = numpy.hstack((data_a,data_b))
print("hasil gabung 2 vektor menjadi matriks (horizontal) :\n",hasil)


print("=================================")
# ukuran 2 dimensi

data_a = numpy.array([[1],[2]])
data_b = numpy.array([[3,4],[5,6]])
hasil = numpy.hstack((data_a, data_b))
print("hasil gabungan 2 dimensi (hstack): \n", hasil)


data_a = numpy.array([[1,2],[3,4]])
data_b = numpy.array([[5,6],[7,8]])
hasil = numpy.dstack((data_a, data_b))
print("hasil gabungan 2 dimensi (dstack): \n", hasil)


print("=================================")
# column stack

data_a = numpy.array([1,2,3])
data_b = numpy.array([4,5,6])
hasil = numpy.column_stack((data_a,data_b))
print("hasil gabungan dengan column stack: \n", hasil)


# row stack (gunakan cstack lebih baik!)

data_a = numpy.array([1,2,3])
data_b = numpy.array([4,5,6])
hasil = numpy.row_stack((data_a,data_b))
print("hasil gabungan dengan row stack: \n", hasil)
