# Modulo 01 - Formateo de cadenas: Cadenas formateadas (f-strings)

Curso: Python | Modulo: 1. Python Basico

---

## Conceptos cubiertos

### El problema de combinar tipos con `+`

Ya aprendimos que `+` puede unir dos cadenas. Sin embargo, usarlo para combinar un numero con una cadena produce un `TypeError`, porque son tipos de datos diferentes.

```python
print("new" + " messages")   # new messages
print(2 + " new messages")   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Cadenas formateadas: f-strings

Las **f-strings** (cadenas formateadas) permiten mostrar diferentes tipos de valores juntos dentro de una cadena, sin errores. Se reconocen por el caracter `f` colocado inmediatamente antes de las comillas.

Una f-string consta de dos partes: el caracter `f` y la cadena que queremos formatear.

```python
print(f"{2} new messages")   # 2 new messages
print(f"{6} new messages")   # 6 new messages
```

### Insertar valores entre llaves `{}`

Para mostrar valores numericos dentro de una f-string, se colocan entre llaves `{}`. Esto permite incluir numeros literales, variables o expresiones directamente en el texto.

```python
print(f"I would walk {500} miles")          # I would walk 500 miles
print(f"popularity increased by {12}%")     # popularity increased by 12%
print(f"{4} dataset entries")               # 4 dataset entries
```

### Insertar variables entre llaves

Las variables tambien pueden colocarse entre las llaves de una f-string. Al ejecutarse, Python sustituye la variable por su valor.

```python
new_messages = 2
print(f"{new_messages} new messages")   # 2 new messages

degrees = 70
print(f"Temperature: {degrees}F")       # Temperature: 70F
```

### Multiples llaves en una f-string

Es posible usar tantos pares de llaves como se necesiten dentro de una misma f-string.

```python
print(f"{5} new messages and {2} friend requests")
# 5 new messages and 2 friend requests
```

### Expresiones dentro de las llaves

Dentro de las llaves pueden colocarse expresiones aritmeticas. Python evaluara la expresion y mostrara el resultado.

```python
new = 5
read = 2
print(f"{new - read} unread messages")   # 3 unread messages
```

### Guardar una f-string en una variable

Las f-strings pueden almacenarse en variables para ser reutilizadas.

```python
new = 5
status = f"{new} new messages"
print(status)   # 5 new messages

movie = "Vertigo"
display = f"Airing tonight: {movie}"
print(display)  # Airing tonight: Vertigo
```

---

## Ejercicios

| Archivo | Descripcion |
|---|---|
| `ejercicio_01_concatenacion_cadenas.py` | Concatena dos cadenas con `+` |
| `ejercicio_02_error_tipo.py` | Muestra el TypeError al combinar `int` y `str` con `+` |
| `ejercicio_03_fstring_basica.py` | Introduce la f-string con un numero literal entre llaves |
| `ejercicio_04_fstring_estructura.py` | Muestra la estructura de una f-string con el caracter `f` separado |
| `ejercicio_05_fstring_multiples_llaves.py` | Usa dos pares de llaves en una misma f-string |
| `ejercicio_06_fstring_variable.py` | Inserta una variable entre las llaves de una f-string |
| `ejercicio_07_fstring_en_variable.py` | Guarda una f-string en una variable y la imprime |
| `ejercicio_08_expresion_en_llaves.py` | Evalua una expresion aritmetica dentro de las llaves |
| `ejercicio_09_fstring_caracter_f.py` | Codifica el caracter `f` antes de la cadena formateada |
| `ejercicio_10_fstring_500_miles.py` | Muestra un numero literal dentro de una f-string |
| `ejercicio_11_fstring_dataset.py` | Muestra una f-string con numero literal |
| `ejercicio_12_fstring_temperatura.py` | Inserta una variable numerica en una f-string de temperatura |
| `ejercicio_13_fstring_pelicula.py` | Guarda una f-string con una variable de cadena en otra variable |
