# Comienza comprobando si like_author es True, luego usa or para comprobar
# like_genre, y finalmente got_recommendation.

like_author = False
like_genre = True
got_recommendation = True

if like_author or like_genre or got_recommendation:
    print("Buy book")

# Salida esperada:
# Buy book
