---
title: Un ejemplo sencillo
menu:
  docs:
    parent: automation-tutorials
weight: 6171
---

Bienvenido al primer tutorial acerca del uso de Karaoke Templater (plantillas Karaoke) para crear [efectos de karaoke]({{<relref path="../../Glossary/Karaoke_effect" lang="en">}}). Comenzaremos con algo simple y luego continuaremos con efectos más avanzados a lo largo de la serie.

## Encontrar Karaoke Templater

Puede ejecutar Karaoke Templater de dos maneras diferentes. Por ahora sólo nos enfocaremos en uno de ellos.

Busque bajo el menú Automatización en Aegisub.

![Automation-menu-kara-templater-gray](/img/3.2/Automation-menu-kara-templater-gray.png)

Debe de verse la opción llamada _Aplicar plantilla karaoke_, aunque no estará disponible. Esto es lo que uno seleccionará para usar las "plantillas" que escribiremos a lo largo de estos tutoriales. En este momento no está disponible porque no se ha creado ninguna plantilla. Llegaremos a eso en un momento.

Si no tiene la opción _Aplicar plantilla karaoke_, su instalación de Aegisub está incompleta o dañada. En ese caso, deberá reparar su instalación para poder utilizar Karaoke Templater.

Pero hay algo más de que asegurarnos primero.

## Karaoke sincronizado

Karaoke Templater puede hacer muchas cosas por usted, pero no puede adivinar la letra de una canción ni cómo se sincroniza con la música. Tendrá que sincronizar la letra uno mismo o pedirle a alguien más que lo haga. Puede aprender a sincronizar el karaoke en el [tutorial de sincronizar karaoke]({{<relref path="Karaoke_Timing_Tutorial" lang="en">}}).

Llamaremos a las letras de canciones con sincronización básica de karaoke (\\k sincronización), pero sin otros efectos especiales, _karaoke cronometrado_. Cuando se ha aplicado un efecto al karaoke lo llamaremos _karaoke con estilo_.

Si no tienes ninguna canción con la que trabajar, aquí tienes dos líneas de una canción. Puede seleccionarlos en su navegador, seleccionar _Editar_→_Copiar_, luego ir a Aegisub y seleccionar _Editar_→_Pegar_, para ingresarlos en Aegisub.

```culo
Diálogo: 0,0:00:01.85,0:00:09.06,Predeterminado,,0000,0000,0000,,{\k97}shi{\k41}ta{\k0} {\k20}no{\k10} { \k30}u{\k80}e{\k53} {\k23}a{\k21}ma{\k39}ku{\k7} {\k24}to{\k24}ke{\k31}ru{\k0 } {\k37}wa{\k23}ta{\k92}gu{\k69}mo
Diálogo: 0,0:00:09.28,0:00:16.21,Predeterminado,,0000,0000,0000,,{\k79}ki{\k61}su{\k0} {\k9}o{\k0} { \k37}shi{\k98}te{\k40} {\k23}ku{\k25}ro{\k40}i{\k0} {\k28}tsu{\k19}ba{\k51}sa{\k0 } {\k11}no{\k0} {\k34}mierda{\k138}ta
```

De cualquier manera, ahora tienes algunas letras cronometradas para karaoke, así que podemos comenzar.

### Cargar un vídeo

No es necesario cargar ningún audio, pero puede ser una buena idea tener algún vídeo abierto. Si no tiene ningún archivo de video listo que pueda usar, seleccione _Video_→_Usar video ficticio_ y simplemente diga Aceptar. No es un vídeo muy interesante el que obtendrás.
pero te mostrará cómo se verán los subtítulos y el efecto que estamos creando.

## Escribir una plantilla de estilo _k-replacer_

Ahora que tenemos todo lo demás configurado, es hora de crear la plantilla real.
Primero, aquí se explica cómo agregarlo. A continuación se explica lo que significa cada parte.

1. Seleccione la primera línea de subtítulo del archivo.
1. Seleccione _Subtítulos_→_Insertar líneas_→_Antes de la actual_ para obtener una nueva línea antes. Esta se convertirá en nuestra línea de plantillas de karaoke. No es necesario que sea el primero, pero normalmente hace que sea más fácil realizar un seguimiento.
1. Asegúrese de que la línea recién creada tenga el mismo _estilo_ que su karaoke cronometrado.
1. Haga clic en la casilla de verificación _Comentario_ para la nueva línea. Debería cambiar de color en la cuadrícula de subtítulos.
1. Busque el campo _Efecto_, está a la derecha de los campos _Estilo_ y _Actor_. Coloque el texto "`línea de plantilla`" en él. (¡Sin las comillas!) Presione la tecla _Enter_ en su teclado para guardar el campo Efecto.
1. Finalmente, ingrese este texto para el texto principal de la línea de su plantilla. Termine con _Enter_ nuevamente. `{\r\t($inicio,$medio,\fscy120)\t($medio,$fin,\fscy100)}`

