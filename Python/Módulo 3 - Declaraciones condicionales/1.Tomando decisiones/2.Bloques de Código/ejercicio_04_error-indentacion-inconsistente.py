# Si la indentacion es incorrecta, la computadora no puede entender el
# codigo. Esto produce un IndentationError en la consola.
# Aqui, el segundo print() esta mal indentado por solo un espacio en
# lugar de dos, como el primer print().

if True:
    print("Look at me!")
   print("I'm a code block")

# Output:
#   File "/home/default/code/file.py", line 3
#     print("I'm a code block")
#                                ^
# IndentationError: unindent does not match any outer indentation level
