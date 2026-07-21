# Vincula las condiciones con un operador que omite el bloque de código,
# no mostrando nada en la consola.

caffeine = True
time = "night"

if caffeine and time != "night":
    print("Good night's sleep")

# Como time != "night" es False, y con and se necesita que ambas condiciones
# sean True, el bloque de código se omite y no se muestra nada en la consola.
