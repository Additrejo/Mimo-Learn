# Almacenar la comparacion de igualdad entre inbox_full y True
# dentro de show_alert, y usar esa variable en la condicion.

inbox_full = True
show_alert = inbox_full == True

if show_alert:
    print("Inbox full")
    print("Archive some to continue")
