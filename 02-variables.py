# Variables

# Siempre definir en snake_case

edad_empleado = 20 # int
peso_empleado = 80.5 # float
print(type(edad_empleado))
print(type(peso_empleado))
nombres_empleado = 'Harry' # str
apellidos_empleado = 'Choo Choo' # str
nombres_empleado = nombres_empleado + ' ' + apellidos_empleado # Concatenar str
print(type(nombres_empleado))
print('\n')
print('***EMPLEADO***')
print('Nombre empleado:', nombres_empleado)
print('La edad del empleado es', edad_empleado, 'años y su peso es', peso_empleado)


# len para saber la longitud de un str
print('El str del nombre completo del empleado tiene ', len(nombres_empleado), 'caracteres incluyendo los espacios')

# Crear varias variables en una sóla línea
nombre, apellido, edad = 'Harry', 'Choo Choo', 35
print('The name is', apellido, ', ', nombre, apellido, ' y mi edad es ', edad)