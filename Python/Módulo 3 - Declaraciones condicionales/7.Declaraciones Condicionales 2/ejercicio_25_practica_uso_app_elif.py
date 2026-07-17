# Agrega otra declaración elif que se ejecute si hours es mayor que 5.

hours = 3

if hours <= 2:
    print("Occasional app use")
elif hours <= 5:
    print("Moderate app use")
elif hours > 5:
    print("Frequent app use")

# Salida esperada:
# Moderate app use
# (hours es 3, por lo que cumple la segunda condición hours <= 5)
