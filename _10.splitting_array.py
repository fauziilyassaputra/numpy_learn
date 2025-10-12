# memecah array
import numpy

# array split

data_kita = numpy.array([1,2,3,4,5])
hasil = numpy.array_split(data_kita, 3) # menjadi 3 bagian

for i, partisi in enumerate(hasil):
    print(f"bagian dari {i + 1}: {partisi}")

# dengan 2 dimensi 

data_kita = numpy.array([[1,2],[3,4],[5,6],[7,8]])
hasil = numpy.array_split(data_kita, 3) # menjadi 3 bagian

for i, partisi in enumerate(hasil):
    print(f"bagian dari {i + 1} (2 dimensi): \n {partisi}")



print("=================================")
# split (harus bisa dibagi  rata)

data_kita = numpy.array([1,2,3,4,5,6])
hasil = numpy.split(data_kita, 3) # menjadi 3 bagian
for i, partisi in enumerate(hasil):
    print(f" splitting dengan split {i + 1}: {partisi}")


data_kita = numpy.array([[1,2,3,4],[5,6,7,8]])
hasil = numpy.split(data_kita, 2, axis=1) # menjadi 3 bagian
for i, partisi in enumerate(hasil):
    print(f" splitting dengan split 2D  ke-{i + 1}: \n {partisi}")

# vsplit

data_kita = numpy.array([[1,2,],[3,4],[5,6],[7,8]])
hasil = numpy.vsplit(data_kita, 2) # menjadi 3 bagian
for i, partisi in enumerate(hasil):
    print(f" splitting dengan vsplit 2D  ke-{i + 1}: \n {partisi}")

# horizontal split

data_kita = numpy.array([[1,2,3,4],[5,6,7,8]])
hasil = numpy.hsplit(data_kita, 2) # menjadi 3 bagian
for i, partisi in enumerate(hasil):
    print(f" splitting dengan hsplit 2D  ke-{i + 1}: \n {partisi}")

print("=================================")
# deeep way split
data_kita = numpy.array([[[1,2],[3,4],[5,6],[7,8]]])
hasil = numpy.dsplit(data_kita, 2) # menjadi 3 bagian
for i, partisi in enumerate(hasil):
    print(f" splitting dengan dsplit 3D  ke-{i + 1}: \n {partisi}")
