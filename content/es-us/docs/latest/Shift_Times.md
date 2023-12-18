---
title: Ajustar tiempos
menu:
  docs:
    parent: timing
weight: 5200
---

La herramienta **ajustar tiempos** es un procesador por lote para códigos de tiempo; ajusta los tiempos de inicio/fin de muchas líneas de subtítulos a la vez de varias maneras. Se encuentra en _Timing_ -> _Shift Times_.

Se ve así:

![shift_times](/img/3.2/shift_times.png#center)

La parte izquierda de la ventana contiene las opciones.

### Ajustar por

Estos controles deciden en qué dirección y cuánto se modificará cada marca de tiempo.

Tiempo
: Cuánto quiere ajustar cada marca de tiempo, en horas:minutos:segundos.centisegundos.

Fotogramas
: Si tiene un video cargado, puede especificar el tiempo de ajuste como un número de fotogramas en su lugar. Tenga en cuenta que cambiar a cero fotogramas se ajustará las marcas de tiempo a los tiempos de fotograma correspondientes sin realizar ningún traslado.

Hacia adelante o hacia atrás
: controla en qué dirección se ajustan las marcas de tiempo.

### Afectar

Estos controles deciden qué renglones se procesarán.

Todas las filas
: Aplica el cambio de tiempo a todas los renglones del guion.

Filas seleccionadas
: Aplica el cambio de tiempo solo a los reglones seleccionadas.

Selección en adelante
: Aplica el cambio de tiempo al primer renglón seleccionado y a todos debajo de él (en la cuadrícula).

### Tiempos

Estos controles deciden qué códigos/marcas de tiempo se procesarán.

Tiempos de inicio y fin
: Tanto el tiempo de inicio como de fin de los renglones afectados se verán modificados por la cantidad dada.

Solo tiempos de inicio
: Solo se modificarán los tiempos de inicio de los renglones afectados. Note que esto hace que los renglones sean más largos (si se traslada atrás) o más cortos (si se traslada adelante) e incluso puede hacer que tengan la duración en cero.

Solo tiempos de fin
: Solo se modificarán los tiempos de fin de los renglones afectados. Tenga en cuenta que esto hace que los renglones sean más largos (se se traslada adelante) o más cortos (si se traslada atrás) e incluso puede hacer que tengan la duración en cero.

Tenga en cuenta que si una línea se desplaza de modo que su marca de tiempo de inicio o fin sea negativa, esa marca de tiempo se pone a cero. Esto se puede utilizar para borrar todos los tiempos de un guion completo, retrocediendo un tiempo mayor que la última marca de tiempo del guion.

### Cargar desde el historial

Este es un historial de todos los ajustes de tiempo que ha realizado desde la última vez que borró el historial de ajustes (con el botón borrar). El formato es una serie de campos separados por comas. Los campos son:

- Nombre de archivo del guion (ej. "ejemplo.ass")
- Cantidad y dirección del ajuste (ej. "0:00:05.00 forward")
- Qué tiempos se vieron afectados, "s" para inicio, "e" para fin, "s+e" para ambos
- Qué filas se vieron afectadas; "sel start-end" para selecciones, "all" para todas las filas (ej. "sel 1-40")

Para cargar la configuración desde una entrada del historial, simplemente hágale doble clic.
