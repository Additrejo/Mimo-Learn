# Bloque 06: Usando decisiones complejas

## Tema 2: Operador OR

### Concepto general

El operador `or` permite ejecutar un bloque de código cuando al menos una de las condiciones vinculadas es `True`. El bloque de código solo se omite cuando todas las condiciones enlazadas con `or` son `False`. A diferencia del operador `and`, con `or` no es necesario que se cumplan todas las condiciones, basta con que una sola sea verdadera.

Se pueden encadenar tantas condiciones como se quiera usando `or` repetidamente, por ejemplo:

```python
if condicion_1 or condicion_2 or condicion_3:
    ...
```

### Ejercicios de código

1. **ejercicio_10_operador_or_certificado_basico.py**
   Certificado otorgado si el promedio es "A" o la puntuación final es mayor o igual a 1300. Ambas condiciones se cumplen, por lo que se imprime el mensaje de certificado logrado.

2. **ejercicio_11_operador_or_certificado_condicion_falsa.py**
   Ninguna de las dos condiciones se cumple (promedio "B" y puntuación 1400 contra el umbral 1500), por lo que el bloque de código no se ejecuta.

3. **ejercicio_12_operador_or_certificado_una_condicion_true.py**
   Solo la condición del promedio se cumple; la de la puntuación final no. Al usar `or`, basta con que una sea verdadera para que el bloque se ejecute.

4. **ejercicio_13_operador_or_ir_a_nadar.py**
   Ejercicio de predicción de salida en consola: `is_summer` es `False` pero `is_warm` es `True`, por lo que el mensaje "Go for a swim" se imprime.

5. **ejercicio_14_operador_or_cargar_bandeja_entrada.py**
   Ambas variables (`mobile_internet` y `wifi`) se asignan como `False` para que el bloque de código no se ejecute, demostrando el caso en que `or` omite la ejecución.

6. **ejercicio_15_operador_or_certificado_tres_condiciones.py**
   Se agrega una tercera condición (`won_competition`) enlazada con `or`, mostrando que se pueden combinar tantas condiciones como se necesiten.

7. **ejercicio_16_operador_or_promover_articulo.py**
   Se agrega la condición `likes >= 60` a una cadena de tres condiciones con `or` para decidir si se promueve un artículo.

8. **ejercicio_17_operador_or_juego_ganado.py**
   Se asigna un valor a `level` para que la condición `level == 5` sea verdadera y el bloque de código se ejecute, aunque `score` no supere a `highest_score`.

9. **ejercicio_18_operador_or_viaje_carretera.py**
   Se enlazan las condiciones `is_weekend` y `on_vacation` con `or` para decidir si se realiza un viaje por carretera.

### Conceptos reforzados sin código (preguntas y ejemplos visuales)

- **Qué hace el operador or**: ayuda a vincular condiciones alternativas, a diferencia de no tener ningún operador lógico.
- **Ejemplo visual de aplicación real**: un formulario de becas estudiantiles ("Student Scholarships") donde el botón "Apply" se habilita si al menos una condición (promedio o puntuación final) se cumple, ilustrando el uso de `or` en una interfaz.
- **Cuándo omite el bloque de código el operador or**: únicamente cuando todas las condiciones vinculadas son `False`.
- **Cuántas condiciones alternativas se pueden enlazar con or**: tantas como se quieran, no hay límite de dos.
