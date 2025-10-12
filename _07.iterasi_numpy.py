import numpy

# contoh metode yang manual (cocok untuk nilai yang biasa, bukan besar)

# iterasi satu dimensi
array_kita = numpy.array([1,2,3,4,5,6])

for value in array_kita:
    print(value)

# iterasi dua dimensi

array_kita = numpy.array([[1,2],[3,4],[5,6]])
print("barisnya adalah: ")
for baris in array_kita:
    print("barisnya adalah: ",array_kita)

print("=================================")
# menggunakan nditer (n dimentional iter)

matriks = numpy.array([[1,2],[3,4],[5,6]])
print("iterasi dengan nditer : ")
for value in numpy.nditer(matriks):
    print( value)

# mengurutkan berdasarkan memori dengan  fortran-style / c-style

# matriks = numpy.array([[1,2],[3,4]], order='F')
matriks = numpy.array([[1,2],[3,4]], order='C')
print("iterasi dengan fortran-style : ")
for value in numpy.nditer(matriks):
    print( value)

print("=================================")
# metode read and write (untuk perubahan nilai)

matriks = numpy.array([1,2,3])
print("iterasi dengan readwrite : ")
for x in numpy.nditer(matriks, op_flags=['readwrite']):
    x[...] = x * 2
print( matriks)

print("=================================")
# apply along axis

def hitung_baris(baris):
    return numpy.mean(baris)

def hitung_kolom(kolom):
    return (kolom - numpy.min(kolom)) / (numpy.max(kolom) - numpy.min(kolom))

matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
meannya = numpy.apply_along_axis(hitung_baris, axis=1, arr=matriks)
print("meannya: ", meannya)

normalisasi = numpy.apply_along_axis(hitung_kolom, axis=0, arr=matriks)
print("normalisasinya : \n", normalisasi)

# hindari foor looping biasa jika nilai arranya sangat besar !!
