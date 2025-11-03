import numpy

array_kita = numpy.array([[1,2],[3,4]], dtype=numpy.int32)
print(f"array kita: \n {array_kita}")
print(f"shape dari array_kita: {array_kita.shape}")

swapping = numpy.swapaxes(array_kita, 0, 1) # 0 baris 1 kolom
print(f"swaping shape: {swapping.shape}")
print(f"array kita setelah di swap: \n {swapping}")

print("====================")
# dengan tensor
data_gambar = numpy.array([[[255, 0, 0], [0, 255, 0]], [[255,255,0], [255,255,0]]])
print(f"shape dari si data_gambar: {data_gambar.shape}") # (2, 2, 3) 
print(data_gambar)

swapping = numpy.swapaxes(data_gambar, 0, 2)
print(f"shape dari hasil swapping: {swapping.shape}")
print(swapping)