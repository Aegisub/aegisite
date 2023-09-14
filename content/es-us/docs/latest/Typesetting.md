---
title: Introducción a la composición tipográfica/Typesetting
menu:
  docs:
    parent: typesetting
    name: Intro a la composición tipográfica
weight: 4000
---

La definición (traducida) de Wikipedia de
[typesetting/composición tipográfica](http://en.wikipedia.org/wiki/Typesetting): "**Typesetting** es la presentación de texto en forma gráfica en papel o algún otro medio." En el contexto del subtitulado, significa tres cosas:

<!-- TODO here -->
- Presentar (una traducción de) el diálogo hablado al espectador de una manera fácil forma legible y visualmente agradable.
- Traducir cualquier texto de fondo en un idioma extranjero (como títulos de episodios, información de la escena como tiempo/lugar y otros escritos importantes para la trama sobre cosas en el fondo) y presentando la traducción al espectador, preferiblemente de modo que parece que la traducción estuvo allí todo el tiempo (aunque conservando legibilidad).
- Diseñar otros textos (logotipos, karaoke, etc. etc.) que deben ser mostrado en el vídeo.

Particularmente en la comunidad fansub, la palabra "typesetting" generalmente se refiere al segundo o tercero de estos tres.

Esta página intentará brindarle una introducción a la composición tipográfica de subtítulos.
Lamentablemente el buen gusto es difícil de enseñar, pero haremos lo mejor que podamos.

## Composición tipográfica de diálogos

El objetivo principal de la composición tipográfica de diálogos es la **legibilidad**; todo lo demás es
sólo la guinda del pastel. De nada sirve tener subtítulos si el espectador
No puedo leerlos. Recuerde que los subtítulos frecuentemente requieren una lectura bastante rápida,
por lo que la facilidad de reconocimiento es vital. Algunas pautas para una buena legibilidad:

- Utilice un tipo de letra sencillo, ordenado y sensato. Fuentes sans-serif (o si insisten en serifas, fuentes "slab serif") son generalmente preferibles, especialmente en resoluciones de video bajas, ya que las serifas tienden a quedar borrosas, lo que naturalmente Se ve mal. También se deben evitar fuentes demasiado finas. Las fuentes en versalitas son malas porque los ascendentes/descendentes de ayudan al reconocimiento de palabras. Usando probado y caras de confianza como Helvetica, Arial o Verdana no están nada mal; si quieres algo que parezca menos "aburrido" pero aún legible, prueba un fuente sans-serif del tipo "humanista", como Calibri.
- Utilice un borde bien definido pero no demasiado grueso. El color es importante; el cuanto mayor sea el contraste con el color principal, mejor. El principal blanco La combinación de color y borde negro está bien probada y es confiable. La sombra es opcional; si si lo usa, considere configurarlo en negro semitransparente; negro sólido tiende perjudicar la legibilidad.
- Utilice letras grandes y amigables con márgenes cómodos; normalmente los subtítulos necesitan ser más grande de lo que cree para que sea fácilmente legible, especialmente en una pantalla de televisión
   (dado que la distancia de visualización en un televisor suele ser de 2 a 3 metros, en comparación con 0,3-0,6 m para una pantalla de ordenador). Si planeas mostrar tus subtítulos en un TV también es necesario realizar [overscan](http://en.wikipedia.org/wiki/Overscan)
   en cuenta; Aegisub tiene una función de máscara de sobreexploración (consulte [trabajar con vídeo]({{<relref path="Video">}})) que puede ayudarle con esto. Incluso si el resultado final no es va a ser visto en un televisor, los subtítulos que están en el área de sobreexploración Por lo general, no es muy legible de todos modos. Considere también la relación de aspecto del video; Las relaciones de aspecto 16:9 o más amplias te dan la oportunidad de tener más tiempo líneas a expensas del espacio vertical.
- Asegúrese de que no sean visibles más de dos líneas de texto a la vez
   (Se pueden hacer excepciones en momentos en los que hay mucha gente hablando en al mismo tiempo). A veces puedes comprimir el texto horizontalmente un poco para exprímelo; en otras ocasiones solo tienes que dividir el bloque de texto en dos líneas diferentes y se muestran una tras otra.

{{<todo>}}ejemplos {{</todo>}}

## Composición tipográfica "Firmar"

La composición tipográfica de letreros (traducir varios textos de fondo) generalmente puede ser
logrado con ASS, pero para efectos más complejos programas comerciales como
A veces se utiliza Adobe AfterEffects, ya que el santo grial de la composición tipográfica de signos
es hacer que el subtítulo parezca parte de la imagen que siempre estuvo
allá. Cómo llegar desde aquí no se discutirá en detalle en esta página.
(consulte el [tutorial de composición tipográfica]({{<relref path="Visual_Typesetting" lang="en">}})), pero aquí hay algunos
punteros:

- ¿Es el cartel realmente importante para la trama? Tratando de traducir cada uno Un fragmento de texto que se muestra en la pantalla te volverá loco rápidamente, y el final El resultado a menudo será ilegible de todos modos.
- Con frecuencia, el texto de un signo importante para la trama (como una carta) es en realidad leer en voz alta el diálogo; Si este es el caso deberías considerar omitir la tipografía de signos porque tener texto y diálogo puede sobrecargar al espectador con información. No deberías componer un cartel sólo para presumir.
   que eres capaz de hacerlo.
- ¿Podrás hacer que la traducción sea fácilmente legible? Por ejemplo, si usted Si tiene muy poco espacio disponible para acomodarlo, considere colocar un nota de traducción como un "título superior" normal.

{{<todo>}}imágenes {{</todo>}}

## Otras lecturas

La página de Wikipedia sobre [tipografía](http://en.wikipedia.org/wiki/Typography) tiene muchos enlaces útiles y explicaciones de varios términos relacionados con la tipografía.