{{<todo>}}Inserta una captura de pantalla de cómo debería quedar después de los pasos. {{</todo>}}

Ahora mira el menú _Automatización_ nuevamente. Si creó la línea de la plantilla correctamente, ahora estará disponible _Aplicar plantilla de karaoke_. Si no es así, revise los pasos anteriores nuevamente.

Seleccione _Aplicar plantillas de karaoke_ y observe cómo Karaoke Templater hace su trabajo.

{{<todo>}}Otra captura de pantalla, esta vez después de aplicar plantillas. {{</todo>}}

Si tienes un vídeo abierto puedes ver el efecto ahora mismo, dentro de Aegisub.

Observe también cómo la línea de la plantilla se dejó en su lugar y el karaoke cronometrado se cambió a líneas de comentarios y se completó _karaoke_ en sus campos de Efecto.
Karaoke Templater conserva tu karaoke cronometrado en el karaoke con estilo para que no lo pierdas. Pero también tiene otra función...

## Ampliando un poco el efecto

Continuando desde arriba, ahora intenta hacer esto:

1. Cambie el texto de la línea de la plantilla a: `{\r\k$kdur\t($start,$end,\1c&H00FF00&)\t($start,$mid,\fscy120)\t($mid,$ fin,\fscy100)}`
1. Aplicar plantillas nuevamente

{{<todo>}}Más captura de pantalla {{</todo>}}

Karaoke Templater reutilizó el karaoke cronometrado comentado y cambió el estilo del karaoke para que coincida con el nuevo efecto. También puedes intentar cambiar el karaoke cronometrado comentado y aplicar plantillas nuevamente.

De esta manera, puedes trabajar gradualmente en tu efecto y obtener una vista previa a medida que avanzas.

# ¿Entonces, qué significa todo ésto?

Para finalizar esta primera parte del tutorial, esto es lo que significa cada parte.
Esta no es la explicación completa de todo, pero debería ser suficiente por ahora.

- Las _Líneas de plantilla_ son líneas en el archivo de subtítulos marcadas de forma especial.
   Siempre deben ser líneas de comentario y la primera palabra en su efecto.
   El campo debe ser "plantilla".
- Existen varios tipos de líneas de plantilla. Solo usamos uno en este
   tutorial, este tipo de línea de plantilla, o _clase de plantilla_, se llama _línea
   plantilla_. Sí, puede resultar un poco confuso. Se llama así porque
   crea una línea de karaoke con estilo a partir de una línea de karaoke cronometrado. El
   La segunda palabra en el campo Efecto de una línea de plantilla indica qué plantilla
   clase es. Para plantillas de línea, esto es "línea".
- Entonces, el texto "línea de plantilla" en el campo Efecto significa que se trata de una
   _línea de plantilla_ de _clase de línea_.

<!-- -->

- Una plantilla sólo hace algo con las líneas de karaoke cronometradas que tienen el mismo
   Estilo como línea de plantilla.

<!-- -->

- El karaoke con estilo producido por Karaoke Templater tiene "fx" en el efecto.
   campo. Esto se utiliza como recordatorio para Karaoke Templater de que esta línea
   deben ser reemplazados, si las plantillas se aplican una vez más.

<!-- -->

- El texto principal de una línea de plantilla se denomina _texto de plantilla_. En
   _line_ plantillas, cada etiqueta \\k se reemplaza con el texto de la plantilla.
- El texto de la plantilla puede utilizar varias _variables_. Estas son palabras cortas que
   comience con un signo de dólar, como `$start`, `$end`, `$mid` y `$kdur`.
   Las variables se reemplazan con la información que almacenan para cada sílaba.
   eso es reemplazado.
   - `$start` se reemplaza con la hora de inicio de la sílaba. Esto es
     en milisegundos desde el inicio de la línea, es decir. un código de tiempo adecuado
     para colocar en las etiquetas \\t, \\move y \\fade.
   - De manera similar, `$end` es el tiempo de finalización de la sílaba, también en
     milisegundos.
   - Un poco más especial es `$mid`, este es el _tiempo intermedio_ del
     sílaba, el tiempo justo en el medio de `$start` y `$end`. Aquí nosotros
     lo usó para hacer crecer cada sílaba durante la primera mitad de su duración,
     y volver a la altura normal para la segunda mitad. También en milisegundos.
   - La variable `$kdur`, sin embargo, está en centisegundos. Este es el
     tiempo original de la etiqueta \\k, y casi sólo es útil para poner
     nuevamente en una etiqueta \\k, como hicimos aquí.

Con este conocimiento, ya deberías poder crear muchos efectos. Es posible que también desee consultar la página sobre [etiquetas de anulación de ASS] ({{<relref path="ASS_Tags" lang="en">}}).

También puedes [continuar con el siguiente tutorial]({{<relref path="./Tutorial_2" lang="en">}}), donde veremos cómo hacer cálculos con variables para obtener más variación.
