# Agrega bilingual como una condición, luego usa or para enlazar trilingual
# y multilingual para que el bloque de código se ejecute.

bilingual = True
trilingual = False
multilingual = False

if bilingual or trilingual or multilingual:
    print("You speak more than one language!")

# Salida esperada:
# You speak more than one language!
