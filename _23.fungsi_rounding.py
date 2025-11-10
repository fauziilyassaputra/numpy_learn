import numpy


value_koma = numpy.array([3.14159, 2.71828, 1.1421])
rounding = numpy.around(value_koma, decimals=2)
print(f"nilai tanpa rounding: {value_koma}")
print(f"nilai dengan rounding: {rounding}")

# membulatkan ke integer terdekat
value_koma = numpy.array([1.4, 1.6, 2.5, 3.5])
rounding = numpy.around(value_koma)
print(f"rounding angka ke integer terdekat: {rounding}")

# membulatkan ke int terkecil
print("====================")
nilai_value = numpy.array([3.7, 3.2, -3.2, -3.7])
floring = numpy.floor(nilai_value)
print(f"nilai value: {nilai_value}")
print(f"nilai hasil flooring: {floring} ")

# membulatkan ke bilangan terbesar
ceiling = numpy.ceil(nilai_value)
print(f"nilai hasil ceiling: {ceiling} \n")

print("====================")
# menghapus bagian desimal (truncate)
nilai_value = numpy.array([3.7, 3.2, -3.2, -3.7])
hapus_bilangan_koma = numpy.trunc(nilai_value)
print(f"value nilai adalah: {nilai_value}")
print(f"hasil bilangan yang dihapus komanya: {hapus_bilangan_koma}")

print("====================")
# menjadikan desimalnya nol (outputnya selalu float)
nilai_value = numpy.array([3.7, 3.2, -3.2, -3.7])
hapus_bilangan_koma = numpy.fix(nilai_value)
print(f"value nilai adalah: {nilai_value}")
print(f"hasil bilangan yang dihapus komanya: {hapus_bilangan_koma}")
