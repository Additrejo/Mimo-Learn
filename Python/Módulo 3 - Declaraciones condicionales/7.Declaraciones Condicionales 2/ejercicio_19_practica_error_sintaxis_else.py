# Pregunta: ¿Qué está mal con este código?

is_weekend = False

else:
    print("rise and shine")
if is_weekend:
    print("stay in bed")

# Salida:
# File "file.py", line 3
#     else:
#     ^
# SyntaxError: invalid syntax

# Respuesta correcta: la declaración else debe venir después de la declaración if.
# El orden correcto sería:
#
# if is_weekend:
#     print("stay in bed")
# else:
#     print("rise and shine")
