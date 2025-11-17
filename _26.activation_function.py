import numpy

def fungsi_linear(x):
    return x

nilai_x =  numpy.array([-2, -1, 0, 1, 2])
output = fungsi_linear(nilai_x)
print(f"inputnya alah : {nilai_x}")
print(f"linear outputnya adalah: {output}")



def funsi_step(x, threshold: int = 0) :
    return numpy.where(x >= threshold, 1,0)

output = funsi_step(nilai_x)
print("hasil dari fungsi step: ",output)


# fungsi sigmoid

def fungsi_sigmoid(x):
    kalkulasi_x = numpy.clip(x, -500, 500)
    return 1 / (1 + numpy.exp(-kalkulasi_x))

def turunan_sigmoid(x):
    sig = fungsi_sigmoid(x)
    return sig * (1 - sig)

output = fungsi_sigmoid(nilai_x)
print(f"hasil fungsi sigmoid: {output}")
print(f"turunannya adalah: {turunan_sigmoid(0)}")


print("\n ====================")
# tanh

def fungsi_aktivasi_tanh(x):
    return numpy.tanh(x)

def turunan_tanh(x):
    return 1 - numpy.tanh(x) ** 2

nilai = numpy.array([-2,1,3,4,1])
output = fungsi_aktivasi_tanh(nilai)
print(f"fungsi tanh: {output}")
print(f"turunannya: {turunan_tanh(0)}")

print("\n ====================")
# Relu

def fungsi_relu(x):
    return numpy.maximum(0,x)

def turunan_relu(x):
    return numpy.where(x > 0, 1 , 0)

nilai_x = numpy.array([-2, 4, 3, 12, -1, 20])
output = fungsi_relu(nilai_x)
print(f"hasil relu: {output}")
print(f"turunannya: {turunan_relu(nilai_x)}")