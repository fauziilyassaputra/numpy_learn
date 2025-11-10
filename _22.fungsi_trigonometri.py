import numpy

angle = numpy.array([0, numpy.pi / 2, numpy.pi , 3 * numpy.pi / 2, 2  * numpy.pi])
nilai_sin = numpy.sin(angle)
nilai_cos = numpy.cos(angle)
nilai_tangen = numpy.tan(angle)
print(f"sudut dalam radian: {angle}")
print(f"nilai sinnya: \n {nilai_sin}")
print(f"nilai cosinus:\n {nilai_cos}")
print(f"nilai tangen: {nilai_tangen}")