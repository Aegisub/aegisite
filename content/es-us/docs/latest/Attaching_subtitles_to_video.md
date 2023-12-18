---
title: Aplicar subtítulos
menu:
  docs:
    parent: working-with-subtitles
weight: 3200
---

En codificación digital, existen dos métodos principales de incluir subtítulos en un video: subtítulos _soft/sueltos_ y subtítulos _hard/incrustados_. Ambos métodos tienen ventajas y desventajas distintas, junto con varios argumentos a favor y en contra de cada método.

## Incrustación/Hardsubbing

Hardsubbing es un método que "graba" subtítulos en la parte fotográfica de una película. Los subtítulos encrustados digitales son muy parecidos a las cintas VHS subtituladas; los subtítulos no pueden apagarse.

### Ventajas del Hardsubbing

El hardsubbing suele ser mucho menos exigente para el dispositivo de reproducción. Dado que el texto ya es parte del video, requiere tanto procesamiento como el video sin subtítulos requeriría y nada más. A menudo también se pueden crear efectos especiales que serían difíciles de replicar en un formato de subtítulos sueltos, debido a la gran cantidad de CPU necesaria para renderizarlos. Incluso en ánime con subtítulos sueltos de fansubs, los de karaoke de apertura y cierre a menudo son incrustados debido a los efectos especiales utilizados.

Algunos argumentan que con los subtítulos incrustados, los guiones son más difíciles de robar, ya que el texto está incrustado en la imagen: los ladrones no pueden simplemente extraer los subtítulos como de un sub suelto. Sin embargo, la presencia de muy buenos extractores de subtítulos diseñados para el propósito de extraer este texto incrustado elimina gran parte del argumento de que los incrustados eviten el robo de guiones.

Muchos dispositivos de reproducción y plataformas informáticas no pueden mostrar las tipografías y formatos especiales que contienen los subs sueltos, pero este problema se elimina con subs incrustados, donde se conserva el estilo. Además, estos estilos se mostrarán exactamente igual en cualquier dispositivo, a diferencia de los sueltos que dependen del dispositivo reproductor para interpretar y mostrar correctamente los estilos.

### Desventajas del Hardsubbing

A pesar de lo que algunos pueden llamar numerosas ventajas del hardsubbing, existen varias desventajas distintas que deben evaluarse antes de tomar una decisión.

El método de incrustación requiere que el video fuente se vuelva a codificar para que se puedan grabar los subtítulos sobre la imagen. Esto, por la naturaleza del video de codificación con pérdida, provoca una reducción en la calidad del video.

Los subtítulos añaden un fuerte contraste en una imagen de video debido a su naturaleza. Esto causará ruido de compresión a lo largo de los bordes del subtítulo codificado, y desenfoque del subtítulo. Este efecto es especialmente evidente a velocidades de bits más bajas.

En circunstancias típicas, la inclusión de subtítulos provocará un aumento en la velocidad de bits necesaria para que el video mantenga la misma calidad. Esto, como consecuencia, significa un tamaño de archivo mayor o una calidad menor con el mismo tamaño. El aumento necesario en la velocidad de bits suele ser de entre el 3 y el 10%.

Cambiar los subtítulos requiere volver a codificar la fuente del video, lo que puede agregar mucho tiempo y trabajo extra para el proceso de publicación.

## Subtítulos sueltos/Softsubbing

Softsubbing es un método que mantiene los subtítulos separados del video y que depende del dispositivo de reproducción para combinar los dos cuando se reproduce el video. Este método se puede comparar mejor con los subtítulos de la mayoría de los DVD. Los subtítulos pueden ser activados o desactivados según sea necesario, y se pueden admitir varios idiomas con solo un archivo multimedia combinado. Sin embargo, a diferencia de un DVD, los subs sueltos digitales son en realidad texto (los subtítulos del DVD son imágenes), lo que agrega muchas características útilos a costo de la complejidad.

### Ventajas del softsubbing

Los subs sueltos se muestran mucho más claros. Ya que no son parte de la imagen del video, la compresión de video no los afecta, y con un buen renderizador de subtítulos, son definidos y nítidos: un gran beneficio para la legibilidad.

