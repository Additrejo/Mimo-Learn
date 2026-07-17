# Pregunta: ¿Qué muestra este código en la consola?

temperature = 5

if temperature < 0:
    print("Brr...")
elif temperature == 0:
    print("It's freezing!")
elif temperature < 10:
    print("It's cold out.")

# Salida esperada:
# It's cold out.
# (temperature no es menor que 0 ni igual a 0, pero sí es menor que 10)
