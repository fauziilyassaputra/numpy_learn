import numpy

# shape
data_kita = [[1,2],[3,4],[5,6]]
array_kita = numpy.array(data_kita)
print(array_kita)
print(f"tipe datanya adalah: {array_kita.dtype}")
print(f"shape dai data kita adalah: {array_kita.shape}")

print("=================================")
# as array (mengubah input menjadi array)
data_kita = numpy.array([2,4,6,8])
referensi_array = numpy.array(data_kita)
print(referensi_array)
print(f"tipe data dari referensi array : {referensi_array.dtype}")

print("=================================")
# array constant 
array_nol = numpy.zeros((3,4), dtype=numpy.float32)
print("array nol: ")
print(array_nol)

array_satu = numpy.ones((2,2), dtype=numpy.int32)
print("array satu: ")
print(array_satu)

array_full = numpy.full([2,3], 20, dtype=numpy.int16)
print("array 20: ")
print(array_full)

print("=================================")
# kelipatan 
array_kita = numpy.arange(0, 10, 2) # mulai dari 0 sampai 10 dengan kelipatan 2
print("array kelipatan 2 : ", array_kita)

# kalau tipe data float maka akan menyebabkan floating error
# solusinya gunakan linspace! (floting grafik, sampling, hyper parameter tuning)
array_kita = numpy.linspace(0,1,5)
print("array_kita dengan linspace: ",array_kita)

print("=================================")
# array dengan pola matriks
matriks_indetitas = numpy.eye(3)
print("matriks identitas: \n", matriks_indetitas)

# matriks persegi
matriks_indetitas = numpy.identity(3)
print("matriks identitas (persegi): \n", matriks_indetitas)

# matriks diagonal
matriks_indetitas = numpy.diag([2,3,4])
print("matriks identitas (diagonal): \n", matriks_indetitas)

print("=================================")
# random array (biasa digunakan untuk machine learning dan testing)

random_matriks_2dimensi = numpy.random.rand(2,3) # distirbusi acak uniform antara 0 - 1
print("random_array :")
print(random_matriks_2dimensi)

random_matriks_2dimensi = numpy.random.randn(2,2) # distirbusi normal standar
print("random_array (normal):")
print(random_matriks_2dimensi)

array_kita = numpy.random.randint(1,100, size=(3,)) # random integer (untuk inisialsisai bobot)
print("random_array (int):")
print(array_kita)

