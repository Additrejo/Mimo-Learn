# Modulo 1 — Python Basico
## Bloque: Usando variables
### Tema: Actualizando variables

> Curso de Python · Mimo  
> Objetivo: Actualizar el valor de una variable usando el signo `=`.

---

## Contenido

- [Por que se llaman variables](#por-que-se-llaman-variables)
- [Como actualizar una variable](#como-actualizar-una-variable)
- [La variable olvida su valor anterior](#la-variable-olvida-su-valor-anterior)
- [Multiples actualizaciones](#multiples-actualizaciones)
- [Asignar el valor de otra variable](#asignar-el-valor-de-otra-variable)
- [Ejercicios](#ejercicios)

---

## Por que se llaman variables

Las variables se llaman variables porque los valores que almacenan **pueden cambiar**. Podemos actualizar una variable usando `=` y dandole un nuevo valor.

> Para actualizar una variable se usa `=` (un solo signo igual).  
> `==` (doble igual) es otra cosa — no actualiza la variable.

```python
# Correcto — actualiza la variable
status = "Working out"

# Incorrecto para actualizar
status == "Working out"
```

---

## Como actualizar una variable

Se escribe el nombre de la variable, el signo `=` y el nuevo valor. El valor anterior se reemplaza.

```python
status = "Watching Netflix"
status = "Relaxing at the beach"
print(status)

# Output:
# Relaxing at the beach
```

---

## La variable olvida su valor anterior

Cuando actualizamos una variable, olvida su valor anterior. Podemos mostrarla en distintos momentos para ver como cambia.

```python
status = "Playing football"
print(status)

status = "Walking the dog"
print(status)

# Output:
# Playing football
# Walking the dog
```

---

## Multiples actualizaciones

Podemos actualizar las variables tantas veces como queramos.

```python
status = "Incomplete"
status = "Complete"
print(status)

status = "New data required"
print(status)

# Output:
# Complete
# New data required
```

---

## Asignar el valor de otra variable

Tambien podemos asignar a una variable el valor de otra variable.

```python
default_option = "upload"
new_status    = "download"

new_status = default_option
print(new_status)

# Output:
# upload
```

---

## Ejercicios

| # | Descripcion | Archivo |
|---|-------------|---------|
| 1 | Actualizar status y mostrar | [ejercicio_01_status_netflix.py](./ejercicio_01_status_netflix.py) |
| 2 | Mostrar variable antes del cambio | [ejercicio_02_status_watching.py](./ejercicio_02_status_watching.py) |
| 3 | Dos prints para ver el cambio | [ejercicio_03_status_football.py](./ejercicio_03_status_football.py) |
| 4 | Multiples actualizaciones con print | [ejercicio_04_status_multiple.py](./ejercicio_04_status_multiple.py) |
| 5 | Asignar valor de otra variable | [ejercicio_05_new_status.py](./ejercicio_05_new_status.py) |
| 6 | Quiz — analysis Mean a Median | [ejercicio_06_analysis.py](./ejercicio_06_analysis.py) |
| 7 | Cambiar temperature a "100 degrees" | [ejercicio_07_temperature.py](./ejercicio_07_temperature.py) |
| 8 | Actualizar status a "Writing code" | [ejercicio_08_status_writing.py](./ejercicio_08_status_writing.py) |
| 9 | Actualizar currency a "Dollar" | [ejercicio_09_currency.py](./ejercicio_09_currency.py) |
| 10 | Cambiar status a "Done" | [ejercicio_10_status_done.py](./ejercicio_10_status_done.py) |

---

*Actualizado el: 06 de junio de 2026*
