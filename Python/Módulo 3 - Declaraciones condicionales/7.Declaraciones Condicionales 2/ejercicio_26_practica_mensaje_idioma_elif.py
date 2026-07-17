# Codifica la condición elif para mostrar Gracias si language es "Spanish".

language = "Spanish"
message = ""

if language == "English":
    message = "Thank you"
elif language == "Spanish":
    message = "Gracias"
elif language == "German":
    message = "Danke"

print(message)

# Salida esperada:
# Gracias
