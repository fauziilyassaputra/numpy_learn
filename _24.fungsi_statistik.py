import numpy

# menghitung rata-rata
data = numpy.array([1,2,3,4,5])
nilai_mean = numpy.mean(data)
print(f"persebaran data: {data}")
print(f"nilai rata-rata adalah: {nilai_mean}")

# menghitung rata-rata matriks 
matriks = numpy.array([[1,2,3],[4,5,6]])
baris_mean = numpy.mean(matriks, axis=1) # mean baris
kolom_mean = numpy.mean(matriks, axis=0) # mean kolom
print(f"mean dari baris adalah: {baris_mean}")
print(f"mean dari kolom adalah: {kolom_mean}")

print("\n ====================")
# median

data = numpy.array([1,2,3,4,5])
nilai_median = numpy.median(data)
print(f"median dari datanya adalah: {nilai_median}")
