import numpy

# matriks x matriks
matriks_pertama = numpy.array([[1,2],[3,4]])
matriks_kedua = numpy.array([[5,6],[7,8]])
hasil = numpy.dot(matriks_pertama,  matriks_kedua)
print("dot antar matriks: \n",hasil)

# matriks x vekor

matriks_pertama = numpy.array([[1,2],[3,4]])
vektor = numpy.array([1,2])
hasil = numpy.dot(matriks_pertama,  vektor)
print("dot matriks x vektor: ",hasil)

print("====================")
# invers
from numpy.linalg import inv, det, eig, solve, svd


matriks_a = numpy.array([[4,7], [2,6]])
hasil_invers = inv(matriks_a)
hasil_identitas = numpy.dot(matriks_a, hasil_invers)
print("hasil inverse: ")
print(hasil_identitas)

print("====================")
# determinan
matriks_a = numpy.array([[1,2],[3,4]])
hasil_determinan = det(matriks_a)
print(f"hasil determinan: {hasil_determinan}")

print("====================")
# eigen
matriks_a =  numpy.array([[4,2],[1,3]])
eigenvalue, eigenvektor = eig(matriks_a)
print(f"eigenvaluenya adalah: {eigenvalue}")
print(f"eigenvektornya adalah: \n {eigenvektor}")

print("====================")
# solve
matriks_a = numpy.array([[2,3],[1,-1]])
vektor_b = numpy.array([7,1])
hasil_nilai_x = solve(matriks_a,vektor_b)
hasil_verif = numpy.dot(matriks_a, hasil_nilai_x)
print(hasil_verif)

print("====================")
# singular value decomposition
matriks_a = numpy.array([[1,2],[3,4],[5,6]])
U, S, VT = svd(matriks_a, full_matrices=False)
print(U)
print(S)
print(VT)

rekonstruksi_data = numpy.dot(U * S, VT)
print(rekonstruksi_data)