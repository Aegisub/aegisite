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

Llamaremos a las letras de canciones con sincronización básica de karaoke (\\k timing), pero sin otros efectos, _karaoke sincronizado_. Cuando se ha aplicado un efecto al karaoke lo llamaremos _karaoke estilizado_.

Si no tiene ninguna canción con la que trabajar, acá abajo hay dos líneas de una canción. Puede seleccionarlas en su navegador, darle a _Editar_→_Copiar_, luego ir a Aegisub y _Editar_→_Pegar_, para pegarlos en Aegisub.

```ass
Dialogue: 0,0:00:01.85,0:00:09.06,Default,,0000,0000,0000,,{\k97}shi{\k41}ta{\k0} {\k20}no{\k10} {\k30}u{\k80}e{\k53} {\k23}a{\k21}ma{\k39}ku{\k7}  {\k24}to{\k24}ke{\k31}ru{\k0} {\k37}wa{\k23}ta{\k92}gu{\k69}mo
Dialogue: 0,0:00:09.28,0:00:16.21,Default,,0000,0000,0000,,{\k79}ki{\k61}su{\k0} {\k9}o{\k0} {\k37}shi{\k98}te{\k40}  {\k23}ku{\k25}ro{\k40}i{\k0} {\k28}tsu{\k19}ba{\k51}sa{\k0} {\k11}no{\k0} {\k34}shi{\k138}ta
```

De cualquier modo, ahora que tiene unas letras karaoke sincronizadas, podemos comenzar.

### Cargar un video

No es necesario cargar ningún audio, pero puede ser buena idea tener algún video abierto. Si no tiene ningún archivo de video listo que pueda usar, seleccione _Video_→_Video suplente_ y dele a OK. No es un video muy interesante el que obtiene, pero le demostrará cómo se verán los subtítulos y el efecto que estamos creando.

## Escribir plantilla estilo _k-replacer_

Ahora que tenemos todo lo demás configurado, es hora de crear la plantilla misma.
Primero, aquí se explica cómo agregarlo. A continuación se explicará lo que significa cada paso.

1. Seleccione el primer renglón de subtítulo del archivo.
1. Seleccione _Subtítulos_→_Insertar renglones_→_Antes del actual_ para crear un nuevo renglón anterior. Este se convertirá en nuestra línea de plantilla de karaoke. No es necesario que sea el primero, pero generalmente hace que sea más fácil de encontrar en adelante.
1. Asegúrese de que la línea recién creada tenga el mismo _estilo_ que su karaoke sincronizado.
1. Haga clic en la casilla para _Comentario_ para la nueva línea. Debe de cambiar de color en la cuadrícula de subtítulos.
1. Busque el campo _Efecto_, que está a la derecha de los campos _Estilo_ y _Actor_. Coloque el texto "`template line`" en él (¡Sin las comillas!). Presione la tecla _Enter_ en su teclado para guardar el campo Efecto.
1. Finalmente, ingrese este texto como texto principal de la línea de su plantilla. Termine con _Enter_ nuevamente. `{\r\t($start,$mid,\fscy120)\t($mid,$end,\fscy100)}`

{{<todo>}}Pantallazo de cómo se ve después de los pasos. {{</todo>}}

Ahora mire al menú _Automatización_ de nuevo. Si creó la línea plantilla correctamente, ahora estará disponible _Aplicar plantilla de karaoke_. Si no es así, revise los pasos anteriores de nuevo.

Seleccione _Aplicar plantillas de karaoke_ y observe cómo Karaoke Templater hace efecto.

{{<todo>}}Otro pantallazo, después de aplicar plantillas. {{</todo>}}

Si tiene un video abierto puede ver el efecto ahora mismo, dentro de Aegisub.

Fíjese también cómo la línea de la plantilla se dejó en su lugar y el karaoke sincronizado se cambió a líneas de comentarios, con _karaoke_ en sus campos de Efecto.
Karaoke Templater conserva su karaoke sincronizado dentro del karaoke con estilo para que no se le pierda. Pero también tiene otra función...

