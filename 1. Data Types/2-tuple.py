x = ("apple", "banana", "cherry", "banana", 100)
print(type(x))
print(x)

#GET INDEX
print(x[:4])

#CARI INDEX KEBERAPA
aaa = x.index('apple')
print(aaa)

#COUNT
count_x = x.count('banana')
print(count_x)

#UPDATE/CHANGE TUPLE
#data di dalam TUPLE sbnrnya tidak bisa diubah, 
# tapi bisa diakali dgn diubah dlu tipenya menjadi list
#setelah diubah dlm list, dikembaikan lagi mennjadi tuple, cth sbb :

y = list(x)
print(type(y))
print(y)

y[1] = "kiwi" #diubah data idx 1 menjadi kiwi
x = tuple(y) #X memakai var Y degn diubah dlu menjadi tipe tuple.
print(x)
print(type(x))
