# Lists

my_list = list()

# Length de la lista
print(len(my_list))

my_list = [17, 56, 24, 11, 78, 63, 38, 40, 38]
my_person = ['Raph', 'Ortiz', 38, 'M', True, 1,72, 70]

print(type(my_list))
print(len(my_list))


# Para saber cuántas veces está el número 38 en la lista
print('En la lista: ' + str(my_list) + ' el número 38 aparece ' + str(my_list.count(38)) + ' veces.')
# print(my_list.count(38))


# Concat dos listas
print (my_list + my_person)

# Agregar un elemento (al final de la lista)
my_list.append(100)
print(my_list)

# Insertar un elemento en una posición específica
my_list.insert(0, 'Italia')
print(my_list)

# Eliminar un elemento de la lista (en el ejemplo elimina el primer elemento que coincida con Italia)
my_list.remove('Italia')
print(my_list)

# Eliminar un elemento de la lista y quedarme con ese valor
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

# Eliminar un elemento de la lista por su posición
del my_list[0]
print(my_list)

# Eliminar todos los elementos de la lista
# my_list.clear()
# print(my_list)

# Copias de listas - un nuevo objeto, una nueva lista con los mismos valores
my_new_list = my_list.copy()
print(my_new_list)

# Imprimir los valores al revés
my_new_list.reverse()
print(my_new_list)

# Ordenar los valores de la lista
my_new_list.sort()
print(my_new_list)