# Modulo 1 — Python Basico
## Bloque: Verdadero y Falso
### Tema: Verdadero y Falso

> Curso de Python · Mimo  
> Objetivo: Usar los valores especiales True y False para representar estados en un programa.

---

## Contenido

- [Que es True](#que-es-true)
- [Que es False](#que-es-false)
- [Almacenar e imprimir booleanos](#almacenar-e-imprimir-booleanos)
- [Booleano vs cadena](#booleano-vs-cadena)
- [Ejercicios](#ejercicios)

---

## Que es True

`True` es un valor especial que no es ni una cadena ni un numero. No lleva comillas y no es un valor numerico. Es ideal para situaciones como verificar si una caracteristica esta activada o si los datos estan disponibles.

```python
powered_on = True
```

> Buen uso de True y False: mostrar si una funcion esta activada o desactivada.

---

## Que es False

`False` es el opuesto de `True`. Tambien es un valor especial sin comillas.

```python
upload = False
```

> Por que `False` no es una cadena: no hay comillas alrededor del valor.  
> Por que `"False"` no es lo mismo que `False`: cuando hay comillas, es una cadena, no un booleano.

---

## Almacenar e imprimir booleanos

Podemos almacenar `True` o `False` en variables y mostrarlos con `print()` igual que con cadenas y numeros.

```python
correct = True
print(correct)

# Output:
# True
```

```python
print("Load data")
status = False
print(status)

# Output:
# Load data
# False
```

---

## Booleano vs cadena

| Valor | Tipo | Tiene comillas |
|-------|------|----------------|
| `True` | Booleano | No |
| `False` | Booleano | No |
| `"True"` | Cadena | Si |
| `"False"` | Cadena | Si |

---

## Ejercicios

| # | Descripcion | Archivo |
|---|-------------|---------|
| 1 | Variable powered_on con True | [ejercicio_01_powered_on.py](./ejercicio_01_powered_on.py) |
| 2 | Almacenar y mostrar True | [ejercicio_02_correct.py](./ejercicio_02_correct.py) |
| 3 | Almacenar False y mostrar con print | [ejercicio_03_status_false.py](./ejercicio_03_status_false.py) |
| 4 | Quiz — False no es cadena | [ejercicio_04_upload_false.py](./ejercicio_04_upload_false.py) |
| 5 | Quiz — usuario dado de baja | [ejercicio_05_subscribed.py](./ejercicio_05_subscribed.py) |
| 6 | Mostrar estado de configuracion como False | [ejercicio_06_auto_update.py](./ejercicio_06_auto_update.py) |
| 7 | Variable prevent_logout con False | [ejercicio_07_prevent_logout.py](./ejercicio_07_prevent_logout.py) |
| 8 | Variable auto_save con True | [ejercicio_08_auto_save.py](./ejercicio_08_auto_save.py) |
| 9 | Variable calculate_average con True | [ejercicio_09_calculate_average.py](./ejercicio_09_calculate_average.py) |

---

*Actualizado el: 06 de junio de 2026*
