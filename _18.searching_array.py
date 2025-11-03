import numpy

print("====================")

data = numpy.array([20, 30, 40, 80, 100, 120, 300, 90])
indexing_data = numpy.where(data > 80)
print(f"valuenya adalah: {data[indexing_data]}")
# data diubah
data = numpy.array([20, 30, 40, 80, 100, 120, 300, 90])
indexing_data = numpy.where(data > 80, 100, data) # dari variable data jika > 80 maka jadikan 100
print(f"valuenya adalah: {indexing_data}")

print("====================")
# minimal dan maksimal

data = numpy.array([30, 20, 50, 80, 90, 100])
maks_index = numpy.argmax(data)
minimal_index = numpy.argmin(data)
print(f"maksimal indeks-nya adalah: {maks_index}")
print(f"maksimal value-nya adalah: {data[maks_index]}")
print(f"minimal indeks-nya adalah: {minimal_index}")
print(f"minimal value-nya adalah: {data[minimal_index]}")

print("====================")
# dengan 2D
matriks = numpy.array([[1,5,3], [9,2,8], [4,7,6]])
flat_index = numpy.argmax(matriks)
baris, kolom = numpy.unravel_index(flat_index, matriks.shape)
print(f"posisi: baris => {baris}, kolom => {kolom}")
print(f"valuenya adalah: {matriks[baris, kolom]}")

print("====================")
vektor = numpy.array([1, 3, 5, 7 ,9])
valuenya: int = 6
posisi = numpy.searchsorted(vektor, valuenya)
print(f"posisi yang akan disisip: {posisi}")
print(f"array nilai yang akan dimasukan valuenya: {numpy.insert(vektor, posisi, valuenya)}")

vektor = numpy.array([1, 3, 5, 7 ,9])
valuenya: int = numpy.array([0,4,6,10])
posisi = numpy.searchsorted(vektor, valuenya)
print(f"posisi yang akan disisip: {posisi}")
print(f"array nilai yang akan dimasukan valuenya: {numpy.insert(vektor, posisi, valuenya)}")