Los subs sueltos pueden ser más pequeños. Dado que el subtítulo es sólo un archivo de texto, puede ocupar menos espacio porque no gasta la velocidad de bits del video. Esto permite que un codificador genere un archivo más pequeño con la misma calidad de video o un archivo del mismo tamaño con mayor calidad de video.

Las personas con problemas de visión tienen la oportunidad de ajustar la apariencia de los subtítulos en la pantalla.

Sin un gran impacto en el tamaño, se pueden admitir varios idiomas en un archivo de video.

Si uno encuentra un error de subtítulado en un archivo, puede solucionarlo sin tener que volver a codificar el video, ahorrando mucho tiempo.

### Desventajas del softsubbing

Los subs sueltos añaden complejidad de procesamiento al video. El dispositivo de reproducción tiene que renderizar y sobreponer el texto antes de mostrar el video. Como resultado, significa que los dispositivos de baja potencia no podrán reproducir el video.

Dado que los subtítulos están empaquetados como texto tal cual, son muy fáciles de extraer y usar. Esto le facilita el labor a los contrabandistas u otros ladrones de guiones. Nota que obtener subtítulos de un subtítulo incrustado es muy fácil actualmente, por lo cual este argumento no aguanta mucho peso.

El dispositivo de reproducción es responsable de mostrar los subtítulos en la pantalla. Como resultado, es posible que no tengan el mismo aspecto que pretendía el subtitulador. En algunos casos, es posible que el dispositivo de reproducción no admita el formato de subtítulos o que tenga errores con él.

El formato de archivo AVI no es confiable para admitir subs sueltos, si lo piensa usar. Tenga en cuenta que Matroska (MKV) es muy compatible con las computadoras, por lo que esto no es un aspecto negativo importante.

Subtítulos con efectos añadidos (típicamente para karaoke) requieren mucho tiempo de procesamiento y puede causar problemas de reproducción si el dispositivo no cumple con los requisitos de procesamiento. Una solución para esto es incrustar las secciones complejas como abrir y finalizar karaoke y dejar suelto el diálogo normal.

## ¿Qué método elijo?

El método que debe elegir depende en gran medida de su audiencia. ¿Tendrán dispositivos de reproducción relativamente nuevos y potentes? ¿Serán posiblemente capaces de instalar algo para reproducir subs sueltos si no lo tienen? ¿Es su destino un formato digital (Matroska, DVD, etc.) o se imprimirá en cinta?

Si bien cada situación será diferente, puede utilizar algunos de los siguientes sugerencias como guía. Estos se basan en realizar un formato digital para reproducción en una computadora.

Si desea que su archivo se pueda reproducir en la mayor variedad de computadoras,
sistemas y pequeños juguetes de plástico, querrá incrustar.

Si su audiencia se presentará en una plataforma donde su formato de subtítulos es bien compatible, subtitulado suelto es una buena idea.

Si desea tener varios idiomas de subtítulos o si algunos de sus espectadores pueden ni querer los subtítulos habilitados, los sueltos son su única opción.

Si desea acelerar el proceso de lanzamiento, utilice subs sueltos. Son más rápidos para corregir si se encuentra un error y le permite publicar tan pronto como se terminen los subtítulos, en lugar de esperar unas horas hasta que se codifique el video.

## Hardsubbing con Avisynth

Mucha gente usa la librería Avisynth para agregar filtros a su video para limpiarlo de defectos o manipular de otro modo la imagen de video antes de codificarla. Es una herramienta muy flexible y también se puede utilizar para agregar subtítulos directamente a la pista de video, lo que permite un método fácil y programable para substituir un video.

Si no está familiarizado con Avisynth, le recomendamos que lo investigue, ya que tiene muchas características interesantes y una gran comunidad que contribuye filtros de video, lo que permite corregir videos fácilmente de cualquier fuente. Este tutorial suponer que tenga algunos conocimientos básicos de Avisynth.

