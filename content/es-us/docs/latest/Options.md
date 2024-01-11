---
title: Opciones de Aegisub
menu:
  docs:
    parent: miscellaneous
weight: 7000
---
Aegisub es altamente configurable y por lo tanto tiene un gran número de opciones configurables por el usuario. Estas están disponibles en la caja diálogo de opciones, dentro del menú Ver. Esta página es una guía de todas las opciones disponibles.

Aegisub almacena toda su configuración en un archivo de texto llamado _config.json_, lo cual por defecto se encuentra en la carpeta [?user]({{<relref path="Aegisub_path_specifiers" lang="en">}}). Si uno quere restablecer Aegisub a sus opciones predeterminadas sin volver a instalarlo, se puede simplemente eliminar _config.json_ y luego reinicar Aegisub.

## General

![preferences-general](/img/3.2/preferences-general.png#center)

Comprobación automática de actualizaciones
: Si está habilitado, Aegisub comprobará periódicamente si hay una nueva versión disponible y le avisará si la hay. Requiere una conexión funcional a Internet, naturalmente.

Mostrar barra de herramientas principal
: Si está deshabilitado, la barra de herramientas principal de Aegisub está oculta.

Guardar el estado de UI (interfaz) en archivos de subtítulos
: De forma predeterminada, Aegisub guarda cosas como la posición de desplazamiento actual de la cuadrícula de subtítulos y el número de fila activa en el archivo de subtítulos para que pueda restaurarse automáticamente cuando vuelva a abrir el archivo. Sin embargo, si está trabajando con control de versiones para sus archivos de subtítulos, es posible que desee desactivarlo para reducir el ruido en los cambios.

Tamaño de ícono de barras de herramientas
: El tamaño de los íconos a usar en todas las barras de herramientas de Aegisub. Actualmente los únicos valores válidos son 16 y 24.

Cargar automáticamente archivos vinculados
: Cada vez que guarda un guion, Aegisub también almacena información sobre qué archivos de video, audio y códigos de tiempo abrió mientras trabajaba en él, dentro del propio guion. Esta opción decide qué hace Aegisub con estos archivos que están "vinculados" al guion al abrirlo. Si está configurado en "preguntar", Aegisub le preguntará al usuario si desea cargar los archivos vinculados. Si se establece en "nunca", Aegisub nunca cargará los archivos vinculados, y del mismo modo, si se establece en "siempre", Aegisub siempre intentará cargar los archivos vinculados (e informará un error si no se encuentran los archivos).

Niveles de deshacer
: El número máximo de cambios que se pueden deshacer. Cuanto mayor sea este valor, más memoria utilizará Aegisub.

Listas de recién usados
: Número máximo de elementos para recordar, aplicado a todas las listas de elementos recién usados en Aegisub. El impacto en la memoria al aumentarlos es trivial, pero las listas más grandes pueden resultar imprácticos de manejar.

### Estilos predeterminados

![preferences-default-styles](/img/3.2/preferences-default-styles.png#center)

## Audio

![preferences-audio](/img/3.2/preferences-audio.png#center)

Anclar desplazamiento en el cursor
: Cuando está habilitado, la vista de onda de audio se desplazará automáticamente para seguir el cursor de reproducción si se acerca demasiado a cualquiera de los bordes.

Encasillar marcadores por defecto
: Cuando está habilitado, Aegisub encasillará de forma predeterminada los marcadores de audio junto con otros marcadores en la visualización de audio (como fotogramas clave y los tiempos de inicio o finalización de otras líneas) al moverlos haciendo clic o arrastrándolos si están lo suficientemente cerca entre sí. El ajuste se puede activar o desactivar manteniendo presionada la tecla mayús/shift.

Rueda del mouse predeterminada de zoom
: Cuando está habilitado, la rueda del mouse ampliará la pantalla de audio horizontalmente de forma predeterminada y desplazará la pantalla de audio cuando se mantenga presionada la tecla ctrl. Si está deshabilitado, estos dos se intercambian.

Enfoque automático al posar cursor
: Si está habilitado, mover el cursor sobre la onda de audio le dará enfoque automáticamente (en lugar de requerir un clic).

Reproducir audio al entrar en vídeo
: Cuando está habilitado, el paso entre fotogramas reproduce el audio de cada fotograma.

Duración predeterminada
: La duración predeterminada de una nueva línea sin tiempo, en milisegundos.

Duración de entrada predeterminada
Duración de salida predeterminada
: La duración agregada al inicio de una línea mediante las funciones "agregar entrada" y "agregar salida". También se utiliza en (y es configurado por) el [postprocesador de sincronización]({{<relref path="Timing_Post-Processor" lang="en">}}).

Sensibilidad de inicio de arrastre de marcador
: La distancia en píxeles que se debe arrastrar un marcador para que se registre como arrastre. Los valores más altos reducen la posibilidad de cambios accidentales, a costa de una peor capacidad de respuesta.

Clic y arrastre izquierdo mueve marcador final
: Cuando está habilitado, hacer clic izquierdo fija el inicio de la línea en el punto picado, luego establecerá el fin de la línea en el punto hasta el que se arrastra, haciendo posible cronometrar una línea con un solo movimiento de clic y arrastrar. Cuando está deshabilitado, hacer clic izquierdo y arrastrar siempre actualiza solo la hora de inicio de la línea, al igual que el clic derecho con la hora de finalización.

Grosor de línea de frontera
: El ancho, en píxeles, de los marcadores de inicio y fin de línea.

Distancia máxima de encasillamiento
: Distancia máxima para encasillar marcadores con otros marcadores vecinos, en píxeles.

Mostrar líneas inactivas
: Controla cómo se dibujan las líneas que rodean la línea seleccionada actualmente en la onda de audio. "No mostrar" solo mostrará la línea actual. "Mostrar anterior" mostrará la línea anterior (en la cuadrícula, _no_ cronológicamente) en gris además de la línea actual. "Mostrar siguiente y anterior" mostrará las líneas antes y después de la línea actual (en la cuadrícula, _no_ cronológicamente). "Mostrar todo" mostrará todas las líneas en gris además de la línea actual.

Incluir líneas inactivas comentadas
: Si está deshabilitado, las líneas comentadas se omitirán al seleccionar qué líneas inactivas mostrar en la pantalla de audio (convirtiendo "Mostrar anterior" en "Mostrar la última línea no comentada antes de esta actual", y así sucesivamente).

### Opciones visuales

Fotogramas clave
: Si está habilitado, las líneas que marcan las posiciones de los fotogramas clave en el video se dibujarán en la forma de onda de audio cuando esté en el modo de sincronización de diálogo (el valor predeterminado).

Fotogramas clave de karaoke
: Si está habilitado, las líneas que marcan las posiciones de los fotogramas clave en el video se dibujarán en la forma de onda de audio cuando esté en el modo de sincronización de karaoke.

Dibujar el tiempo del cursor
: Si está habilitado, se dibujará una marca de tiempo que enseña el tiempo desde el inicio del archivo cerca de la parte superior del cursor de la onda de audio.

Posición del vídeo
: Si está habilitado, se dibuja una línea en la pantalla de audio que marca la hora de inicio del cuadro de video actual.

Estilo de forma de onda
: Selecciona cuál de los estilos de representación de formas de onda usar.

  Máximo + Promedio
  : La forma de onda es de dos tonos, lo que indica tanto el valor máximo de una muestra dentro del intervalo un píxel como, en un color más claro, el valor promedio de todas las muestras dentro del rango de tiempo.

  Máximo
  : La forma de onda muestra sólo el valor máximo, como lo hacían las versiones anteriores de Aegisub.

### Etiquetas de audio

Estas opciones controlan la apariencia de las etiquetas dibujadas en la vista de audio para las sílabas de karaoke.

Tipo de fuente
: La fuente tipográfica que se usará para las etiquetas de audio.

Tamaño de fuente
: El tamaño de fuente que se usará para las etiquetas de audio.

## Video
<span id="revisión"></span>

![preferences-video](/img/3.2/preferences-video.png#center)

Mostrar fotogramas clave en el control deslizante
: Cuando está habilitado, Aegisub dibujará marcadores de fotogramas clave en el control deslizante de búsqueda de video.

Buscar video para comenzar la línea en el cambio de selección
: Cuando está habilitado, cada vez que se cambia la línea activa, Aegisub buscará automáticamente el video en el primer cuadro de la nueva línea. Tenga en cuenta que esto se puede hacer manualmente haciendo doble clic en la cuadrícula o presionando Ctrl-1.

Mostrar siempre herramientas visuales
: Cuando está deshabilitada, las herramientas de composición tipográfica visual solo se representan cuando el mouse está sobre la pantalla de video.

Abrir audio automáticamente al abrir video
: Cuando está habilitado, cuando abre un archivo de video que también tiene datos de audio, Aegisub cargará automáticamente el audio.

Zoom predeterminado
: El nivel de zoom de vídeo predeterminado. Útil si tienes una pantalla muy grande o muy pequeña.

Paso de salto rápido en fotogramas.
: Decide qué tan grandes "saltos" hará Aegisub cuando uses la función de búsqueda rápida (Alt-flecha derecha y Alt-flecha izquierda). Medido en cuadros.

Ruta para guardar captura de pantalla
: Decide dónde Aegisub debe guardar las capturas de pantalla. El valor predeterminado es `?video`, lo que significa que se guardan dondequiera que esté el video, pero puedes cambiarlo a la ruta que desees. [Aegisub_path_specifiers]({{<relref path="Aegisub_path_specifiers" lang="en">}}) son compatibles. Otra opción directamente disponible en el menú desplegable es `?script`, que es dondequiera que esté el script.

### Resolución de guion

Usar la resolución del primer vídeo abierto
: Cuando está habilitado, Aegisub configurará automáticamente la resolución del guion a la resolución del video si abre un video y la resolución del guion aún no está configurada. Si esto está deshabilitado, Aegisub establece la resolución del script en un valor predeterminado configurable.

Igualar la resolución del vídeo al abrir
: Controla lo que Aegisub hará con respecto a la resolución del script cuando abres un video. Si se configura en "nunca", Aegisub no hará nada si la resolución del script no coincide con la resolución del video. Si está configurado en "preguntar", Aegisub le preguntará si desea cambiar la resolución del script para que coincida con la resolución del video si no coinciden. Si se configura en "siempre", Aegisub siempre volverá a muestrear el script para que coincida con la resolución del video automáticamente.

## Interfaz

![preferences-interface](/img/3.2/preferences-interface.png#center)

Habilitar sugerencias de llamadas
: Cuando está habilitado, Aegisub detectará cuando estás escribiendo una [etiqueta de anulación]({{<relref path="ASS_Tags">}}) y mostrará un pequeño cuadro con una breve referencia de la sintaxis de la etiqueta en cuestión hasta que cierres la etiqueta. Esto se denomina "consejo de llamada" y la función puede resultar familiar para los usuarios de varios IDE de programación.

Sobrescribir en cuadros de tiempo
: controla el comportamiento de todos los cuadros de edición de tiempo en el programa. De forma predeterminada, todos los cuadros de edición de tiempo en Aegisub se comportan como si hubiera presionado el botón Insertar,
   por lo que cada dígito que escriba sobrescribe lo que ya está allí, y no puede borrar los números que ya están allí, debe sobrescribirlos. Desmarcar esta casilla desactiva este comportamiento y hace que los cuadros de edición de tiempo se comporten como cuadros de edición de texto normales (casi).

Habilitar resaltado de sintaxis
: habilita o deshabilita el resaltado de sintaxis de etiquetas de anulación en el cuadro de edición principal.

Ruta a archivos de diccionario
: Decide dónde buscará Aegisub los archivos de diccionario para su corrector ortográfico y diccionario de sinónimos. De forma predeterminada, aparece en `?data/dictionaries`, pero si tiene sus propios diccionarios en el formato correcto en otro lugar, no dude en señalar a Aegisub allí.

Fuente
: decide la fuente y el tamaño de fuente utilizados para el cuadro de edición de subtítulos y otros cuadros de edición.

Máximo de caracteres por línea
: Si el valor del contador de caracteres es mayor que este número, el fondo se volverá rojo para alertarle que ha excedido la longitud máxima de línea. La longitud máxima no se aplica de ninguna otra manera.

Umbral de advertencia de caracteres por segundo
Umbral de error de caracteres por segundo
: Los umbrales en los que la columna CPS de fondo comienza a colorearse y cuando se alcanza el color del error.

Ignorar espacios en blanco
: Si está habilitado, los espacios en blanco no se incluirán en el recuento de caracteres.

Ignorar la puntuación
: Si está habilitado, la puntuación no se incluirá en el recuento de caracteres.

Cuadrícula de enfoque al hacer clic
: Cuando está habilitada, la cuadrícula de subtítulos actúa como su propia área del programa y puede tener foco, al igual que el audio o el video, y mientras lo hace, puede usar las teclas de flecha/rueda del mouse para desplazarse por ella, etc. por otro lado, si desactivas esta opción, el foco permanecerá donde estaba antes cada vez que hagas clic en la cuadrícula. Esto significa que ya no puedes usar atajos de teclado en la cuadrícula, pero por otro lado significa que puedes hacer clic en la cuadrícula para ir a una línea sin perder el foco de audio, etc. Úselo a su propia discreción.

Resaltar subtítulos visibles
: Cuando está habilitado, todas las líneas de subtítulos que están visibles actualmente en el fotograma del video (o al menos _deberían_ ser visibles; Aegisub no tiene en cuenta el alfa y ese tipo de trucos en este caso; solo se preocupa por el tiempo de la línea) se resaltarán en la cuadrícula con un color de fondo especial (consulte la opción "Línea en el fondo del marco" a continuación).

Ocultar símbolo de anulaciones
: El carácter que se mostrará en lugar de anular bloques si la ocultación de etiquetas está activa. Tenga en cuenta que, a pesar del nombre, puede haber más de un carácter si así lo desea.

Fuente
: Decide la fuente y el tamaño de fuente de todo el texto en la cuadrícula.

### Colores

![preferences-colours](/img/3.2/preferences-colours.png#center)

#### Vista de audio

Reproducir cursor
: El color del cursor de reproducción.

Inicio del límite de la línea
Fin del límite de línea
Límite de línea línea inactiva
: Los colores respectivos de los distintos marcadores de límites de línea.

Límite de sílaba
: El color de la línea límite de una sílaba en el modo karaoke.

### Esquemas de color

Controla la combinación de colores utilizada para la forma de onda/espectro y algunos de los elementos de la interfaz de usuario. Aegisub actualmente no tiene una interfaz de usuario para editar los esquemas de color o crear otros nuevos, pero si te sientes aventurero, puedes encontrarlos en config.json.

#### Resaltado de sintaxis

Normal
: El color del texto normal.

Soportes
: El color de los corchetes que inician/finalizan los bloques de anulación.

Barras y paréntesis
: El color de las barras invertidas y los paréntesis dentro de los bloques de anulación.

Etiquetas
: El color de los nombres de etiquetas dentro de los bloques de anulación.

Parámetros
: El color de los parámetros para anular las etiquetas.

Error
: el color de error para una sintaxis no válida dentro de un bloque de anulación.

Fondo de error
: Color de fondo para errores.

salto de línea
: Color para \\N, \\n y \\h fuera de los bloques de anulación.

Plantillas de karaoke
: Color para bloques de plantilla de karaoke en líneas de plantilla.

#### Cuadrícula de subtítulos

Primer plano estándar
Fondo estándar
: El color normal de las líneas de la cuadrícula. "Primer plano" es el color del texto y "Fondo" es obviamente el color de fondo.

Primer plano de selección
Fondo de selección
: El color de las líneas seleccionadas en la cuadrícula.

Fondo del comentario
Fondo del comentario seleccionado
: El color de fondo de las líneas comentadas y de las líneas comentadas seleccionadas.
respectivamente.

Primer plano de colisión
: El color del texto de las líneas cuyos tiempos se superponen con la línea actualmente activa.

Línea en el fondo del marco
: El color de fondo de las líneas actualmente visibles en el fotograma del vídeo.

Encabezamiento
Columna izquierda
Borde de línea activa
Líneas
: El color de las líneas de la cuadrícula y las columnas/encabezados fijos.

## Atajos de tecla

![preferences-hotkeys](/img/3.2/preferences-hotkeys.png#center)

Esta página enumera todas las teclas de acceso rápido configuradas actualmente en Aegisub y le permite agregar,
eliminarlos o cambiarlos.

### Contextos de atajos de tecla

Aegisub admite la configuración de diferentes teclas de acceso rápido dependiendo de qué parte del programa esté enfocada.

El grupo "Predeterminado" es para teclas de acceso rápido que deberían funcionar independientemente de lo que en Aegisub tenga actualmente el foco del teclado. Las teclas de acceso rápido configuradas de forma predeterminada se anulan por categorías más específicas cuando corresponde.

El grupo "Siempre" establece teclas de acceso rápido habilitadas por el modo Medusa, que se aplican en todas partes del programa y anulan todas las demás pulsaciones de teclas, incluida la escritura normal en cuadros de edición.

Todos los demás contextos de teclas de acceso rápido deben explicarse por sí solos.

### Definir atajos de tecla

Para modificar una tecla de acceso rápido, primero haga clic en la fila para seleccionarla, luego haga clic en el campo de tecla de acceso rápido de la fila y luego presione las teclas que deberían activar el comando. Acepte la nueva tecla de acceso rápido haciendo clic en otra fila.

Para agregar una nueva tecla de acceso rápido, seleccione el contexto al que desea agregar la tecla de acceso rápido y luego haga clic en el botón Nuevo. Ingrese el [nombre del comando]({{<relref path="Commands" lang="en">}}), luego configure la tecla de acceso rápido como cuando los editó.

## Respaldo

![preferences-backup](/img/3.2/preferences-backup.png#center)

### Guardar automático

Permitir
: Si está habilitado, Aegisub guardará periódicamente una copia del script en el que está trabajando en la ruta de guardado automático.

Intervalo en segundos
: ¿Con qué frecuencia Aegisub debe guardar automáticamente?

Camino
: decide dónde guardar las copias guardadas automáticamente de los scripts en los que estás trabajando. De forma predeterminada, establezca `autoguardado` en su directorio `?user` de Aegisub (consulte la
   [Aegisub_path_specifiers]({{<relref path="Aegisub_path_specifiers" lang="en">}}) página para más detalles).

Guardado automático después de cada cambio
: Si está habilitado, Aegisub guardará el archivo después de cada cambio realizado. Tenga en cuenta que esto actualmente causa algunos problemas con el sistema de deshacer.

### Respaldo automático

Permitir
: Si está habilitado, Aegisub guardará una copia de seguridad de cada script que abra inmediatamente al abrirlo. De forma predeterminada, se guarda en `?user/autoback/`, pero esto se puede cambiar (ver más abajo).

Ruta
: Decide dónde guardar las copias de seguridad automáticas de los scripts. Por defecto está configurado en `autoback` en su directorio Aegisub `?user`.

## Automatizar

![preferences-automation](/img/3.2/preferences-automation.png#center)

Camino básico
: un directorio base donde se colocan los scripts de automatización no cargados automáticamente. Se utiliza sólo para guardar rutas a archivos de script en los subtítulos.

incluir ruta
: Lista de directorios donde se buscan archivos y módulos incluidos. Los directorios están separados por un carácter de barra vertical, `|`.

Ruta de carga automática
: Lista de directorios en los que se buscan scripts al inicio, que luego se cargan automáticamente. Los directorios están separados por un carácter de barra vertical, `|`.

Nivel de seguimiento
: Cuando un script envía un mensaje a la consola de depuración, también puede especificar un nivel de seguimiento. Si el nivel de seguimiento de un mensaje es inferior al valor proporcionado aquí, el mensaje no se registra. Los nombres dados a los niveles son sólo sugerencias y no tienen ningún efecto en la ejecución del script.
   (es decir, un mensaje de nivel "Fatal" no hará que el script finalice).

Tarea prioritaria
: Prioridad dada al hilo de ejecución del script. Si está en un sistema de un solo núcleo/una sola CPU, tener esto a un nivel más bajo de lo normal hará que otros programas respondan mejor mientras los scripts de ejecución prolongada estén activos.

Recarga automática al exportar
: Recarga automáticamente los conjuntos de scripts especificados al [Exportar]({{<relref path="Exporting" lang="en">}}) Se abre el diálogo. En ese caso tendrás que pasar a la ventana [Automation/Manager]({{<relref path="Automation/Manager" lang="en">}}) y determinar la causa del error.

## Audio avanzado

![preferences-advanced-audio](/img/3.2/preferences-advanced-audio.png#center)

Proveedor de audio
: Qué backend usar para cargar audio. Actualmente sólo existen dos métodos.

_avisynth_ (solo Windows)
: Utiliza [Avisynth](http://www.avisynth.org) para cargar audio. Todos los tipos de archivos se cargarán con DirectShowSource(), excepto los archivos AVS que se abrirán con Import().

_FFmpegSource_
: Utiliza [FFMS2](http://code.google.com/p/ffmpegsource/) para cargar audio. Generalmente es más confiable que abrir a través de DirectShowSource, pero más lento debido a que primero tiene que indexar los archivos.

Independientemente de esta configuración, el lector PCM WAV interno siempre se probará primero para los archivos WAV.

Reproductor de audio
: Qué método utilizar para reproducir audio. Las opciones dependen de la plataforma.

_DirectSound_ (solo Windows)
: utiliza Microsoft DirectSound para reproducir audio. Este es el reproductor de audio mejor probado y más estable.

_DirectSound-antiguo_ (solo Windows)
: Implementación original de Aegisub del reproductor DirectSound. Si tiene problemas de reproducción de audio cuando utiliza el reproductor DirectSound, este puede funcionar mejor (pero probablemente no lo haga).

_pulse_ (solo Linux)
: Utiliza la [Arquitectura de sonido avanzada de Linux] (http://www.alsa-project.org/) para reproducir audio. ALSA es la arquitectura de sonido nativa de Linux y no está disponible en ningún otro sistema.

_pulse_ (Linux y otros sistemas tipo \*NIX)
: Reproduce sonido a través de un servidor de sonido [PulseAudio](http://pulseaudio.org/). Este es el reproductor de audio menos probado y con menos probabilidades de funcionar, y solo se recomienda si su configuración de audio hace que los reproductores que no sean de pulso sean indeseables.

_portaudio_
: Utilice la API [PortAudio](http://www.portaudio.com/) para reproducir sonido. PortAudio tiene diferentes implementaciones de reproducción en diferentes plataformas. En la mayoría de los Unices utiliza Open Sound System (OSS) para la salida. Actualmente es el único reproductor de audio de Windows que admite la selección del dispositivo de salida.

_openal_
: Utiliza la API [OpenAL](http://www.openal.com/) para reproducir audio. Este es el reproductor recomendado en OS X. Normalmente no se incluye en las compilaciones de Windows debido a que agrega una dependencia adicional con pocos beneficios.

### Caché

Tipo de caché
: Use RAM a menos que tenga muy poca, luego use el Disco Duro. El caché no es necesario ni se utiliza cuando se abren archivos PCM WAV. Si desactiva el almacenamiento en caché, la reproducción de audio puede volverse muy poco confiable.

Camino
Nombre del archivo
: Estas opciones determinan dónde se ubicará el caché de audio del disco duro. Sólo se utiliza si la caché está configurada en el disco duro. No debería necesitar cambiar esto a menos que tenga poco espacio en el disco. Para el nombre, la cadena espera un parámetro "%i" de estilo printf, que será reemplazado por un número. "%02i" se utiliza de forma predeterminada. No cambies eso a menos que sepas lo que estás haciendo.

### Spectrum

Calidad del espectro
: Determina la calidad de la visualización del espectro de audio. Una configuración de mayor calidad da como resultado un mayor uso de CPU y RAM. Cada configuración consecutiva utiliza un poco más de CPU que la anterior y el doble de RAM. Para audio con una frecuencia de muestreo de 48 kHz, un minuto de audio utiliza esta cantidad de memoria en las diferentes configuraciones:

<table class="table table-bordered table-condensed">
  <tr><th>0 "regular"</th><td>11 MB</td>
  <tr><th>1 "better"</th><td>22 MB</td>
  <tr><th>2 "high"</th><td>44 MB</td>
  <tr><th>3 "insane"</th><td>88 MB</td>
</table>

La cantidad de memoria utilizada no depende del número de canales.
(Aegisub siempre funciona en mono) o la profundidad de bits (el espectro siempre se calcula en punto flotante de 32 bits) del audio.

{{<todo>}}this is probably wrong {{</todo>}}

Memoria caché máxima
: la cantidad máxima de memoria que se utilizará para el almacenamiento en caché del espectro de audio. Los resultados de los cálculos para mostrar el espectro de audio se almacenan en caché para que el desplazamiento por el audio sea más fluido. La cantidad de visualización del espectro que se puede almacenar en caché en una determinada cantidad de memoria depende de la configuración de calidad anterior. El tamaño de caché predeterminado de 128 MB da como resultado un poco menos de 6 minutos de audio a 48 kHz en calidad 1. Si lo configura en menos de 5 MB, se utilizará el valor predeterminado de 128 MB. Probablemente no deberías configurar esto en más de 1/4 de la cantidad de RAM física instalada.

### Avisynth (solo Windows)

Mezclador descendente Avisynth
: Aegisub sólo puede utilizar audio mono (un solo canal). Esta opción determina qué función de Avisynth utilizar para convertir audio a mono.

Forzar frecuencia de muestreo
: convierte todo el audio abierto a la frecuencia de muestreo dada. Forzar la frecuencia de muestreo a la frecuencia de muestreo utilizada por su tarjeta de sonido (en lugar de que el reproductor de audio lo haga) puede mejorar potencialmente el rendimiento del audio y solucionar problemas de reproducción.

### FFmpegSource

Modo de manejo de errores de indexación de audio
: Qué hacer si se produce un error al indexar una pista de audio.

   _Ignorar_
   : Ignore el error y continúe decodificando el archivo. Este modo puede permitirle abrir algunos archivos corruptos, pero puede causar desincronización de audio/vídeo.

   _Claro_
   : Finge que la pista con el error no existe en el archivo.

   _Detener_ (predeterminado)
   : Detiene la indexación en el punto del error y devuelve todos los datos de audio antes del error. Este es el valor predeterminado debido a que los paquetes de audio corruptos al final de los archivos son bastante comunes.

   _Abortar_
   : Negarse a abrir el archivo en absoluto.

Indexar siempre todas las pistas de audio
: Si está deshabilitado, abrir un archivo de video solo indexará las pistas de video, lo que le obligará a volver a indexar el archivo para abrir pistas de audio del mismo archivo.

### Portaudio

Dispositivo de portaudio
: Qué dispositivo de salida usar al reproducir audio a través de portaudio.

## Video avanzado

![preferences-advanced-video](/img/3.2/preferences-advanced-video.png#center)

Proveedor de vídeo
: Decide qué método debe utilizar Aegisub para cargar el vídeo. Las opciones que tiene disponibles aquí dependen de cómo se compiló su copia de Aegisub y del sistema operativo que esté ejecutando. Existen las siguientes alternativas:

   _avisynth_ (solo Windows)
   : Utiliza [Avisynth](http://www.avisynth.org) para cargar vídeo. Versátil, admite la carga de casi todos los formatos comunes, así como archivos .d2v (DVD VOB indexados) si se suministra el complemento correcto. Tenga en cuenta que Aegisub puede instalar su propio avisynth.dll en lugar de utilizar la instalación de su sistema si así lo desea. Requiere decodificadores de Video para Windows para archivos AVI para obtener el mejor rendimiento. Utiliza DirectShow para la mayoría de los formatos, por lo que no se recomienda para nada más que AVI, d2v y abrir scripts de Avisynth.

   _FFmpegSource_
   : Utiliza [FFMS2](http://code.google.com/p/ffmpegsource/) para cargar videos. Generalmente la opción más confiable.

Proveedor de subtítulos
: Decide qué backend utiliza Aegisub para representar los subtítulos en el vídeo. Si instala renderizadores CSRI adicionales como VSFilterMod o xy-VSFilter (colocando los archivos dll en el directorio CSRI dentro del directorio de Aegisub), se enumerarán aquí junto con los predeterminados.

   *CSRI/vsfilter_textsub* (solo Windows)
   : Utilice VSFilter 2.40 para representar subtítulos. Este es el procesador de subtítulos estándar que define el formato ASS utilizado por Aegisub.

   _libass_
   : Utilice [libass](http://code.google.com/p/libass/) para representar subtítulos. libass es mucho más rápido que VSFilter y (en cierto modo) multiplataforma, pero desafortunadamente todavía tiene algunas diferencias de representación con respecto a VSFilter y problemas relacionados con las fuentes en Windows. Si está realizando una composición tipográfica compleja que será [softsubbed]({{<relref path="Attaching_subtitles_to_video#softsubbing" lang="en">}}), es una buena idea comprobar su trabajo tanto con VSFilter como con libass, como Un número cada vez mayor de usuarios utiliza libass.

Fuerza BT.601
: Suponga que todos los videos YUV son BT.601, para compatibilidad con VSFilter.

   Cuando VSFilter se utiliza como filtro DirectShow, siempre utiliza la matriz de color BT.601 para convertir los subtítulos de RGB a YUV. Esto significa que si el video usa BT.709 (como lo hacen la mayoría de los videos HD y ocasionalmente los DVD), los colores que coinciden con el video en Aegisub no coincidirán con el video en el reproductor. Esta opción hace que Aegisub siempre convierta videos a RGB usando BT.601, lo que hace que los colores que se muestran en Aegisub sean incorrectos, pero si los colores coinciden en Aegisub, coincidirán en el reproductor.

   Para hacer las cosas más interesantes, VSFilter usará el espacio de color *correcto* cuando se use como renderizador de subtítulos interno en MPC-HC, por lo que habilitar esta opción dará como resultado colores *no coincidentes* en ese caso. Como el ISR actualmente está roto de muchas maneras (por ejemplo, es imposible colocar los subtítulos con precisión), recomendamos no preocuparse por eso por ahora.

   Esta comparación puede aclarar esto:

   ![bt601](/img/3.2/bt601.png)

   Aegisub ahora escribe qué espacio de color se debe usar para las conversiones RGB -> YUV al archivo de subtítulos, por lo que esperamos que este lío se resuelva mediante mejoras en el renderizador en algún momento en el futuro.

### Avisynth

Permitir Avisynth anterior a 2.56a
: Admite el uso de versiones antiguas de Avisynth que algunas personas se niegan a actualizar por varias malas razones.

Límite de memoria de Avisynth
: Límite de memoria caché de fotogramas para Avisynth. Por lo general, aumentar esto no mejora el rendimiento y solo debe hacerse si está abriendo directamente scripts de Avisynth demasiado complicados.

### FFmpegSource

Detalle del registro de depuración
: establece el nivel de detalle de ffmpeg/libav. Sólo tiene efecto cuando tienes un depurador adjunto a Aegisub.

Hilos de decodificación
: Número máximo de hilos a usar para decodificar video, o -1 para elegir automáticamente. Establecer esto en 1 puede solucionar algunos problemas de decodificación a costa del rendimiento. Rara vez hay algún motivo para establecerlo en un valor distinto de 1 o -1.

Habilitar búsquedas inseguras
: deshabilite algunas de las comprobaciones de cordura de FFMS2 cuando busque en video. Hace posible abrir algunos archivos en los que FFMS2 no puede buscar cuadros con precisión.
