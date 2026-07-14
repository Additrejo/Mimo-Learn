# Operador AND

Este bloque introduce el operador `and`, usado para tomar decisiones complejas que dependen de mas de una condicion a la vez.

## Conceptos

### Para que sirve el operador and

El operador `and` sirve para enlazar multiples condiciones dentro de una misma declaracion `if`. El bloque de codigo solo se ejecuta si todas las condiciones enlazadas son `True`.

### Cuando se omite el bloque de codigo

El operador `and` omite el bloque de codigo cuando una o mas condiciones son `False`. Por ejemplo, en `age > 16 and has_permit`, si cualquiera de las dos condiciones es `False`, el bloque no se ejecuta.

### Cuantas condiciones se pueden enlazar

No hay un limite de dos condiciones: se pueden agregar tantas condiciones como se quiera usando `and` de forma repetida, por ejemplo `condicion1 and condicion2 and condicion3`.

### Decisiones complejas en la practica

Los programas inteligentes usan el operador `and` para tomar decisiones que dependen de varios factores a la vez, como habilitar un boton solo cuando todas las condiciones necesarias se cumplen (por ejemplo, todas las casillas de un formulario marcadas).

## Ejercicios

1. `ejercicio_01_una-condicion.py` - Recordatorio de como ejecutar codigo con una sola condicion, antes de introducir `and`.
2. `ejercicio_02_dos-condiciones.py` - Combinar dos condiciones con `and` para verificar si se puede conducir.
3. `ejercicio_03_ambas-condiciones-true.py` - Practicar que ambas condiciones deben ser `True` para que el bloque se ejecute.
4. `ejercicio_04_condicion-false.py` - Ver como `and` omite el bloque cuando una condicion es `False`.
5. `ejercicio_05_tercera-condicion.py` - Agregar una tercera condicion encadenada con `and`.
6. `ejercicio_06_validar-anio.py` - Usar `and` para validar que un anio este dentro de un rango.
7. `ejercicio_07_caminar-al-trabajo.py` - Encadenar tres condiciones con `and` para decidir si caminar al trabajo.
