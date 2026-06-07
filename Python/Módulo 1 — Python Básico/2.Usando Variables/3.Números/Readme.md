# Modulo 1 — Python Basico
## Bloque: Usando variables
### Tema: Numeros

> Curso de Python · Mimo  
> Objetivo: Almacenar y operar con valores numericos en variables.

---

## Contenido

- [Numeros en variables](#numeros-en-variables)
- [Expresiones con numeros](#expresiones-con-numeros)
- [Operadores aritmeticos](#operadores-aritmeticos)
- [Numeros vs cadenas](#numeros-vs-cadenas)
- [Almacenar calculos en variables](#almacenar-calculos-en-variables)
- [Ejercicios](#ejercicios)

---

## Numeros en variables

Las variables tambien pueden almacenar numeros. A diferencia de las cadenas, los valores numericos **no usan comillas**.

```python
active_users = 5
```

Los numeros facilitan el seguimiento de datos numericos.

> Como saber que una variable almacena un numero: no hay comillas dobles alrededor del valor.
> `score = 40 + 4`  →  numero
> `score = "40"`    →  cadena

---

## Expresiones con numeros

Podemos crear expresiones con numeros usando `+` para sumar.

```python
number_of_applications = 5 + 1
print(number_of_applications)

# Output:
# 6
```

Tambien podemos usar variables numericas en los calculos.

```python
number_of_steps = 70
print("You're on step:")
print(number_of_steps + 1)

# Output:
# You're on step:
# 71
```

---

## Operadores aritmeticos

| Operador | Operacion | Ejemplo |
|----------|-----------|---------|
| `+` | Suma | `3 + 5` → `8` |
| `-` | Resta | `10 - 3` → `7` |
| `*` | Multiplicacion | `0.5 * 100` → `50.0` |
| `/` | Division | `460 / 5` → `92.0` |

```python
percent = 0.5 * 100
print(percent)

# Output:
# 50.0
```

---

## Numeros vs cadenas

Cuando los digitos van entre comillas son cadenas, no numeros. El operador `+` los concatena en lugar de sumarlos.

```python
# Cadenas — concatena, no suma
temperature = "3" + "1"
print(temperature)
# Output: 31  (no 4)

# Numeros — suma
score = 40 + 4
print(score)
# Output: 44

# El operador dentro de una cadena no calcula
area = "3 * 5"
print(area)
# Output: 3 * 5  (no 15)
```

---

## Almacenar calculos en variables

Las expresiones numericas se convierten en valores y podemos almacenarlas en variables.

```python
private = 3
public  = 10
total   = private + public
print("Total posts:")
print(total)

# Output:
# Total posts:
# 13
```

---

## Ejercicios

| # | Descripcion | Archivo |
|---|-------------|---------|
| 1 | Variable con valor numerico | [ejercicio_01_active_users.py](./ejercicio_01_active_users.py) |
| 2 | Expresion numerica con + | [ejercicio_02_applications.py](./ejercicio_02_applications.py) |
| 3 | Variable en calculo numerico | [ejercicio_03_steps.py](./ejercicio_03_steps.py) |
| 4 | Quiz — valor de speed | [ejercicio_04_speed.py](./ejercicio_04_speed.py) |
| 5 | Almacenar calculo en variable | [ejercicio_05_total_posts.py](./ejercicio_05_total_posts.py) |
| 6 | Multiplicacion con * | [ejercicio_06_percent.py](./ejercicio_06_percent.py) |
| 7 | Quiz — cadena vs numero con + | [ejercicio_07_cadena_vs_numero.py](./ejercicio_07_cadena_vs_numero.py) |
| 8 | Quiz — score es numero | [ejercicio_08_score.py](./ejercicio_08_score.py) |
| 9 | Quiz — operador dentro de cadena | [ejercicio_09_area_cadena.py](./ejercicio_09_area_cadena.py) |
| 10 | Establecer months_per_year | [ejercicio_10_months.py](./ejercicio_10_months.py) |
| 11 | Restar discount de total | [ejercicio_11_discount.py](./ejercicio_11_discount.py) |
| 12 | Multiplicar savings por interest | [ejercicio_12_savings.py](./ejercicio_12_savings.py) |
| 13 | Dividir sum_of_grades entre students | [ejercicio_13_grades.py](./ejercicio_13_grades.py) |

---

*Actualizado el: 06 de junio de 2026*
