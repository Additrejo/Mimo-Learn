# Al intentar asignar a today el valor de la variable monday,
# Python produce un NameError porque monday no ha sido definida.
# Para actualizar una variable con otro valor de cadena,
# ese valor debe ir entre comillas.

# Codigo con error (no ejecutar):
# today = "Sunday"
# today = monday        # NameError: name 'monday' is not defined
# print(today)

# Codigo corregido:
today = "Sunday"
today = "Monday"
print(today)