Para permitir agregar subtítulos a la pista de video, tiene dos opciones: puede usar VSFilter (incluido con Aegisub, en la carpeta "csri"), o puede usar
[AssRender](http://srsfckn.biz/assrender/), que utiliza `libass`. Las siguientes instrucciones suponen que está utilizando VSFilter.

Para simplemente agregar subtítulos, querrá crear un archivo AVS simple que contenga los renglones del guión que necesita. Empiece con un archivo de texto sin formato en el notepad (o en su editor de texto favorito) y guárdelo con la extensión `.avs` (tenga en cuenta que Windows quizá esté ocultando su extensión y que en realidad esté creando un archivo `.avs.txt`). Aquí hay un ejemplo:

```plaintext
LoadPlugin("c:\archivos de programa\aegisub\csri\vsfilter.dll")
AVISource("c:\proyectos\proyecto1\video\mycoolvideo.avi")
TextSub("c:\proyectos\proyecto1\subs\mainsubtitles.ass")
TextSub("c:\proyectos\proyecto1\subs\endkaraoke.ass")
```

El script anterior toma un archivo AVI (`mycoolvideo.avi`) y luego dibuja el contenido de dos archivos de subtítulos en el video. Luego uno puede codificar este video en cualquier programa que admita AVS, como [VirtualDub](http://www.virtualdub.org) o `x264`. Para hacerlo, simplemente abra el archivo `.avs` en el programa y siga el procedimiento de codificación normal para ello.

Tenga en cuenta que, debido a un error en VSFilter, la ruta a los archivos de subtítulos **TIENE QUE** ser absoluto.

## Hardsubbing con VirtualDub

Si ya está familiarizado con los filtros de VirtualDub y no tiene intención de hacer ningún otro procesamiento de video, debe tener en cuenta que es posible usar VSFilter como filtro para VirtualDub también. Simplemente cambie el nombre del `.dll` a `.vdf` y cópielo a la carpeta de complementos de VirtualDub. El filtro estará entonces disponible como "TextSub".

**Advertencia**: VirtualDub viene con un TextSub propio, que se llama
"TextSub 2.23". Esta es una versión muy antigua que, entre muchas otras cuestiones,
no puede analizar correctamente los archivos UTF-8 (la codificación Aegisub predeterminada). Esto causará que los caracteres que no sean ASCII se rendericen como texto sin sentido. NUNCA USE ESTE FILTRO.

## Subítulos sueltos

El subtitulado suelto de un video se puede realizar de varias formas. En Windows usando un reproductor DirectShow, como Media Player Classic, ZoomPlayer o incluso Windows Media Player, necesita VSFilter instalado para ver los subtítulos. Si usa MPlayer, necesita `libass` y FontConfig compilados para ver correctamente todo el formateo.

### Variante 1: Sub suave dentro del contenedor de video

Matroska Video (MKV) es actualmente el mejor contenedor para este método (MP4, OGM e incluso AVI técnicamente pueden contener subs sueltos, pero ninguno admite incluir archivos de fuentes tipográficos, y todos ellos tienen varios otros problemas). Usando un conmutador que admite archivos adjuntos (es decir, [mkvmerge GUI](http://www.bunkus.org/videotools/mkvtoolnix/)), simplemente agrega sus archivos de subtítulos al archivo Matroska como pistas separadas (al igual que agrega pistas de audio y de video) y cualquier fuente tipográfico como archivo adjunto (asegúrese de que tengan el formato MIME `aplicación/x-truetype-font`). Las fuentes se instalarán temporalmente por Haali Media Splitter (en Windows) o MPlayer (en \*nix y MacOS) durante la reproducción.

### Variante 2: Distribución de archivos de guión

Este método funciona mejor cuando desea codificar el video en un contenedor AVI. Uno solo envía los archivos de subtítulos sin procesar junto con el video. El espectador necesita entonces cargarlos en un reproductor que admita subtítulos externos. Al usar este método, debe asegurarse de, o utilizar tipografías que todos hayan instalado, o distribuir un archivo ZIP separado con las tipografías. Por razones obvias, no se recomienda este método.
