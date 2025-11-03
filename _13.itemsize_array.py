# 8 bit = 1 byte
import numpy

data_array = numpy.array([1 , 2 , 3 ], dtype=numpy.int32) # int 32 adalah 32 bit (4 byte)
print(f"itemsizenya (int32) adalah: {data_array.itemsize}") # hasilnya tiap elemen mengandung 4 byte

# contoh dengan float
data_array = numpy.array([1.2 , 3.1, 4.2], dtype=numpy.float64) # 64bit = 8 byte
print(f"itemsizenya (float64) adalah: {data_array.itemsize}")


#gunakan int 64/float 64 untuk data yang lebih presisi, kelemahannya lebih lambat dan banyak makan memori
# merupakan properti penting untuk n-dimentional array yang akan menentukan berapa banyak memori yang dialokasikan untuk setiap elemen yang ada pada array numerical python