import numpy

# range 1 parameter
array_kita = numpy.arange(5)
print(array_kita) # 1,2,3,4,5

# range 3 parameter (start, stop, step)
array_kita = numpy.arange(2,100,2)
print("array dengan 3 parameter : \n", array_kita)

# range dengan float
array_kita = numpy.arange(0,1,0.1)
print("array dengan float: ", array_kita)

print("=================================")
# range float dengan linspace (start,stop,num)
array_kita = numpy.linspace(0,1,5)
print("array dengan linspace: ", array_kita)

array_kita = numpy.linspace(0,1,5, endpoint=False) # stopnya di sertakan
print("array dengan endpoint false: ", array_kita)


print("=================================")
# range dengan logspace

array_kita = numpy.logspace(0,2,3) # 10^0, 10^1, 10^2
print("array dengan logspace: ", array_kita)

array_kita = numpy.logspace(0,3,4, base=2) 
print("array dengan logspace base 2: ", array_kita)

print("=================================")
# range dengan geomspace

array_kita = numpy.geomspace(1,8,4) 
print("array dengan geomspace: ", array_kita)

array_kita = numpy.geomspace(1,1_000,4) 
print("array dengan geomspace: ", array_kita)
