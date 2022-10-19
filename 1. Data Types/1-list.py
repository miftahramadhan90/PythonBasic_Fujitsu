var_list = [1, 20, "miftah", 100]
print(type(var_list))
print(var_list)

list_baru = var_list.copy()

#RETRIVE LIST :

#1. ambil by indexnya :
print(var_list[1]) 
print(var_list[0])
print(var_list[-1])

#2. ambil by subindex
print(var_list[0:3]) #ngebacanya : index ke 3 ga ditarik(krn eklusif)
print(var_list[-2:]) #ambil dr "miftah sampai ke akhir index"
print(var_list[:4]) #ambil dr depan sampe index ke 3

#INSERT to LIST (sisip data ke dalam list)
var_list.insert(3, "RAMADHAN") #input data di index ke-3(setelah index ke 2)
var_list.insert(4, "RAMADHAN") #LIST dpt input data yang sama
print(var_list)

#APPEND DATA LIST (insert data di akhir list)
var_list.append(200)
print(var_list)

#CHANGE LIST by indexnya (yg membedakan dgn tuple, krn tuple tdk bisa Diubah)
var_list[4] = 'bin usman'
var_list[5:] = [101, 202] #change dengna range subindex.
print(var_list)

#DELETE DATA TERTENTU di DALAM LIST (remove / pop)
var_list.remove('RAMADHAN')  #remove : delete by valuenya
print(var_list)

var_list.pop(3)     #pop : delete by indexnya
var_list.pop(2)
print(var_list) 

#SORTIR (hanya bisa dengan tipe data yg sama, misal int saja)
var_list.sort(reverse=True)  #True ; artinya descending
print(var_list)

#COUNTING data LIST (misal jumlah data yg 200)
aa = var_list.count(200) #buat variable baru dlu utk nampung countnya
print(aa)

#MENCARI INDEX KEBERAPA dari DATA LIST Tertentu. 
bb= var_list.index(1) #buat variable baru dlu
print(bb)

#MENGHAPUS SELURUH DATA di DALAM LIST
var_list.clear()
print(var_list)

#HASIL COPY LIST_BARU 
print(list_baru) #tidak ngefek setelah byk perubahan var_list diatas

#=============================================
#EXTEND 2 BUAH LIST
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

'''cara cetak list action apa saja yg dimiliki oleh object'''
print(var_list.__dict__)