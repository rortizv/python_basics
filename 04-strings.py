my_name = "Rafael"

# String concatenation and strings in two lines
print(my_name + "\nString length: " + str(len(my_name)))

# Tab
my_lastname = "Ortiz"
print(my_lastname + " (here comes a tab)\tString length: " + str(len(my_lastname)))

# Formatted string - this is the correct way to format strings in Python 3
name, lastname, age = "Rafael", "Ortiz", 38
print(f"My name is {name} {lastname} and I'm {age} years old")