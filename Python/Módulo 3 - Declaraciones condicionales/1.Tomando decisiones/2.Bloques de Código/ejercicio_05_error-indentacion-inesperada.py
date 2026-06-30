# Las dos declaraciones print() dentro del bloque if no tienen la
# misma indentacion, por lo que la consola muestra un IndentationError.
# En este caso, la segunda linea tiene mas indentacion de la esperada.

if True:
    print("Good morning!")
        print("You have three appointments today")

# Output:
#   File "/home/default/code/file.py", line 3
#     print("You have three appointments today")
# IndentationError: unexpected indent
