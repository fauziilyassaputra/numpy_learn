import numpy

data_tanggal = numpy.datetime64("2023-11-11")

# ada detik dengan T
data_detik = numpy.datetime64('2023-11-12T12:30:45')
data_milisecond = numpy.datetime64('2023-11-12T12:30:45.3419')

print(f"waktu: {data_tanggal}")
print(f"waktu dengan detik: {data_detik}")
print(f"waktu dengan milisecond: {data_milisecond}")


print("\n ====================")
# data tanggal berdasarkan hari
data_hari = numpy.datetime64("2025-11-11", "D") # D = daily, h = hourly, m = minute
print(f"menggunakan hari : {data_hari}")


print("\n ====================")
# time delta
satu_hari = numpy.timedelta64(1, 'D')
print(f"satu hari dengan timedelta: {satu_hari}")
beberapa_menit = numpy.timedelta64(12, 'm')
print(f"satu hari dengan timedelta: {beberapa_menit}")


print("\n ====================")
# penambahan dan pengurangan

waktu_mulai = numpy.datetime64("2025-01-01")
waktu_selesai = waktu_mulai + numpy.timedelta64(7,'D')
print(f"mulai event: {waktu_mulai}") # 2025-01-01
print(f"event selesai: {waktu_selesai}") # 2025-01-08

data_waktu = numpy.datetime64("2020-01-01")
data_waktu_kedua = numpy.datetime64("2020-06-01")
durasi_waktu = data_waktu_kedua - data_waktu
print(f"durasi dari 6 bulan: {durasi_waktu}") # dengan hari
print(f"durasi 6 bulan dengan jam : {durasi_waktu / numpy.timedelta64(1, 'h')}")