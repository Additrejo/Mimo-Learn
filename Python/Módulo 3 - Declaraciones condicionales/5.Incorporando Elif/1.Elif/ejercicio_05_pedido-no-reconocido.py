# Muestra un mensaje en la consola cuando topping no sea igual a
# "pineapple" o "pepperoni".

topping = "mushrooms"

if topping == "pineapple":
    print("Request denied.")
elif topping == "pepperoni":
    print("Request accepted.")
else:
    print("Could not process request.")
