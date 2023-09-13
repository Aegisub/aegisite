---
title: Aplicar subtítulos
menu:
  docs:
    parent: working-with-subtitles
weight: 3200
---

En codificación digital, existen dos métodos principales de incluir subtítulos en un vídeo: subtítulos _soft/sueltos_ y subtítulos _hard/incrustados_. Ambos métodos tienen ventajas y desventajas distintas, junto con varios argumentos a favor y en contra de cada método.

## Incrustación/Hardsubbing

Hardsubbing es un método que "graba" subtítulos en la parte fotográfica de una película. Los subtítulos encrustados digitales son muy parecidos a las cintas VHS subtituladas; los subtítulos no pueden apagarse.

### Ventajas del Hardsubbing

El hardsubbing suele ser mucho menos exigente para el dispositivo de reproducción. Dado que el texto ya es parte del video, requiere tanto procesamiente como el video sin subtítulos requisiera y nada más. A menudo también se puede crear efectos especiales que serían difíciles de replicar en un formato de subtítulos sueltos, debido a la gran cantidad de CPU necesaria para renderizarlos. Incluso en ánime con subtítulos sueltos de fansubs, los de karaoke de apertura y cierre a menudo son incrustados debido a los efectos especiales utilizados.

Algunos argumentan que con los subtítulos incrustados, los guiones son más difíciles de robar, ya que el texto está incrustado en la imagen: los ladrones no pueden simplemente extraer los subtítulos como de un sub suelto. Sin embargo, la presencia de muy buenos extractores de subtítulos diseñados para el propósito de extraer este texto incrustado elimina gran parte del argumento de que los incrustados eviten el robo de guiones.

Muchos dispositivos de reproducción y plataformas informáticas no pueden mostrar las tipografías y formatos especiales que contienen los subs sueltos, pero este problema se elimina con subs incrustados, donde se conserva el estilo. Además, estos estilos se mostrarán exactamente igual en cualquier dispositivo, a diferencia de los sueltos que dependen del dispositivo reproductor para interpretar y mostrar correctamente los estilos.

### Desventajas del Hardsubbing

A pesar de lo que algunos pueden llamar numerosas ventajas del hardsubbing, existen varias desventajas distintas que deben evaluarse antes de hacer una decisión.

El método de incrustación requiere que el vídeo fuente se vuelva a codificar para que se puedan grabar los subtítulos sobre la imagen. Esto, por la naturaleza del vídeo de codificación con pérdida, provoca una reducción en la calidad del vídeo.

Los subtítulos añaden un fuerte contraste en una imagen de vídeo debido a su naturaleza. Esto causará ruido de compresión a lo largo de los bordes del subtítulo codificado, y desenfoque del subtítulo. Este efecto es especialmente evidente a velocidades de bits más bajas.

En circunstancias típicas, la inclusión de subtítulos provocará un aumento en la velocidad de bits necesaria para que el video mantenga la misma calidad. Esto, como consecuencia, significa un tamaño de archivo mayor o una calidad menor con el mismo tamaño. El aumento necesario en la velocidad de bits suele ser de entre el 3 y el 10%.

Cambiar los subtítulos requiere volver a codificar la fuente del vídeo, lo que puede agregar mucho tiempo y trabajo extra para el proceso de publicación.

## Subtítulos sueltos/Softsubbing

Softsubbing es un método que mantiene los subtítulos separados del vídeo y se basa en el dispositivo de reproducción para combinar los dos cuando se reproduce el vídeo. Este Este método se puede comparar mejor con los subtítulos de la mayoría de los DVD. La subtitulación puede ser activar o desactivar según sea necesario, y se pueden admitir varios idiomas con solo un archivo multimedia combinado. Sin embargo, a diferencia de un DVD, los softsubs digitales son en realidad texto (los subtítulos del DVD son imágenes), lo que agrega muchas características interesantes al mismo tiempo.
costo de la complejidad.

### Ventajas del softsubbing

Los softsubs se muestran mucho más claros. Ya que no son parte del video.
imagen, la compresión de vídeo no les afecta, y con un buen subtítulo renderizador, son nítidos y nítidos: un gran beneficio para la legibilidad.

