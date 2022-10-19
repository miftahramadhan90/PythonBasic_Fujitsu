#contoh menggunakan Iterasi(Return) : membuat fungsi pangkat 2
sample_uji = [10,12,25]
def pangkat2(x):
    temp_list=[]
    for iterator in x:
        temp_list.append(iterator**2)
    return temp_list #----->#return : utk mengembalikan nilai akhir yg dibuat oleh si fungsi itu sendiri bro
                                    # dgn kondisi akan dikembalikan ketika ada yg panggil si fungsi ini cuy
                                    # contohnya dibawah dipanggil oleh Var a dengan input parameternya(var sample_uji)
                                    # Mau bukti? : matiin aja return nya (comment #), maka print(a) outputnya NONE.
result = pangkat2(sample_uji)
print(result)

#contoh menggunakan Generator (yield) : membuat fungsi pangkat 2
#Note: yield mengambalikan nilai dlm bentuk OBJECT(tidak bs langsung diprint dengan print(result))
sample_uji_2 = [10,12,25]
def pangkat2_yield(y):
    #temp_list=[]       #yield tidak perlu temporary list utk nampung sementara angka yg diproses
    for iterator in y:
        yield iterator**2 #langsung proses di dalam object Yield nya 
result2 = sorted(pangkat2_yield(sample_uji_2), reverse=True)  #jangan lupa dibuat variable result dlu diluar fungsi def nya

#ada 3 cara print utk object yield :

#cara 1, convert menjadi type list
#print(list(result2))   

#cara 2, di looping dlu resultnya lalu print di dlm looping | hasilnya dlm format looping:turun kebawah
for iterasi in result2:
    print(iterasi) 

#cara 3, menggunakan next, konsekuensinya diprint berkali2 sampe iterasi habis
#print(next(result2)) 
#print(next(result2))
#print(next(result2))


