import pdb

# h = untuk help
# n = continue
# list = melihat code hanya spesifik
# ll = melihat seluruh code

def tambah(*args):
  hasil = 0
  for i in args:

    # attach debugger
    pdb.set_trace()
    hasil += i
  return hasil


def kali(*args):
  hasil = 1
  for i in args:
    hasil *= i
  return hasil

tambah(1,2,3,4,5,5,6,7,8,9)