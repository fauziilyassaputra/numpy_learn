# dtype
# integer -> integer, unsigned integer
# floating point
# complex
# boolean
# string
# object
# datetime

import numpy

# integer
# int8, int 32, int-n

array_kita_int = numpy.array([1,2,3], dtype=numpy.int32)
print(array_kita_int)
print("tipe data array_kita_int : ")
print(array_kita_int.dtype)
print("byte pada array_kita_int : ")
print(array_kita_int.itemsize, " byte")

print("=================================")
# unsigned integer (hanya menerima tipe data positif)
# uint8, uint16, uint-n
array_kita_uint = numpy.array([[0, 128, 255], [30, 100, 200]], dtype=numpy.uint8)
print("array_kita_uint: ")
print(array_kita_uint)
print("tipe data array_kita_uint: ")
print(array_kita_uint.dtype)

# tes warping 
print("\ntes warping")
array_kita_uint = numpy.array([[5]], dtype=numpy.uint8)
print("array_kita_uint sebelum warp: ")
print(array_kita_uint)
print("array_kita_uint saat warp (5 - 10): ")
print(array_kita_uint - 10)

print("=================================")
# float32, float64
array_kita_float = numpy.array([3.1415926532], dtype= numpy.float32)
array_kita_float64 = numpy.array([3.1415926564], dtype= numpy.float64)
print("array_kita_float  :")
print(array_kita_float[0]) # otomatis dibulatkan jika float32 karena terbatas
print("\narray_kita_float64:")
print(array_kita_float64[0])
# seringnya di ML gunakan float 32 karena cukup akurat dan 2 kali lebih hemat memori, gunakan 64 jika mengejar presisi yang lebih banyak


print("=================================")
# complex64, complex128
array_kita_complex = numpy.array([1 + 2j, 3 - 4j], dtype=numpy.complex64)
print("array_kita_complex  :")
print(array_kita_complex[0])
print("tipe data array_kita_complex  :")
print(array_kita_complex.dtype)
# biasanya  digunakan dalam digital signal processing dan simulasi fisika


print("=================================")
# Boolean
array_boolean = numpy.array([True, False, True], dtype=bool)
print("array_boolean : ")
print(array_boolean)
print("tipe data array_boolean : ")
print(array_boolean.dtype)


print("=================================")
# str_
nama = numpy.array(["Rizki", "Nongpal", "Nizwa"], dtype='U10')
nama_str = numpy.array([b"hello", b"apa kabar"], dtype="S10") # maksimal 10 karakter, b = Byte of char
print("nama :")
print(nama)
print("tipe data nama :")
print(nama.dtype)
print("\nnama_str :")
print(nama_str)
print("tipe data nama_str :")
print(nama_str.dtype)


print("=================================")
# object (bisa menyimpan beragam tipe data)
objek_array = numpy.array([[1,2], {'b':1}, lambda x : x ** 2], dtype=object)
print("object array: ")
print(objek_array)
print("tipe data objek array: ")
print(objek_array)


print("=================================")
# Datetime
waktu = numpy.array(['2020-01-01', '2025-01-02'], dtype='datetime64[D]')
print("waktu :")
print(waktu)
print("selisih keduanya dalam hari :")
print(waktu[1] - waktu[0])
# sangat berguna untuk time series analysis, monitoring