Los softsubs pueden ser más pequeños. Dado que el subtítulo es sólo un archivo de texto, puede ocupar menos espacio porque no acapara la velocidad de bits del video. Esto permite que un codificador cree un archivo más pequeño con la misma calidad de video o un archivo del mismo tamaño con mayor calidad de vídeo.

Las personas con problemas de visión tienen la oportunidad de ajustar la apariencia de los subtítulos en la pantalla.

Sin un gran impacto en el tamaño, se pueden admitir varios idiomas en un archivo de vídeo.

Si encuentra un error de subtitulado en un archivo, puede solucionarlo sin tener que hacerlo.
Vuelva a codificar el vídeo, ahorrando mucho tiempo.

### Desventajas del softsubbing

Los softsubs añaden complejidad de procesamiento al vídeo. El dispositivo de reproducción tiene que renderizar y superponer el texto antes de mostrar el vídeo, como resultado, esto significa que los dispositivos de baja potencia no podrán reproducir el vídeo.

Dado que los subtítulos están agrupados como texto simple, son muy fáciles de extraer.
y use. Esto facilita las cosas a los contrabandistas u otros ladrones de guiones. Nota que obtener subtítulos de un subtítulo duro es muy fácil actualmente, por lo que este argumento no aguanta mucho peso.

El dispositivo de reproducción es responsable de mostrar los subtítulos en la pantalla. Como un Como resultado, es posible que no tengan el mismo aspecto que pretendía el subtitulador. En algunos casos,
Es posible que el dispositivo de reproducción no admita el formato de subtítulos o que tenga errores.
con eso.

El formato de archivo AVI no es confiable para admitir softsubs, si planea usar
él. Tenga en cuenta que Matroska (MKV) es muy compatible con las computadoras, por lo que Esto no es un aspecto negativo importante.

Subtítulos con efectos añadidos (normalmentepara karaoke) requieren mucho procesamiento tiempo y puede causar problemas de reproducción si el dispositivo no puede manejar el procesamiento requisitos. Una solución para esto es endurecer las partes complejas como abrir y finalizar karaoke y suavizar el diálogo normal.

## ¿Qué método elijo?

El método que debes elegir depende en gran medida de tu audiencia. ¿Tendrán
¿Dispositivos de reproducción relativamente nuevos y potentes? ¿Serán posiblemente capaces de
¿Instalar algo para reproducir softsubs si no lo tienen? Es tuyo destino un formato digital (Matroska, DVD, etc.) o imprimirá en
¿cinta?

Si bien cada situación será diferente, puedes utilizar algunos de los siguientes sugerencias para guiarte. Estos se basan en realizar un formato digital para reproducción en un sistema informático.

Si desea que su archivo se pueda reproducir en la mayor variedad de computadoras,
sistemas y pequeños juguetes de plástico, querrás substituirlos.

Si su audiencia se presentará en una plataforma donde su formato de subtítulos es Los softsubs con buen soporte son una buena idea.

Si desea tener varios idiomas de subtítulos o si algunos de sus espectadores pueden No quiero tener subtítulos habilitados en absoluto, los softsubs son su única opción.

Si desea acelerar el proceso de lanzamiento, utilice softsubs. Son más rápidos para corregir si se encuentra un error y permitirle publicar tan pronto como se publiquen los subtítulos.
hecho, en lugar de esperar unas horas hasta que se codifique el vídeo.

## Hardsubbing con Avisynth

Mucha gente usa el paquete Avisynth para agregar filtros a su video para limpiarlo.
defectos o manipular de otro modo la imagen de vídeo antes de codificarla. Es un Herramienta muy flexible y también se puede utilizar para agregar subtítulos directamente al video.
Stream, lo que permite un método fácil y programable para substituir un vídeo.

Si no está familiarizado con Avisynth, le recomendamos que lo investigue.
ya que tiene muchas características interesantes y una gran comunidad que contribuye con videos.
filtros, lo que permite corregir vídeos fácilmente para cualquier fuente. Este tutorial asume que tener algunos conocimientos básicos de Avisynth.

