# Pregunta: ¿Qué muestra este código en la consola?

caffeine = True
time = "day"

if caffeine == False or time != "night":
    print("Good night's sleep")
else:
    print("Awake all night")

# Salida esperada:
# Good night's sleep
# (caffeine == False es False, pero time != "night" es True,
# por lo que basta con or para cumplir la condición)
