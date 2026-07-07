# Podemos almacenar el resultado de una comparacion en una variable
# y reutilizar esa variable en la condicion, en lugar de reescribir
# la comparacion cada vez.

score = 51
pass_grade = score > 50
if pass_grade:
    print("Passed!")
