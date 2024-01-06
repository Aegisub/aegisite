---
title: Trabajando con video
menu:
  docs:
    parent: typesetting
weight: 4100
---

Aegisub no es un reproductor de video (ni de media), pero aún así soporta abrir y trabajar con video de varias maneras. Esta página es una referencia de cómo el manejo de video de Aegisub funciona; para una intro más suave de cómo simplemente lograr que las cosas se muestren correctamente puede que quiera leer las páginas [Disposición visual de texto]({{<relref path="Visual_Typesetting" lang="en">}}).

## Abrir video

Para abrir un archivo video, vaya al menú _Video_ y dele a _Abrir archivo de video_. Cuáles archivos uno puede abrir depende de su [proveedor de video]({{<relref path="Options#video" lang="en">}}). Para usar un video de suplente (falso, vacío), pulse _Use video de suplente_.

### Formatos soportados

Aegisub normalmente usa [FFMS2](http://code.google.com/p/ffmpegsource/) para abrir
video, que admite la apertura de casi todos los formatos A/V comunes y muchos poco comunes. Para obtener una lista completa de códecs compatibles, consulte la documentación de [FFmpeg](http://ffmpeg.org/) o de [Libav](http://libav.org/). Tenga en cuenta que FFMS2 actualmente tiene problemas con H.264 entrelazado.

En Windows, se puede utilizar [Avisynth](http://avisynth.org/mediawiki/Main_Page)
en lugar de FFMS2. Al abrir a través de _Avisynth_, Aegisub probará varias funciones fuentes para encontrar la mejor opción:

`Import()`
: Función incorporada de Avisynth. Se usa para abrir scripts de Avisynth, nunca usado para cualquier otra cosa.

`AviSource()`
: Función incorporada de Avisynth. AviSource utiliza el decodificador Video para Windows (VfW) para abrir el video, que para algunos formatos esotéricos pueden ser la mejor o la única forma de abrir un archivo. Sólo admite archivos .avi, por razones obvias. Si AviSource no puede abrir un archivo, DSS2 se prueba, seguido de DirectShowSource.

`MPEG2Source()`
: Sólo se usa para cargar archivos .d2v (archivos proyecto DVD2AVI; también conocidos como archivos .VOB indexados extraídos de DVD). Intenta utilizar [DGDecode](http://neuron2.net/dgmpgdec/dgmpgdec.html) de neuron2 para abrir el archivo; si Aegisub no puede encontrarlo o cargarlo, probará con el antiguo `mpeg2dec3.dll` en su lugar; si eso también falla, devuelve un error. Esta es la forma más confiable de abrir videos DVD en Aegisub.

`DSS2()`
: Intenta buscar, cargar y utilizar el complemento DirectShowSource2 de Haali (viene
  con el paquete [Haali Media Splitter](http://haali.cs.msu.ru/mkv/)
  y con la [CCCP](http://cccp-project.net); el complemento Avisynth es
  _avss.dll_, debe colocarse manualmente en algún lugar donde Aegisub o
  Avisynth puede encontrarlo, vea más abajo). Eso a su vez intentará usar el entorno DirectShow de la computadora para abrir el archivo. En teoría cualquier archivo renderizable por DirectShow debe de ser compatible, pero como uno está a la merced de divisores y decodificadores de terceros, su experiencia puede variar.
  Como regla general, si se puede reproducir en Windows Media Player, Aegisub
  debe de poder cargarlo. Tenga en cuenta que DSS2 convierte archivos de velocidad de fotogramas variable en constante. Normalmente esto es lo que se quiere y espera. Pero si uno quiere hacer subtítulos VFR reales, no lo es.

`DirectShowSource()`
: Usa DirectShowSource() (que se incluye con Avisynth) para intentar cargar el archivo. Básicamente es lo mismo que DSS2, pero mucho menos confiable y no converte VFR a CFR. Aviso: DSS es conocido por tener dificultad con saltos con precisión a fotograma. No lo use si se puede evitar.

Tenga en cuenta que [VFR]({{<relref path="Video#variableframeratevideo">}}) no es compatible con el proveedor Avisynth. en algunos casos cargar [códigos de tiempo externos]({{<relref path="Video#timecodes" lang="en">}})
puede funcionar, pero en la práctica muchas veces resulta en un lío descompuesto.

Aegisub buscará extensiones Avisynth en su carpeta
[?data]({{<relref path="Aegisub_path_specifiers#?data" lang="en">}}) (generalmente la carpeta en donde está `aegisub32.exe`, en Windows). También se los puede colocar directamente en la carpeta plugins/extensiones Avisynth para autocargarlos.

### Video de suplente

Aegisub también permite proporcionar una superficie de video falsa sobre la que renderizar subtítulos sin tener ningún video real cargado. El cuadro de diálogo de video de suplente se ve así:

![Dummy_video](/img/3.2/Dummy_video.png#center)

Resolución
: La resolución del video de suplente en píxeles. Hay algunos
  opciones predefinidas en el menú desplegable; también se puede especificar el tamaño uno mismo. Tenga en cuenta que, dado que el video de suplente es RGB, no hay restricciones particulares con respecto a anchos/altos impares.

Color
: El color de la superficie del video. El color es sólido por defecto; enmarque la casilla "patrón tablero de ajedrez" si desea más variación.

Fotogramas por segundo
: Determina cuánto tiempo se muestra cada fotograma por configurar el número de
  fotogramas por segundo (fps). Tenga en cuenta que de hecho es posible cargar códigos de tiempo VFR con video de suplente.

Duración
: La duración del video en fotogramas. Debajo de este número se muestra la duración resultante en horas/minutos/segundos.

## Reproducir video

Aegisub sí permite reproducir el video, pero ha sido ampliamente debatido por si sea o no una función equívoca.

### Antes de ponerle "play"

Piénselo bien. ¿Realmente **quiere** reproducir el video? (Pista: la respuesta
es "no", no lo quiere hacer, al menos no en Aegisub.) Si se quiere comprobar si un subtítulo coincide con algo en el video, ¿no sería más fácil recorrer el video cuadro por cuadro con las teclas de flecha? Si está viendo de prueba, sería una mejor idea verlo en un reproductor que los espectadores realmente usarían.

Para concluir: en situaciones del mundo real, nunca va a necesitar reproducir el video dentro de Aegisub. El mantra es: Aegisub no es un reproductor multimedia; si quiere un reproductor multimedia, utilice un reproductor multimedia. No obstante, Aegisub hace un razonable esfuerzo para proveer una reproducción de video confiable y, en la práctica, generalmente funcionará bien.

Tenga en cuenta que el audio debe cargarse explícitamente para que Aegisub lo reproduzca mientras se reproduce el video. Si esto le resulta molesto, existe una opción para automáticamente abrir el audio cada vez que se abre un archivo de video.

## Fotograma clave

Una explicación breve y muy simplificada de qué es un fotograma/cuadro clave, para la gente que se perdió de video 101:

Los códecs de video modernos comprimen el video almacenando tan poca información como sea posible. En lugar de almacenar todos los fotogramas completos (como una gran cantidad de fotos JPG), ocasionalmente sacan un fotograma clave, que se almacena por completo, y para cada fotograma después, hasta el siguiente fotograma clave, solo almacenan lo que cambió en la imagen desde el fotograma anterior. Por lo tanto, para buscar cualquier marco, el decodificador necesita encontrar el fotograma clave anterior y decodificar todos los fotogramas entre ese y la meta, lo cual significa que buscar fotogramas clave es más rápido que buscar otros. Los fotogramas clave son interesantes principalmente por motivos de sincronización de la escena, porque suelen aparecer en los cambios de escena. El primer fotograma de una escena es
casi invariablemente un fotograma clave, pero tenga cuidado: ¡para nada esto quiere decir que cada fotograma clave sea un cambio de escena! La mayoría de los codificadores insertan un fotograma clave al menos una vez cada 250-300 fotogramas, incluso si no ha habido un cambio de escena.

Aegisub utiliza los datos de fotogramas clave en varios lugares del programa. Están dibujados como líneas negras en la barra de búsqueda de video y (de forma predeterminada) también se muestran en la barra del analizador de audio de forma de onda/espectro.

### Abrir y guardar datos de fotogramas clave

Al abrir un video a través de FFMS2, Aegisub admite la lectura de datos de fotogramas clave desde la mayoría de los formatos de archivo, mientras que el proveedor Avisynth solo admite la lectura de fotogramas clave de AVI. Si uno está utilizando un formato de video cuyos fotogramas clave no se pueden leer,
aún se puede cargar datos de fotogramas clave por separado. Aegisub actualmente admite la lectura desde varios formatos: su propio formato de archivo de fotogramas clave (consulte las especificaciones a continuación), archivos de primer paso XviD, archivos primer paso DivX y archivos primer paso x264.

Incluso si los fotogramas clave se pueden leer desde el archivo, a veces es útil sobreescribirlos con fotogramas clave externos. Uso de archivos .stat de primer paso XviD para sincronizar con audio es bastante popular, ya que las opciones de fotogramas clave de XviD se correlacionan inusualmente bien con cambios de escena.

Aegisub también puede escribir los datos de fotogramas clave actualmente cargados en un nuevo archivo de fotogramas clave, lo que puede resultar útil para evitar demasiado intercambio de archivos de video en algunas situaciones (sincronización de audio, por ejemplo).

### Especificación de archivo fotogramas clave

Un archivo de fotogramas clave es un archivo de texto codificado en ASCII; tanto \\n como \\r\\n son reconocidos como saltos de línea. Ejemplo de sintaxis:

```plaintext
# keyframe format v1
fps 0
0
30
70
82
130
131
```

La primera línea es la especificación del formato: el texto `# keyframe format v1` La segunda línea contiene el FPS del video utilizado para generar los datos del fotograma clave; sin embargo, no hay ningún programa (incluido Aegisub) hasta la fecha que en realidad admite esto y, por lo tanto, normalmente es solo `0` Finalmente, después del renglón fps, sigue una cantidad arbitraria de números enteros largos (uno por renglón), cada uno de los cuales que representa el número de fotograma de un fotograma clave. Los números de fotograma están indexados desde cero; es decir, el primer fotograma del video es el fotograma número 0.

## Video de velocidad de fotogramas variable

Aegisub admite la carga y el trabajo con video de velocidad de fotogramas variable El cómo y por qué de VFR está muy fuera del alcance de este manual (véase por ejemplo [el hilo VFR en AnimeSuki](http://forums.animesuki.com/showthread.php?t=34738) o la [página del manual de Avisynth](http://avisynth.org/mediawiki/VFR) para obtener más información sobre VFR), pero hablaremos lo que hay que saber sobre cómo Aegisub lo maneja.

### Códigos de tiempo

La carga de archivos de código de tiempo Matroska (v1 y v2) es compatible y útil si tiene un archivo de video VFRaC (velocidad de fotogramas presumida constante; por ejemplo, los fotogramas de un MKV VFR almacenados en un AVI a un FPS constante, consulte el hilo VFR vinculado arriba para más detalles) pero quiere que los subs se sincronicen con él. Si carga un archivo VFR, Aegisub leerá automáticamente los códigos de tiempo directamente.

### VFR e incrustar subtítulos (hardsubbing)

Mientras no esté codificando con GDSMux, el entorno de codificación en el que su filtro de subtítulos esté funcionando (es decir, Avisynth, VirtualDub o mencoder) supondrá que el mundo es CFR (velocidad de fotogramas constante) y, por lo tanto, que el archivo de entrada es VFRaC. Esto obviamente es un problema ya que arruina la sincronización de los subtítulos. Aegisub proporciona una forma de solucionar este problema a través del filtro de exportación Framerate Transformation (transforme de velocidad de fotogramas), que toma la velocidad de fotogramas del archivo de entrada VFRaC y los códigos de tiempo, y luego cambia cada código de tiempo y etiqueta manual en el guion para que pueda ser incrustado en el video VFRaC y aún sincronizar perfectamente después de aplicar los códigos de tiempo. Para preparar un guion para incrustar subtítulos, asegúrese de tener los códigos de tiempo cargados y luego vaya al menú _Archivo_ y dele a _Exportar_. Anule todo excepto el filtro _Transformar velocidad de fotogramas_. Elija el modo de salida _Variable_. Necesita saber el FPS del video en el que va a incrustar los subtítulos; si uno tiene el video cargado Aegisub sacará el FPS de ese video y lo insertará en el cuadro automáticamente.

**Nota:** si tiene cargado un archivo Matroska u otro archivo VFR, recuerde que el valor de FPS que informa Aegisub puede no ser el mismo que el del video en que va a incrustar los subtítulos.

## Video anamórfico

**Ó: Cómo evitar que se vean estirados los subtítulos**

Los siguientes párrafos suponen un conocimiento práctico de qué es el video anamórfico y de cómo funcionan las relaciones de aspecto. Si uno no está seguro, puede que quiera consultar una [introducción gradual pero bastante completa](http://www.hometheaterhifi.com/volume_6_4/feature-article-enhanced-widescreen-november-99.html).

### Estiramiento de imagen y rederizaje de subítulos

Una imagen anamórfica necesita ampliarse hasta alcanzar la relación de aspecto adecuada antes de presentarse al espectador. En una computadora, esto generalmente se hace mediante el renderizador de video, y aquí radica un problema. La mayoría de los renderizadores de subtítulos (incluido VSFilter, el actual renderizador "estándar") dibuja los subtítulos en la imagen antes de que se estire, y dado que el renderizador no tiene conocimiento de complicaciones por la relación de aspecto, los subtítulos se ampliarán juntos con la imagen cuando se reproduzca el video para el espectador y así se verán estirados. Aegisub renderiza sus subtítulos de esta manera también (ya que de esa manera será consistente con la mayoría de los reproductores); uno puede probar cómo se ve usando la opción "Anular relación de aspecto" en el menú de video.

### Compensar el estiramiento

Afortunadamente es fácil compensar el estiramiento, ya que se sabe cuánto se estirará la imagen (ya que se conocen sus dimensiones originales y la relación de aspecto de la pantalla). Calcule de qué porcentaje será la imagen estirada en la dirección X o Y, y luego fije el `ScaleX` o `ScaleY` en el [estilo]({{<relref path="Styles">}}) (o use [etiquetas]({{<relref path="ASS_Tags">}} `\fscx` o `\fscy`)) con la misma cantidad, pero de sentido contrario.

Ejemplo: tenemos una imagen de 704x480 que sabemos que se mostrará en formato 16:9 (o 1.7777...:1). Si presumimos que el reproductor estirará el ancho y dejará intacto el alto, esto significa que el nuevo ancho será:

```plaintext
(16/9) * 480 = 853.333...
```

cuyo porcentaje es:

```plaintext
853.333... / 704 = 1.212121...
```

es decir, 121%. Por lo tanto, para compensar este estiramiento horizontal (dirección X) configuramos `ScaleY` en todos nuestros estilos al 121% para estirar los subtítulos por la misma cantidad, y después de renderizarlos ya no se verán estirados.

**Ó** podemos hacer el estiramiento en la otra dirección, suponiendo que en su lugar el reproductor cambie el alto de la imagen. Usando la misma imagen: 
704 / (16 / 9) = 396
que corresponde a:
396/480 = 0.825
o 82.5%, lo que significa que podemos compensar la compresión vertical (Y) fijando `ScaleX` en 82.5%.

### Advertencias

Ambos métodos anteriores le dan a los subtítulos la relación de aspecto adecuada, pero eependiendo de cómo el reproductor haga el estiramiento, es posible que se vean variaciones sutiles del tamaño de subtítulos. Aegisub (y de hecho la mayoría de los reproductores y renderizadores de video) siempre cambia el ancho de la imagen y nunca el alto, excepto si se elige la relación de aspecto "personalizado" y especifica una resolución. Tenga en cuenta que si utiliza el contenedor Matroska, puede especificar la resolución de pantalla directamente, pero su compatibilidad con reproductores varía.

Tenga en cuenta que algunos renderizadores de subtítulos extraños (sobre todo el renderizador incorporado de Media Player Classic) son en realidad parte del renderizador de video y que harán el renderizado de subtítulos _después_ del estiramiento anamórfico, lo que da como resultado un estiramiento de subtítulos y mucha frustración. Con el renderizador libass de MPlayer, puede de hecho especificar si los subtítulos deben dibujarse antes o después del estirado usando el parámetro `-vf` para mover el renderizador de subtítulos dentro de la cadena de filtros.

### Lectura continuada

Para obtener más información sobre el video anamórfico y las relaciones de aspecto en general (un tema profundamente confuso que a primera vista parece simple) los siguientes enlaces pueden ser de interés:

- [Una guía rápida a la resolución de video digital y la conversión de relaciones de aspecto](http://lipas.uwasa.fi/~f76998/video/conversion/) - Lectura absolutamente esencial para cualquiera que quiera entender realmente el tema, aunque desafortunadamente, mucho más que todo lo que la mayoría de la gente haya querido saber.
- [Widescreen.org: Relaciones de aspecto](http://www.widescreen.org/aspect_ratios.shtml) - la historia y razones detrás de algunas relaciones de aspecto comunes.
- [Wikipedia: Relación de aspecto (imagen)](<http://en.wikipedia.org/wiki/Aspect_ratio_(image)>)
- [Wikipedia: pantalla ancha anamórfica](http://en.wikipedia.org/wiki/Anamorphic_widescreen)

## El menú de video

Las siguientes opciones están disponibles desde el menú de video:

### Relacionado con archivo fuente

Abrir video
: Abre video. Tenga en cuenta que si intenta abrir otro video con video
  ya cargado, el video original se cerrará primero.

Cerrar video
: Cierra el video actualmente abierto.

Reciente
: Enseña la lista de videos abiertos recientemente.

Usar video suplente
: Abre un video de suplente (véase arriba).

Mostrar detalles del video
: Demuestra alguna información sobre el video actualmente abierto. Detalles mostrados son el nombre de archivo, cuadros/fotogramas por segundo (para archivos VFR, el FPS promedio), resolución y relación de aspecto, duración y decodificador. Decodificador siendo qué filtro/método utilizó Aegisub para abrir el archivo.

### Relacionado con códigos de tiempo

Abrir archivo de códigos de tiempo
: Carga un archivo de códigos de tiempo y lo aplica al video, cambiando la sincronización de video/subtítulos.

Guardar archivo de códigos de tiempo
: Guarda los códigos de tiempo actualmente cargados como un nuevo archivo de códigos de tiempo v2.

Cerrar archivo de códigos de tiempo
: Quita los códigos de tiempo actualmente cargados.

Reciente
: Muestra la lista de archivos de códigos de tiempo abiertos recientemente.

### Relacionado con fotogramas clave

Abrir fotogramas clave
: Carga datos de fotogramas clave del archivo dado. Si ya tiene datos de fotograma clave cargados, serán reemplazados por los leídos del archivo.

Guardar fotogramas clave
: Guarda los datos de fotogramas clave actualmente cargados en un archivo de fotogramas clave.

Cerrar fotogramas clave
: Quita los datos de fotogramas clave actualmente cargados, si los hay. Tenga en cuenta que no es posible quitar datos de fotogramas clave que se cargaron directamente desde el archivo de video. Si quieres deshacerse de eso por alguna razón, cargue un archivo de fotogramas clave con solo el fotograma 0 marcado como fotograma clave.

Reciente
: Enseña la lista de archivos de fotogramas clave cargados recientemente.

### Relacionado con muestra/pantalla

Desconectar video
: Desconecta la pantalla de video y los controles relacionados de la ventana de Aegisub principal y la mueve a su propia ventana. Para volver a adjuntar el video a la ventana principal, cierre la ventana separada. Esta característica puede ser particularmente útil en configuraciones de múltiples monitores.

Establecer zoom
: Establece el nivel de zoom del video.

Especificar relación de aspecto
: Estira el video a la relación de aspecto especificada modificando el
  ancho del video. Útil para video anamórfico (véase arriba).

Mostrar capa de sobredesviación/overscan
: Dibuja una capa azul sobre la imagen, indicando las fronteras de las
  zonas seguras para acciones (azul oscuro) y seguras para títulos (azul claro). Útil si piensa mostrar los subtítulos en un televisor sin correción de sobredesviación ajustable. Para obtener más información, consulte las páginas de Wikipedia en [sobredesviación](http://en.wikipedia.org/wiki/Overscan), [zonas seguras](http://en.wikipedia.org/wiki/Safe_area) y [cantidades de sobredesviación](http://en.wikipedia.org/wiki/Overscan_amounts). Aegisub sigue las [recomendaciones BBC](http://www.bbc.co.uk/guidelines/dq/pdf/tv/tv_standards_london.pdf) con respecto a qué tan grandes deberían ser las zonas seguras.

### Relacionado con saltos

Saltar a
: Salta en el video al tiempo o fotograma indicado.

Saltar al inicio del video
: Salta el video hasta el inicio del renglón actualmente activo.

Saltar al final del video
: Salta el video hasta el momento fin del renglón actualmente activo.
