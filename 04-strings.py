my_name = "Rafael"

# String concatenation and strings in two lines
print(my_name + "\nString length: " + str(len(my_name)))

# Tab
my_lastname = "Ortiz"
print(my_lastname + " (here comes a tab)\tString length: " + str(len(my_lastname)))

# Formatted string - this is the correct way to format strings in Python 3
name, lastname, age = "Rafael", "Ortiz", 38
print(f"My name is {name} {lastname} and I'm {age} years old")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[0:2]
print(language_slice)

language_slice = language[2:5]
print(language_slice)

# Reversing a string
reversed_string = language[::-1]
print(reversed_string)

# Funciones
print(language.upper())
print(language.lower())
print(language.title())
print(language.capitalize())
print(language.count("y"))
print(type(language))
print(language.isnumeric())
print(language.isalpha())
print(language.isalnum())
print(language.isdigit())
print(language.islower())
print(language.isupper())
print(language.isspace())
print(language.istitle())
print(language.startswith("p"))