# Para una condicion mas especifica, como si hour es mayor que 12
# pero menor que 17, podemos codificar elif hour < 17: en su lugar.

hour = 14

if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
