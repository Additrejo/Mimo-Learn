# Módulo 3: Declaraciones condicionales

Este módulo cubre las declaraciones condicionales en Python: la base para que
un programa tome decisiones y ejecute distintas líneas de código según se
cumplan o no determinadas condiciones. Empieza con la declaración `if` más
simple y avanza hasta encadenar múltiples condiciones con `elif`, `else`,
`and` y `or`.

## Bloques de este módulo

### [1. Tomando decisiones](./modulo-03-tomando-decisiones/modulo-03-tomando-decisiones.md)

Introduce la declaración `if`, su sintaxis básica y el concepto de condición.
Cubre cómo los valores booleanos `True` y `False` determinan si un bloque de
código se ejecuta o se omite, y cómo se construye una declaración `if`
completa: palabra clave `if`, condición y dos puntos `:`.

### [2. Bloques de código](./modulo-03-bloques-de-codigo/modulo-03-bloques-de-codigo.md)

Profundiza en el concepto de bloque de código: el conjunto de líneas
indentadas que dependen de una condición. Cubre la indentación, los errores
de indentación (`IndentationError`), el uso de variables como condición, y la
diferencia entre el código que pertenece al bloque `if` y el código que se
ejecuta siempre, independientemente de la condición.

### [3. Usando condiciones](./bloque-03-usando-condiciones/bloque-03-usando-condiciones.md)

Profundiza en el uso de operadores de comparación (`==`, `!=`, `>`, `<`,
`>=`, `<=`) como condiciones dentro de declaraciones `if`. Cubre qué tipos de
datos se pueden comparar, cómo comparar variables booleanas directamente con
`True` o `False`, y cómo almacenar el resultado de una comparación en una
variable para reutilizarlo como condición.

### [4. Declaraciones Condicionales 1](./bloque-04-declaraciones-condicionales-1/bloque-04-declaraciones-condicionales-1.md)

Consolida los fundamentos de la declaración `if`: la palabra clave, el
requisito de que la condición sea siempre un valor booleano, y cómo la
indentación determina qué código pertenece al bloque condicional. Introduce
además el operador `not`, que invierte un valor booleano, y explica por qué
conviene usar comparaciones o variables como condición en lugar de escribir
`True` o `False` de forma fija.

### [5. Declaraciones Else y Elif](./bloque-05-declaraciones-else-elif/bloque-05-declaraciones-else-elif.md)

**Tema 1: Declaraciones Else** — Introduce `else` como el plan de respaldo de
un `if`: se ejecuta cuando la condición del `if` es `False`. Explica por qué
`else` no necesita su propia condición, su posición al final del bloque, y
cómo reemplaza la necesidad de escribir una segunda declaración `if not`.

**Tema 2: Elif** — Introduce `elif` ("else if"), que permite verificar una
condición adicional cuando la anterior es `False`. Cubre cómo se pueden
encadenar múltiples declaraciones `elif`, cómo combinarlas con un `else`
final, y el orden en que Python evalúa las condiciones (se detiene en la
primera que sea `True`).

### [6. Usando decisiones complejas](./bloque-06-usando-decisiones-complejas/bloque-06-usando-decisiones-complejas.md)

**Tema 1: Operador AND** — Introduce el operador `and` para enlazar múltiples
condiciones en una misma declaración `if`. El bloque de código solo se
ejecuta si todas las condiciones enlazadas son `True`; si una sola es
`False`, el bloque se omite. Se pueden encadenar tantas condiciones como se
necesiten.

**Tema 2: Operador OR** — Introduce el operador `or`, que ejecuta el bloque
de código cuando al menos una de las condiciones vinculadas es `True`. El
bloque solo se omite cuando todas las condiciones son `False`. Al igual que
con `and`, se pueden encadenar tantas condiciones como se quiera.

### [7. Declaraciones Condicionales 2](./bloque-07-declaraciones-condicionales-2/bloque-07-declaraciones-condicionales-2.md)

Sección de práctica que repasa todo el contenido del módulo: `if`/`else`,
`elif`, los operadores `and` y `or`, y errores comunes de sintaxis e
indentación (`SyntaxError`, `IndentationError`).

## Conceptos clave del módulo

- La declaración `if` ejecuta un bloque de código solo si su condición se
  evalúa como verdadera.
- Las condiciones pueden ser valores booleanos directos (`True`, `False`),
  variables que almacenan esos valores, comparaciones, o el resultado de
  aplicar el operador `not`.
- Un bloque de código puede contener una o varias líneas, siempre que
  compartan la misma indentación. Una indentación incorrecta produce un
  `IndentationError`.
- Los operadores de comparación (`==`, `!=`, `>`, `<`, `>=`, `<=`) permiten
  construir condiciones más precisas, y su resultado puede guardarse en una
  variable para reutilizarlo.
- `else` funciona como respuesta predeterminada: se ejecuta cuando la
  condición del `if` correspondiente es `False`, y no necesita su propia
  condición.
- `elif` permite encadenar condiciones adicionales entre el `if` y el
  `else`. Python evalúa las condiciones en orden y se detiene en la primera
  que sea `True`.
- El operador `and` exige que todas las condiciones enlazadas sean `True`
  para ejecutar el bloque de código.
- El operador `or` solo necesita que una de las condiciones enlazadas sea
  `True` para ejecutar el bloque de código.
- Tanto `and` como `or` permiten enlazar tantas condiciones como se
  necesiten, sin límite de dos.
