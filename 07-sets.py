this_set = {} # This is a dictionary
print(type(this_set))

this_set = { "Galford", "Hanzo", "Haohmaru", "Ukyo" }
print(this_set)
print(type(this_set))
print(len(this_set))

my_set = { 1, 2, 3, 4, 5 } # This is a set
print(len(my_set))
print(type(my_set))

my_set.add(100)
print(my_set)
my_set.add(34)
print(my_set)

# Un set no es una estructura ordenada
# Un set no admite repetidos
my_set.add(2)
print(my_set) # No se repite el 2


# Podemos hacer búsquedas
print(2 in my_set)
print(200 in my_set)

# Podemos eliminar elementos
my_set.remove(34)
print(my_set)

# Podemos copiar un set
my_set_copy = my_set.copy()
print(my_set_copy)

# Podemos eliminar el objeto completamente
del my_set_copy
# print(my_set_copy) # Error, not defined

# Podemos limpiar el set
my_set.clear()
print(len(my_set))
print(my_set)