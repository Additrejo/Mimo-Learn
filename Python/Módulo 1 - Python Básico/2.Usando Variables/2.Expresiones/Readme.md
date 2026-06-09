# Modulo 1 — Python Basico
## Bloque: Usando variables
### Tema: Expresiones

> Curso de Python · Mimo  
> Objetivo: Combinar valores de cadena usando el operador `+`.

---

## Contenido

- [Que es una expresion](#que-es-una-expresion)
- [Concatenar cadenas con mas](#concatenar-cadenas-con-mas)
- [Expresiones con variables](#expresiones-con-variables)
- [Almacenar expresiones en variables](#almacenar-expresiones-en-variables)
- [Ejercicios](#ejercicios)

---

## Que es una expresion

Una expresion es una combinacion de valores que produce un nuevo valor. Las expresiones se convierten en valores, por lo que podemos usarlas en cualquier lugar donde usariamos un valor.

---

## Concatenar cadenas con mas

Podemos unir (concatenar) valores de cadena con el signo `+`.

```python
"Followers:" + "55"
```

El resultado de esta expresion es la cadena `"Followers:55"`. El `+` une las dos cadenas sin agregar espacios entre ellas.

```python
print("Jon" + "athan")

# Output:
# Jonathan
```

---

## Expresiones con variables

Cuando una expresion contiene variables, utiliza los valores almacenados en ellas.

```python
user = "snoopdogg"
print("Username:" + user)

# Output:
# Username:snoopdogg
```

```python
followers = "55"
print("Followers:" + followers)

# Output:
# Followers:55
```

---

## Almacenar expresiones en variables

Ya que las expresiones se convierten en valores, podemos almacenarlas en variables de la misma manera que los valores simples.

```python
label = "Name:" + "Joe"
# El valor de label es "Name:Joe"

label = "Posts:" + "13"
print(label)

# Output:
# Posts:13
```

---

## Ejercicios

| # | Descripcion | Archivo |
|---|-------------|---------|
| 1 | Concatenar dos cadenas con + | [ejercicio_01_followers_concatenar.py](./ejercicio_01_followers_concatenar.py) |
| 2 | Expresion con variable followers | [ejercicio_02_followers_variable.py](./ejercicio_02_followers_variable.py) |
| 3 | Valor de expresion guardada en label | [ejercicio_03_label_name.py](./ejercicio_03_label_name.py) |
| 4 | Expresion almacenada en variable label | [ejercicio_04_label_posts.py](./ejercicio_04_label_posts.py) |
| 5 | Quiz — concatenar Jon y athan | [ejercicio_05_jonathan.py](./ejercicio_05_jonathan.py) |
| 6 | Quiz — variable user en expresion | [ejercicio_06_username.py](./ejercicio_06_username.py) |
| 7 | Agregar variable temperature a expresion | [ejercicio_07_temperature_degrees.py](./ejercicio_07_temperature_degrees.py) |
| 8 | Mostrar Posts:55 en la consola | [ejercicio_08_posts.py](./ejercicio_08_posts.py) |
| 9 | Mostrar 40 likes en la consola | [ejercicio_09_likes.py](./ejercicio_09_likes.py) |
| 10 | Mostrar Ms. Irene en la consola | [ejercicio_10_ms_irene.py](./ejercicio_10_ms_irene.py) |

---

*Actualizado el: 06 de junio de 2026*
