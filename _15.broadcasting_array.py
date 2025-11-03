# bisa melakukan operasi matematika dengan shape yang berbeda 

# 1. jika array tidak punya dimensi yang sama axis=0
# 2. untuk setiap dimensi, dimensinya akan dianggap kompatible

import numpy

print("====================")
# boardcasting 1D dengan 2D
matriks = numpy.array([[1,2,3], [4,5,6]])
vektor = numpy.array([10, 20, 30])
hasil = matriks + vektor
print(f"shape matriks : {matriks.shape}")
print(f"shape vektor : {vektor.shape}")
print(f"matriks + vektor: \n {hasil}")