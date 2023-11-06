# import module matematika

# 1. Cara import biasa
import matematika

print(matematika.tambah(2,3,4))
print(matematika.kali(2,3,4))
print(matematika.pangkat(2)(4))

# 2. Menggunakan from

from matematika import tambah, kali, pangkat
# from matematika import * # Tidak di sarankan karena kita tidak bisa mengetahui apa yang di import

print(tambah(2,3,4))
print(kali(2,3,4))
print(pangkat(2)(4))

# 3.  Menggunakan alias

from matematika import tambah as add, kali as multiply, pangkat as square
import matematika as math

print(add(2,3,4))
print(multiply(2,3,4))
print(square(2)(4))

print(math.tambah(2,3,4))
print(math.kali(2,3,4))
print(math.pangkat(2)(4))