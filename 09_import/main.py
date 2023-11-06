# 1. untuk menyambung program dari external
import print_saja

# 2. import dengan data
import kota
import provinsi

print(kota.data) # kota itu namespace
print(provinsi.data) # provinsi itu namespace

# 3. import dengan fungsi
import matematika

print(matematika.tambah(4,4,4))