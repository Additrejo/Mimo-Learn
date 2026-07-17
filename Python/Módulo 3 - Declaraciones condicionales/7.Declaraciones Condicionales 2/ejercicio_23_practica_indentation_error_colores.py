# La indentación de print("My favorite color!") es diferente en el primer bloque if
# en comparación con el segundo.
#
# Este código da un IndentationError. ¿Qué bloque if lo causa?

color = "red"
if color == "blue":
    print("Blue is awesome!")
    print("My favorite color!")

if color == "green":
    print("Green is awesome!")
print("My favorite color!")

# Salida:
# File "/home/code/file.py", line 4
#     print("My favorite color!")
#                                ^
# IndentationError: unindent does not match any outer indentation level

# Respuesta correcta: el bloque "blue" causa el error, ya que la sangría del
# segundo print() es diferente tanto del otro print() como del if, por lo que
# el intérprete no entiende a dónde pertenece esa línea.
#
# En el bloque "green", el segundo print() está correctamente desindentado
# al mismo nivel que el if, por lo que no forma parte del bloque condicional.
