# Una tupla es inmutable, no se puede modificar

my_tuple = tuple()
my_other_tuple = ()

my_tuple = ('Raph', 'Ortiz', 38, 'M', True, 1,72, 70)
my_other_tuple = (55, 66, 77)

print(my_tuple.count(70))

# Para saber el index de un valor
print(my_tuple.index(True))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)


# Convertir la tupla a lista
my_tuple_converted_to_list = list(my_tuple)
print(type(my_tuple_converted_to_list))

# Eliminar la tupla - esto elimina la variable
del my_tuple
# print(my_tuple)
# NameError: name 'my_tuple' is not defined