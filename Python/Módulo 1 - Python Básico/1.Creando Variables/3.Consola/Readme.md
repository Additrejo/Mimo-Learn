# Modulo 1 — Python Basico
## Tema: Consola

> Curso de Python · Mimo  
> Objetivo: Mostrar valores en la consola usando la instruccion `print()`.

---

## Contenido

- [Instrucciones y ejecucion](#instrucciones-y-ejecucion)
- [La funcion print()](#la-funcion-print)
- [El orden importa](#el-orden-importa)
- [Multiples print()](#multiples-print)
- [Imprimir variables](#imprimir-variables)
- [Ejercicios](#ejercicios)

---

## Instrucciones y ejecucion

Las lineas de codigo son **instrucciones** para que la computadora las siga. Cuando ejecutamos codigo, le decimos a la computadora que siga las instrucciones que hemos reunido.

> Que es la consola: un area que muestra la salida del programa, tambien conocida como shell.

---

## La funcion print()

Con la instruccion especial `print()` le decimos a la computadora que muestre un valor en la consola.

```python
print("Hello, World!")
```

Output:
```
Hello, World!
```

> Que hace print(): muestra un valor en la consola.  
> Como saber que "Hello, World!" es una cadena: comienza y termina con comillas dobles.

---

## El orden importa

El orden de las instrucciones importa porque la computadora las sigue **linea por linea**.

```python
step_1 = "Collect pants"
step_2 = "?"
step_3 = "Profit"
```

---

## Multiples print()

Podemos usar `print()` tantas veces como queramos. Cada valor aparece en una nueva linea en la consola.

```python
print("3, 2, 1")
print("GO!")
```

Output:
```
3, 2, 1
GO!
```

---

## Imprimir variables

Tambien podemos usar `print()` para mostrar el valor de una variable.

```python
greeting = "Hello, World!"
print(greeting)
```

Output:
```
Hello, World!
```

Al pasar una variable a `print()`, la consola muestra su valor, no su nombre.

```python
sport = "B-ball"
print(sport)
# Output: B-ball  (no "sport")
```

---

## Ejercicios

| # | Descripcion | Archivo |
|---|-------------|---------|
| 1 | Hello World con print() | [ejercicio_01_hello_world.py](./ejercicio_01_hello_world.py) |
| 2 | Orden de instrucciones con steps | [ejercicio_02_steps.py](./ejercicio_02_steps.py) |
| 3 | Multiples print() | [ejercicio_03_multiples_print.py](./ejercicio_03_multiples_print.py) |
| 4 | Imprimir una variable | [ejercicio_04_greeting.py](./ejercicio_04_greeting.py) |
| 5 | Mostrar el valor de job | [ejercicio_05_job.py](./ejercicio_05_job.py) |
| 6 | print() con cadena directa | [ejercicio_06_buzz.py](./ejercicio_06_buzz.py) |
| 7 | Imprimir variable sport | [ejercicio_07_sport.py](./ejercicio_07_sport.py) |
| 8 | Mostrar el valor de last_name | [ejercicio_08_last_name.py](./ejercicio_08_last_name.py) |
| 9 | Mostrar el valor de frequency | [ejercicio_09_frequency.py](./ejercicio_09_frequency.py) |

---

*Actualizado el: 06 de junio de 2026*
