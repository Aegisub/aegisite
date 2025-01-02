---
title: Introducción a la composición tipográfica/Typesetting
menu:
  docs:
    parent: typesetting
    name: Intro a la composición tipográfica
weight: 4000
---

La definición (traducida) de Wikipedia de
[typesetting/composición tipográfica](http://en.wikipedia.org/wiki/Typesetting): "**Typesetting** es la presentación de texto en forma gráfica en papel u otro medio." En el contexto del subtitulado, significa tres cosas:

- Presentar (una traducción del) diálogo hablado al espectador de una manera legible y visualmente agradable.
- Traducir cualquier texto de fondo de idioma extranjero (títulos de episodios, información de la escena como tiempo/lugar y otros escritos importantes para la trama sobre cosas en el trasfondo) y presentar la traducción al espectador, preferiblemente de modo que parece que la traducción estuviera ahí todo el tiempo (pero siempre conservando legibilidad).
- Diseñar otros textos (logotipos, karaoke, etc.) que deben aparecer en el vídeo.

Particularmente en la comunidad fansub, la palabra "typesetting" generalmente se refiere al segundo o tercero de estos tres.

Esta página intentará brindarle una introducción a la composición tipográfica de subtítulos.
Lamentablemente el buen gusto es difícil de enseñar, pero haremos lo mejor que podamos.

## Composición tipográfica de diálogos

El objetivo principal de la composición tipográfica de diálogo es la **legibilidad**; todo lo demás es sólo la cereza del pastel. De nada sirve tener subtítulos si el espectador no los puede leer. Recuerde que los subtítulos frecuentemente requieren una lectura bastante rápida,
por lo que la facilidad de reconocimiento es vital. Algunas pautas para una buena legibilidad:

- Utilice un tipo de letra sencillo, ordenado y serio. Fuentes sin serifas (o si insisten en serifas, fuentes "slab serif") son generalmente preferibles, especialmente en resoluciones de video bajas, ya que las serifas tienden a quedar borrosas, lo que naturalmente se ve mal. También se deben evitar fuentes demasiado finas. Las fuentes de mayúsculas pequeñas en lugar de minúsculas son malas porque los ascendentes/descendentes de las letras ayudan al reconocimiento de palabras. Usar tipos de letra conocidos y confiables como Helvetica, Arial o Verdana no está nada mal; si quiere algo que parezca menos "aburrido" pero aún legible, pruebe una fuente sin serifas del tipo "humanista", tal como Calibri.
- Utilice un borde bien definido pero no demasiado grueso. El color es importante; cuanto mayor sea el contraste con el color principal, mejor. El combo relleno blanco con borde negro es bien probado y confiable. La sombra es opcional; si la usa, considere configurarla en negro semitransparente; negro sólido tiende a perjudicar la legibilidad.
- Utilice letras grandes y amigables con márgenes cómodos; normalmente los subtítulos necesitan ser más grandes de lo que uno espera para que sean fácilmente legibles, especialmente en una pantalla de televisión (dado que la distancia de visualización en un televisor suele ser 2-3 metros, en comparación con 0.3-0.6 metros para una pantalla de computadora). Si piensa mostrar sus subtítulos en un televisor, también es necesario tomar en cuenta la [sobredesviación/overscan](http://en.wikipedia.org/wiki/Overscan); Aegisub tiene una función de capa de sobredesviación (consulte [trabajar con vídeo]({{<relref path="Video#relacionado-con-muestrapantalla">}})) que puede ayudarle con esto. Además, incluso si el resultado final no se verá por televisor, los subtítulos que están en la zona de sobredesviación por lo general no son muy legibles. Considere también la relación de aspecto del video; las relaciones de aspecto 16:9 o más amplias le dan la oportunidad de tener renglones más largos a cambio de menos espacio vertical.
- Asegúrese de que no sean visibles más de dos renglones de texto a la vez (se permiten excepciones en momentos en los que hay mucha gente hablando al mismo tiempo). A veces se puede contraer el texto horizontalmente un poco para hacer que quepa. En otras ocasiones solo hay que dividir el bloque de texto en dos líneas diferentes y mostrarlas una tras otra.

{{<todo>}}ejemplos {{</todo>}}

## Composición tipográfica de "letrero/cartel"

La composición tipográfica de carteles (traducir varios textos de fondo) generalmente puede ser logrado con ASS pero para lograr efectos más complejos, programas comerciales como Adobe AfterEffects a veces se usan, ya que el resultado ideal de la composición tipográfica de carteles es hacer que el subtítulo parezca ser parte de la imagen original. Desde acá cómo llegar hasta ahí no se tratará en detalle en esta página (consulte el [tutorial de composición tipográfica]({{<relref path="Visual_Typesetting" lang="en">}})), pero a continuación hay algunos consejos:

- ¿Es el cartel realmente importante para la trama? Tratar de traducir cada fragmento de texto que aparece en la pantalla vuelve loco en seguida a cualquiera, y el resultado final a menudo será ilegible de todas formas.
- Con frecuencia, el texto de un cartel importante para la trama (como una carta) es en realidad leído en voz alta con el diálogo. Si este es el caso debería considerar omitir el subtitulado de ese cartel porque tener texto y diálogo puede sobrecargar al espectador de información. No se debe componer un cartel sólo para demostrar que uno es capaz de hacerlo.
- ¿Podrá hacer que la traducción sea fácilmente legible? Por ejemplo, si tiene muy poco espacio disponible para acomodarla considere colocar una nota de traducción como un título superior "sobretítulo" normal en su lugar.

{{<todo>}}imágenes {{</todo>}}

## Otras lecturas

La página de Wikipedia sobre [tipografía](http://en.wikipedia.org/wiki/Typography) tiene muchos enlaces útiles y explicaciones de varios términos relacionados con la composición tipográfica.
