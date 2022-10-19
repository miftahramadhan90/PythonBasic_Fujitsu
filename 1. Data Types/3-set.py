data_set = {2,4,5,6,7,8,10,10,'arip'} #SET tidak bisa data sama
print(type(data_set))
print(len(data_set))
print(data_set)
set2 = data_set.copy()

data_set.add("ramadhan")
print(data_set)

data_set.add(12)
print(data_set)

data_set.add(2)
print(data_set)

data_set.update()

data_set.clear()
print(data_set)
