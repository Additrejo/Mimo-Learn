# Pregunta: ¿Qué muestra esto en la consola?

read = False
time_elapsed = 50

if read or time_elapsed > 30:
    print("Can't delete the message")

# Salida esperada:
# Can't delete the message
# (time_elapsed > 30 es True, por lo que basta para cumplir la condición con or)
