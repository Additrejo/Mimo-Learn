# Agreguemos otra declaracion if que use el operador not para
# ejecutar un bloque de codigo diferente si la condicion es False.

available = True

if available:
    print("In stock")

if not available:
    print("Out of stock")
