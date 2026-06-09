# Modulo 1 — Python Basico
## Bloque: Usando variables

> Curso de Python · Mimo  
> Objetivo: Actualizar, operar y combinar variables con expresiones y numeros.

---

## Temas del bloque

- [Actualizando variables](#actualizando-variables)
- [Expresiones](#expresiones)
- [Numeros](#numeros)

---

## Actualizando variables

Las variables se llaman variables porque sus valores pueden cambiar. Se actualizan asignando un nuevo valor con `=`. Al actualizarse, la variable olvida su valor anterior.

```python
status = "Watching Netflix"
status = "Relaxing at the beach"
print(status)
# Output: Relaxing at the beach
```

Tambien es posible asignar a una variable el valor de otra variable.

```python
default_option = "upload"
new_status     = default_option
print(new_status)
# Output: upload
```

Notas completas: [modulo-01-actualizando-variables.md](./modulo-01-actualizando-variables.md)

---

## Expresiones

Una expresion combina valores para producir un nuevo valor. Las cadenas se pueden unir con `+`. Las expresiones pueden usarse directamente en `print()` o almacenarse en variables.

```python
# Concatenar cadenas
print("Followers:" + "55")
# Output: Followers:55

# Expresion con variable
followers = "55"
print("Followers:" + followers)
# Output: Followers:55

# Almacenar expresion en variable
label = "Posts:" + "13"
print(label)
# Output: Posts:13
```

Notas completas: [modulo-01-expresiones.md](./modulo-01-expresiones.md)

---

## Numeros

Los valores numericos no usan comillas. Con numeros podemos hacer calculos usando los operadores `+`, `-`, `*` y `/`.

```python
# Variable numerica
active_users = 5

# Suma
score = 40 + 4          # 44

# Resta
total    = 100
discount = 20
print(total - discount) # 80

# Multiplicacion
percent = 0.5 * 100
print(percent)          # 50.0

# Division
sum_of_grades = 460
students      = 5
print(sum_of_grades / students)  # 92.0
```

Diferencia clave: `3 + 1` suma (resultado: `4`), pero `"3" + "1"` concatena (resultado: `"31"`).

Notas completas: [modulo-01-numeros.md](./modulo-01-numeros.md)

---

## Archivos de este bloque

### Actualizando variables

| # | Archivo |
|---|---------|
| 01 | [ejercicio_01_status_netflix.py](./ejercicio_01_status_netflix.py) |
| 02 | [ejercicio_02_status_watching.py](./ejercicio_02_status_watching.py) |
| 03 | [ejercicio_03_status_football.py](./ejercicio_03_status_football.py) |
| 04 | [ejercicio_04_status_multiple.py](./ejercicio_04_status_multiple.py) |
| 05 | [ejercicio_05_new_status.py](./ejercicio_05_new_status.py) |
| 06 | [ejercicio_06_analysis.py](./ejercicio_06_analysis.py) |
| 07 | [ejercicio_07_temperature.py](./ejercicio_07_temperature.py) |
| 08 | [ejercicio_08_status_writing.py](./ejercicio_08_status_writing.py) |
| 09 | [ejercicio_09_currency.py](./ejercicio_09_currency.py) |
| 10 | [ejercicio_10_status_done.py](./ejercicio_10_status_done.py) |

### Expresiones

| # | Archivo |
|---|---------|
| 01 | [ejercicio_01_followers_concatenar.py](./ejercicio_01_followers_concatenar.py) |
| 02 | [ejercicio_02_followers_variable.py](./ejercicio_02_followers_variable.py) |
| 03 | [ejercicio_03_label_name.py](./ejercicio_03_label_name.py) |
| 04 | [ejercicio_04_label_posts.py](./ejercicio_04_label_posts.py) |
| 05 | [ejercicio_05_jonathan.py](./ejercicio_05_jonathan.py) |
| 06 | [ejercicio_06_username.py](./ejercicio_06_username.py) |
| 07 | [ejercicio_07_temperature_degrees.py](./ejercicio_07_temperature_degrees.py) |
| 08 | [ejercicio_08_posts.py](./ejercicio_08_posts.py) |
| 09 | [ejercicio_09_likes.py](./ejercicio_09_likes.py) |
| 10 | [ejercicio_10_ms_irene.py](./ejercicio_10_ms_irene.py) |

### Numeros

| # | Archivo |
|---|---------|
| 01 | [ejercicio_01_active_users.py](./ejercicio_01_active_users.py) |
| 02 | [ejercicio_02_applications.py](./ejercicio_02_applications.py) |
| 03 | [ejercicio_03_steps.py](./ejercicio_03_steps.py) |
| 04 | [ejercicio_04_speed.py](./ejercicio_04_speed.py) |
| 05 | [ejercicio_05_total_posts.py](./ejercicio_05_total_posts.py) |
| 06 | [ejercicio_06_percent.py](./ejercicio_06_percent.py) |
| 07 | [ejercicio_07_cadena_vs_numero.py](./ejercicio_07_cadena_vs_numero.py) |
| 08 | [ejercicio_08_score.py](./ejercicio_08_score.py) |
| 09 | [ejercicio_09_area_cadena.py](./ejercicio_09_area_cadena.py) |
| 10 | [ejercicio_10_months.py](./ejercicio_10_months.py) |
| 11 | [ejercicio_11_discount.py](./ejercicio_11_discount.py) |
| 12 | [ejercicio_12_savings.py](./ejercicio_12_savings.py) |
| 13 | [ejercicio_13_grades.py](./ejercicio_13_grades.py) |

---

*Actualizado el: 06 de junio de 2026*