Para permitir agregar subtítulos a la transmisión de video, tiene dos opciones: puede use VSFilter (incluido con Aegisub, en la carpeta "csri"), o puede usar
[AssRender](http://srsfckn.biz/assrender/), que utiliza libass. La siguiente Las instrucciones asumen que está utilizando VSFilter.

Para simplemente agregar subtítulos, querrás crear un archivo AVS simple que contenga el líneas de guión que necesitas. Simplemente cree un archivo de texto sin formato en el bloc de notas (o en su editor de texto favorito) y guárdelo con la extensión .avs (tenga en cuenta que Windows Es posible que esté ocultando su extensión y que en realidad esté creando un .avs.txt.
archivo). Aquí hay un ejemplo:

```texto sin formato
LoadPlugin("c:\archivos de programa\aegisub\csri\vsfilter.dll")
AVISource("c:\proyectos\proyecto1\video\mycoolvideo.avi")
TextSub("c:\proyectos\proyecto1\subs\mainsubtitles.ass")
TextSub("c:\proyectos\proyecto1\subs\endkaraoke.ass")
```

El script anterior tomará un archivo AVI (mycoolvideo.avi) y luego dibujará el Contenido de dos archivos de subtítulos en el vídeo. Luego puedes codificar este vídeo en cualquier programa que admita AVS, como [VirtualDub](http://www.virtualdub.org)
o x264. Para hacerlo, simplemente abra el archivo .avs en el programa y siga las instrucciones procedimiento de codificación normal para ello.

Tenga en cuenta que, debido a un error en VSFilter, la ruta a los archivos de subtítulos DEBE ser absoluto.

## Hardsubbing con VirtualDub

Si ya está familiarizado con los filtros de VirtualDub y no tiene intención de hacer ninguno otro procesamiento de video, debe tener en cuenta que es posible usar VSFilter como Filtro VirtualDub también. Simplemente cambie el nombre del .dll a .vdf y cópielo en el Carpeta de complementos de VirtualDub. El filtro estará entonces disponible como "TextSub".

**Advertencia**: VirtualDub viene con un TextSub propio, que se llama
"Subtexto 2.23". Esta es una versión muy antigua que, entre muchas otras cuestiones,
no puede analizar correctamente los archivos UTF-8 (la codificación Aegisub predeterminada). Esta voluntad provocar que los caracteres que no sean ASCII se representen como un galimatías. NUNCA USE ESTO FILTRAR.

## Substitución suave

La substitución suave de un vídeo se puede realizar de varias formas. En Windows usando DirectShow reproductor, como Media Player Classic, ZoomPlayer o incluso Windows Media Player,
necesita VSFilter instalado para ver los subtítulos. Si usas MPlayer, necesitas libass y FontConfig compilados para ver correctamente todo el formato.

### Variante 1: softsubs dentro del contenedor de video

Matroska Video (MKV) es actualmente el mejor contenedor para este método (MP4, OGM e incluso AVI técnicamente puede contener softsubs, pero ninguno admite fuentes archivos adjuntos, y todos ellos tienen varios otros problemas). Usando un muxer que admite archivos adjuntos (es decir, [mkvmerge GUI](http://www.bunkus.org/videotools/mkvtoolnix/)), simplemente agrega tu archivos de subtítulos al archivo Matroska como pistas separadas (al igual que agrega audio y pistas de vídeo) y cualquier fuente como archivo adjunto (asegúrese de que tengan el formato MIME).
escriba aplicación/x-truetype-font). Las fuentes se instalarán temporalmente por Haali Media Splitter (en Windows) o MPlayer (en \*nix y MacOS X) durante reproducción.

### Variante 2: distribución de archivos de script

Este método funciona mejor cuando desea codificar el video en un contenedor AVI. Tú
simplemente envíe los archivos de subtítulos sin procesar junto con el video. El espectador necesita entonces para cargarlos en un reproductor que admita subtítulos externos. Al usar este método, debe asegurarse de utilizar fuentes que todos puedan usar Se espera que haya instalado o distribuido un archivo ZIP separado con el fuentes. Por razones obvias, no se recomienda este método.
