import numpy
import numpy.char as nchar

# menggabungkan nama
list_nama_pertama = numpy.array(["jane", "hoshimi", "asaba"])
list_nama_kedua = numpy.array(["doe", "miyabi", "harumasa"])
hasil = nchar.add(nchar.add(list_nama_pertama," "), list_nama_kedua)
print(f"hasilnya adalah: {hasil}")

# memberi nama jenis file
list_nama = numpy.array(["data_kita", "data_lapor", "data_makan"])
tambahin_format = nchar.add(list_nama, ".csv")
print(f"file dengan ekstensi csv: {tambahin_format}")

# menjadikan kapital atau sebaliknya

list_nama = numpy.array(["hugo", "vivian"])
menjadi_kapital = nchar.upper(list_nama)
print(f"hasil setelah upper: {menjadi_kapital}")

list_nama = numpy.array(["KOMANO", "ALICE", "yUZuHa"])
menjadi_kapital = nchar.lower(list_nama)
print(f"hasil setelah lower: {menjadi_kapital}")

list_nama = numpy.array(["hoshimi likes melon", "harumasa sleep walking", "the apple has been eaten  by shukaku"])
menjadi_kapital = nchar.capitalize(list_nama)
print(f"hasil setelah capitalize: {menjadi_kapital}")

#title case
list_nama = numpy.array(["hoshimi likes melon", "harumasa sleep walking", "the apple has been eaten  by shukaku"])
menjadi_kapital = nchar.title(list_nama)
print(f"hasil setelah title: {menjadi_kapital}")

print("====================")
# replace
list_nama = numpy.array(["power harumasa is electric","power qingyi is electric","power jane is pychical", "power dialyn is pychical"])
menjadi_kapital = nchar.replace(list_nama, 'electric', 'ether')
print(f"hasil setelah title: {menjadi_kapital}")