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

print("\n ====================")

data = numpy.array([1,2,3,4,100])
nilai_mean = numpy.mean(data)
nilai_median = numpy.median(data)
print(f"nilai mean dengan outlier: {nilai_mean}")
print(f"nilai median dengan outlier: {nilai_median}")

print("\n ====================")
# menghitung standar deviasi

data = numpy.array([1,2,3,4,5])
std_deviasi =  numpy.std(data)
print(f"nilai standar deviasi adalah: {std_deviasi}")

# default ddof=0 yaitu populasi , ddof=1 digunakan untuk sample
data = numpy.array([1,2,3,4,5])
pop_stddeviasi = numpy.std(data, ddof=1)
print(f"hasil standar deviasi dengan ddof: {pop_stddeviasi}")

print("\n ====================")
# mencari varians (varience)

data = numpy.array([1,2,3,4,5])
varience = numpy.var(data)
print(f"variencenya : {varience}")


print("\n ====================")
# min & max
data = numpy.array([3,1,4,1,5,9,2,6])
nilai_min = numpy.min(data)
nilai_max = numpy.max(data)
print(f"nilai min adalah: {nilai_min}")
print(f"nilai max adalah: {nilai_max}")

print("\n ====================")
# peak to peak (max - min)

data = numpy.array([1,3,5,7,9])
range_data = numpy.ptp(data)
print(f"data: {data}")
print(f"hasil ptp: {range_data}") # 9 - 1

print("\n ====================")
# menghitung rata-rata berbobot

data_value = numpy.array([1,2,3,4])
data_bobot = numpy.array([1,2,3,4])

bobot_nilai_rata2 = numpy.average(data_value, weights=data_bobot)
rata_rata_simple = numpy.average(data_value)
print(f"rata-rata nilai bobot: {bobot_nilai_rata2}")
print(f"\n rata-rata sederhana: {rata_rata_simple}")