## Extendiendo un poco el efecto

Continuando desde arriba, ahora intente lo siguiente:

1. Cambie el texto de la línea de plantilla a: `{\r\k$kdur\t($start,$end,\1c&H00FF00&)\t($start,$mid,\fscy120)\t($mid,$end,\fscy100)}`
1. Aplicar plantillas nuevamente

{{<todo>}}Más pantallazos {{</todo>}}

Karaoke Templater reutilizó el karaoke sincronizado comentado y cambió el estilo del karaoke para que coincida con el nuevo efecto. También puede intentar cambiar el karaoke sincronizado comentado y aplicar plantillas nuevamente.

De esta manera, se puede trabajar gradualmente en un efecto y tener una vista previa a medida que avanza.

# Entonces ¿qué significa todo esto?

Para finalizar esta primera parte del tutorial, a continuación es lo que significa cada paso.
Esta no es la explicación completa de todo, pero debe de bastar por ahora.

- Las _Líneas de plantilla_ son líneas en el archivo de subtítulos marcadas de forma especial. Siempre deben ser líneas de comentario y la primera palabra en su campo de Efecto debe ser `template`.
- Existen varios tipos de líneas de plantilla. Solo usamos uno en este tutorial. Este tipo de línea de plantilla, o _clase de plantilla_, se llama _plantilla de línea_. Sí, puede resultar un poco confuso. Se llama así porque crea una línea de karaoke con estilo a partir de una línea de karaoke sincronizado. La segunda palabra en el campo Efecto de una línea de plantilla indica de qué clase es la plantilla. Para plantillas de línea, esta palabra es `line`.
- Entonces, el texto `template line` en el campo Efecto significa que se trata de una _línea de plantilla_ de _clase línea_.

<!-- -->

- Una plantilla sólo afecta las líneas de karaoke sincronizadas que tienen el mismo Estilo como la línea de plantilla.

<!-- -->

- Todo karaoke con estilo producido por Karaoke Templater tiene `fx` en el campo Efecto. Esto se utiliza como recordatorio para Karaoke Templater de que esta línea deben ser reemplazado, si las plantillas se aplican otra vez.

<!-- -->

- El texto principal de una línea de plantilla se denomina _texto de plantilla_. En plantillas _line_, cada etiqueta \\k se reemplaza con el texto de la plantilla.
- El texto de la plantilla puede utilizar varias _variables_. Estas son palabras cortas que empiezan con signo de dólar, como `$start`, `$end`, `$mid` y `$kdur`. Las variables se reemplazan con la información que almacenan para cada sílaba reemplazada.
- `$start` se reemplaza con la hora de inicio de la sílaba. Esta es en milisegundos desde el inicio de la línea. Es decir, un código de tiempo adecuado para colocar en las etiquetas \\t, \\move y \\fade.
- De manera similar, `$end` es el tiempo de finalización de la sílaba, también en milisegundos.
- Un poco más especial es `$mid`, que es el _tiempo intermedio_ de la sílaba, el tiempo justo en el medio de `$start` y `$end`. En nuestro ejemplo, lo usamos para hacer crecer cada sílaba durante la primera mitad de su duración, y volver a la altura normal para la segunda mitad. También es milisegundos.
- La variable `$kdur`, sin embargo, está en centisegundos. Este es el tiempo original de la etiqueta \\k, y es casi solo útil para poner nuevamente en una etiqueta \\k, como hicimos acá.

Con este conocimiento, ya debería poder crear muchos efectos. Es posible que también desee consultar la página sobre [etiquetas manuales ASS]({{<relref path="ASS_Tags">}}).

También puede [continuar con el siguiente tutorial]({{<relref path="./Tutorial_2" lang="en">}}), donde veremos cómo hacer cálculos con variables para conseguir más variación.
