import numpy

# pertambahan
data_a = numpy.array([1, 2, 3])
data_b = numpy.array([4, 5, 6])
hasil = data_a + data_b
print(f"hasil pertambahan: {hasil}")
print(f"data_a + 5: {data_a + 5}")

print("====================")
# pengurangan
data_a = numpy.array([10, 20, 30])
data_b = numpy.array([1, 2, 3])
hasil = data_a - data_b
print(f"hasil pengurangan adalah: {hasil}")
print(f"data_a - 5: {data_a - 4}")

print("====================")
# perkalian
data_a = numpy.array([2,3,4])
data_b = numpy.array([5,6,7])
hasil = data_a * data_b
print(f"hasil perkalian adalah: {hasil}")


print("====================")
# pembagian
data_a = numpy.array([10,20,30])
data_b = numpy.array([2,4,5])
hasil = data_a / data_b
print(f"hasil baginya: {hasil}") # hasilnya jika setelah koma adalah 0 maka tidak dibaca
print(f"tipe datanya adalah: {hasil.dtype}") # hasilnya adalah float untuk presisi, jika pembaginya bulat maka hasilnya integer

print("====================")
# pangkat
data_kita = numpy.array([2,3,4])
hasil = data_kita ** 2 
print(f"hasil dari pangkat 2 : {hasil}")

print("====================")
# sisa bagi
data_kita = numpy.array([10, 11, 12])
hasil = data_kita % 3
print(f"hasil dari modulus 3 adalah: {hasil}" )