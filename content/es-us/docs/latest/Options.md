---
title: Opciones de Aegisub
menu:
  docs:
    parent: miscellaneous
weight: 7000
---

Aegisub es altamente configurable y por lo tanto tiene un gran número de opciones configurables por el usuario. Estas están disponibles en la caja diálogo de opciones, dentro del menú Ver. Esta página es una guía de todas las opciones disponibles.

Aegisub almacena toda su configuración en un archivo de texto llamado _config.json_, el cual por defecto se encuentra en la carpeta [?user]({{<relref path="Aegisub_path_specifiers" lang="en">}}). Si uno quiere restablecer Aegisub a sus opciones predeterminadas sin volver a instalarlo, se puede simplemente eliminar _config.json_ y luego reinicar Aegisub.

## General

![preferences-general](/img/3.2/preferences-general.png#center)

Buscar actualizaciones al inicio
: Si está habilitado, Aegisub comprobará al arrancar si hay una nueva versión disponible y le avisará si la hay. Requiere una conexión con acceso a Internet, naturalmente.

Mostrar barra de herramientas principal
: Si está deshabilitado, la barra de herramientas principal de Aegisub está oculta.

Guardar el estado de la interfaz de usuario en archivos de subtítulos
: Por defecto, Aegisub guarda cosas como la posición de desplazamiento actual de la cuadrícula de subtítulos y el número de fila activa en el archivo de subtítulos para que pueda restaurarse automáticamente cuando vuelva a abrir el archivo. Sin embargo, si está trabajando con control de versiones para sus archivos de subtítulos, puede que quiera desactivarlo para reducir el ruido en los cambios.

Tamaño de ícono de la barra de herramientas
: El tamaño de los íconos para usar en todas las barras de herramientas de Aegisub. Actualmente los únicos valores válidos son 16 y 24.

Cargar automáticamente archivos vinculados
: Cada vez que guarda un guion, Aegisub también almacena información sobre qué archivos de video, audio y códigos de tiempo abrió mientras trabajaba en él, dentro del propio guion. Esta opción decide qué hace Aegisub con estos archivos que están "vinculados" al guion al abrirlo. Si está configurado en "preguntar", Aegisub le preguntará a uno si desea cargar los archivos vinculados. Si se establece en "nunca", Aegisub nunca cargará los archivos vinculados, y del mismo modo, si se establece en "siempre", Aegisub siempre intentará cargar los archivos vinculados (y reportará un error si no se encuentran los archivos).

Niveles de deshacer
: El número máximo de cambios que se pueden deshacer. Cuanto mayor sea este valor, más memoria utilizará Aegisub.

Listas de usados recientemente
: Números máximos de elementos para recordar, para todas las variaslistas de elementos recién usados en Aegisub. El impacto en la memoria al aumentarlos es trivial, pero las listas más grandes pueden resultar imprácticas de manejar.

### Estilos predeterminados

![preferences-default-styles](/img/3.2/preferences-default-styles.png#center)

## Audio

![preferences-audio](/img/3.2/preferences-audio.png#center)

Bloquear desplazamiento en el cursor
: Cuando está habilitado, la vista de onda de audio se desplazará automáticamente para seguir el cursor de reproducción si se acerca demasiado a cualquiera de los bordes.

Ajustar marcadores por defecto
: Cuando está habilitado, Aegisub encasillará de forma predeterminada los marcadores de audio junto con otros marcadores en la visualización de audio (como fotogramas clave y los tiempos de inicio o finalización de otras líneas) al moverlos haciendo clic o arrastrándolos si están lo suficientemente cerca entre sí. El ajuste se puede activar o desactivar manteniendo presionada la tecla mayús/shift.

Rueda de ratón predeterminada para acercamiento
: Cuando está habilitado, la rueda del mouse ampliará la vista de audio horizontalmente de forma predeterminada y desplazará la vista de audio cuando se mantenga presionada la tecla ctrl. Si está deshabilitado, estos dos se intercambian.

Autoenfoque al pasar el ratón
: Si está habilitado, mover el puntero sobre la onda de audio le dará enfoque automáticamente (en lugar de requerir un clic).

Reproducir audio al recorrer el video
: Cuando está habilitado, el paso entre fotogramas reproduce el audio de cada fotograma.

Longitud de sincronización predeterminada
: La duración predeterminada de una nueva línea sin tiempo, en milisegundos.

Longitud de entrada predeterminada
Longitud de cierre predeterminada
: La duración agregada al inicio de una línea mediante las funciones "agregar apertura/entrada" y "agregar cierre/salida". También se utiliza en (y es configurado por) el [postprocesador de sincronización]({{<relref path="Timing_Post-Processor" lang="en">}}).

Sensibilidad de inicio de arrastre de marcador
: La distancia en píxeles que se debe arrastrar un marcador para que se registre como arrastre. Los valores más altos reducen la posibilidad de cambios accidentales, a costa de una peor capacidad de respuesta.

Clic izquierdo y arrastrar para mover marcador de cierre
: Cuando está habilitado, hacer clic izquierdo fija el inicio de la línea en el punto presionado, luego establecerá el fin de la línea en el punto hasta el que se arrastra, haciendo posible cronometrar una línea con un solo movimiento de clic y arrastre. Cuando está deshabilitado, hacer clic izquierdo y arrastrar siempre actualiza solo el momento de inicio de la línea, al igual que el clic derecho con el momento de finalización.

Grosor del límite de línea
: El ancho, en píxeles, de los marcadores de inicio y fin de línea.

Máxima distancia de ajuste
: Distancia máxima para encasillar marcadores con otros marcadores vecinos, en píxeles.

Mostrar líneas inactivas
: Controla cómo se dibujan las líneas que rodean la línea seleccionada actualmente en la onda de audio. "No mostrar" solo mostrará la línea actual. "Mostrar anterior" mostrará la línea anterior (en la cuadrícula, _no_ cronológicamente) en gris además de la línea actual. "Mostrar anterior y siguiente" mostrará las líneas de antes y después de la línea actual (en la cuadrícula, _no_ cronológicamente). "Mostrar todo" mostrará todas las líneas en gris además de la línea actual.

Incluir líneas inactivas comentadas
: Si está deshabilitado, las líneas comentadas se omitirán al seleccionar qué líneas inactivas mostrar en la pantalla de audio (convirtiendo "Mostrar anterior" en "Mostrar la última línea no comentada antes de la actual", y similarmente en otro caso).

### Opciones visuales de pantalla

Cuadros clave en modo diálogo
: Si está habilitado, las líneas que marcan las posiciones de los fotogramas clave en el video se dibujarán en la forma de onda de audio cuando esté en el modo de sincronización de diálogo (el valor predeterminado).

Cuadros clave en modo karaoke
: Si está habilitado, las líneas que marcan las posiciones de los fotogramas clave en el video se dibujarán en la forma de onda de audio cuando esté en el modo de sincronización de karaoke.

Tiempo del cursor
: Si está habilitado, se dibujará una marca de tiempo que enseña el tiempo desde el inicio del archivo cerca de la parte superior del cursor de la onda de audio.

Posición de video
: Si está habilitado, se dibuja una línea en la pantalla de audio que marca la hora de inicio del cuadro de video actual.

<!-- TODO Límites de segundos: pendiente -->

Estilo de forma de onda
: Selecciona cuál de los estilos de representación de formas de onda usar.

  Máximo + Promedio
  : La forma de onda es de dos tonos, lo que indica tanto el valor máximo de una muestra dentro del intervalo de un píxel como, en un color más claro, el valor promedio de todas las muestras dentro del rango de tiempo.

  Máximo
  : La forma de onda muestra sólo el valor máximo, como lo hacían las versiones anteriores de Aegisub.

### Etiquetas de audio

Estas opciones controlan la apariencia de las etiquetas dibujadas en la vista de audio para las sílabas de karaoke.

Fuente
: La fuente tipográfica que se usará para las etiquetas de audio.

Tamaño de fuente
: El tamaño de fuente que se usará para las etiquetas de audio.

## Video

![preferences-video](/img/3.2/preferences-video.png#center)

Mostrar cuadros clave en desplazador
: Cuando está habilitado, Aegisub dibujará marcadores de fotogramas clave en el deslizador de desplazamiento de video.

Desplazar video al inicio de línea al cambiar selección
: Cuando está habilitado, cada vez que se cambia la línea activa, Aegisub desplazará automáticamente el video al primer cuadro de la nueva línea activa. Tenga en cuenta que esto se puede hacer manualmente haciendo doble clic en la cuadrícula o presionando Ctrl-1.

Mostrar herramientas visuales solo al colocar el ratón sobre el video
: Cuando está habilitado, las herramientas de composición tipográfica visual solo se representan cuando el puntero está sobre la pantalla de video.

Cargar audio automáticamente al abrir video
: Cuando está habilitado, cuando abre un archivo de video que también tiene datos de audio, Aegisub cargará automáticamente el audio.

Aumento predeterminado
: El nivel de aumento/zoom de video predeterminado. Útil si uno tiene una pantalla muy grande o muy pequeña.

Paso de salto rápido en cuadros
: Decide qué tan grandes "saltos" hará Aegisub cuando use la función de desplazamiento rápido (Alt-flecha derecha y Alt-flecha izquierda). Medido en cuadros.

Ruta para capturas de pantalla
: Decide dónde Aegisub debe guardar las capturas de pantalla. El valor predeterminado es `?video`, lo que significa que se guardan dondequiera que esté el video, pero puedes cambiarlo a la ruta que desee. [Aegisub_path_specifiers]({{<relref path="Aegisub_path_specifiers" lang="en">}}) son compatibles. Otra opción directamente disponible en el menú desplegable es `?script`, que es dondequiera que esté el guion.

### Resolución de secuencia

Usar resolución del primer video abierto
: Cuando está habilitado, Aegisub configurará automáticamente la resolución del guion a la resolución del video si abre un video y la resolución del guion aún no está configurada. Si esto está deshabilitado, Aegisub establece la resolución del guion en un valor predeterminado configurable.

Coincidir resolución de video al abrir
: Controla lo que Aegisub hará con respecto a la resolución del guion cuando abre un video. Si se configura en "nunca", Aegisub no hará nada si la resolución del guion no coincide con la resolución del video. Si está configurado en "preguntar", Aegisub le preguntará si desea cambiar la resolución del guion para que coincida con la resolución del video si no coinciden. Si se configura en "Remuestrear siempre", Aegisub siempre volverá a muestrear el guion para que coincida con la resolución del video automáticamente. <!-- TODO "siempre establecido" pendiente -->

## Interfaz

![preferences-interface](/img/3.2/preferences-interface.png#center)

Activar consejos de llamadas
: Cuando está habilitado, Aegisub detectará cuando está escribiendo una [etiqueta manual]({{<relref path="ASS_Tags">}}) y mostrará un pequeño cuadro con una breve referencia de la sintaxis de la etiqueta en cuestión hasta que cierre la etiqueta. Esto se denomina "consejo de llamada" y la función puede resultar familiar para los usuarios de varios IDE de programación.

Sobrescribir en cajas de tiempo
: Controla el comportamiento de todas las cajas de edición de tiempo en el programa. De forma predeterminada, todas las cajas de edición de tiempo en Aegisub se comportan como si hubiera presionado el botón Insertar, por lo que cada dígito que escriba sobrescribe lo que ya está ahí, y no puede borrar los números que ya están ahí, sido debe sobrescribirlos. Desmarcar esta casilla desactiva este comportamiento y hace que las cajas de edición de tiempo se comporten como cajas de edición de texto normales (casi).

Habilitar resaltado de sintaxis
: habilita o deshabilita el resaltado de sintaxis de etiquetas de anulación en el cuadro de edición principal.

Ruta a archivos de diccionario
: Decide dónde buscará Aegisub los archivos de diccionario para su corrector ortográfico y diccionario de sinónimos. De forma predeterminada, aparece en `?data/dictionaries`, pero si tiene sus propios diccionarios en el formato correcto en otro lugar, no dude en señalar a Aegisub ahí.

Fuente
Tamaño de fuente
: Decide la fuente y el tamaño de fuente utilizados para la caja de edición de subtítulos y otras cajas de edición.

Máximo de caracteres por línea
: Si el valor del contador de caracteres es mayor que este número, el fondo se volverá rojo para alertar que ha excedido la longitud máxima de línea. La longitud máxima no se aplica de ninguna otra manera.

Umbral de advertencia de caracteres por segundo
Umbral de error de caracteres por segundo
: Los umbrales en los que la columna CPS de fondo comienza a colorearse y cuando se alcanza el color del error.

Ignorar espacios en blanco
: Si está habilitado, los espacios en blanco no se incluirán en el recuento de caracteres.

Ignorar la puntuación
: Si está habilitado, la puntuación no se incluirá en el recuento de caracteres.

Enfocar rejilla al hacer clic
: Cuando está habilitado, la cuadrícula/rejilla de subtítulos actúa como su propia área del programa y puede tener enfoque, al igual que el audio o el video, y mientras lo hace, puede usar las teclas de flecha/rueda del mouse para desplazarse por ella, etc. Por otro lado, si desactiva esta opción, el enfoque permanecerá donde estaba antes cada vez que haga clic en la cuadrícula. Esto significa que ya no puede usar atajos de teclado en la cuadrícula, pero por otro lado significa que puede hacer clic en la cuadrícula para ir a una línea sin perder el enfoque de audio, etc. Úselo a su propia discreción.

Resaltar subtítulos visibles
: Cuando está habilitado, todas las líneas de subtítulos que están visibles actualmente en el fotograma del video (o al menos _deberían_ ser visibles; Aegisub no tiene en cuenta el alfa y ese tipo de trucos en este caso; solo se preocupa por el tiempo de la línea) se resaltarán en la cuadrícula con un color de fondo especial (consulte la opción "Línea en el fondo del marco" a continuación).

Símbolo para ocultar etiquetas de control
: El carácter que se mostrará en lugar bloques de anulación/control si la ocultación de etiquetas está activa. Tenga en cuenta que, a pesar del nombre, puede haber más de un carácter si así lo desea.

Fuente
Tamaño de fuente
: Decide la fuente y el tamaño de fuente de todo el texto en la cuadrícula.

### Colores

![preferences-colours](/img/3.2/preferences-colours.png#center)

#### Visualización de audio

Cursor de reproducción
: El color del cursor de reproducción.

Inicio de límite de la línea
Fin de límite de línea
Línea inactiva de límite de línea
: Los colores respectivos de los distintos marcadores de límites de línea.

Límites de sílaba
: El color de la línea límite de una sílaba en el modo karaoke.

### Esquemas de color de audio

Controla la combinación de colores utilizada para la forma de onda/espectro y algunos de los elementos de la interfaz de usuario. Aegisub actualmente no tiene una interfaz de usuario para editar los esquemas de color o crear otros nuevos, pero si te sientes aventurero, puedes encontrarlos en config.json.

#### Resaltado de sintaxis

Fondo
: El color de fondo.

Normal
: El color del texto normal.

Comentarios
: El color de texto de comentarios.

Dibujos
: El color de dibujos.

Corchetes
: El color de los corchetes que inician/finalizan los bloques de anulación.

Barras y paréntesis
: El color de las barras invertidas y los paréntesis dentro de los bloques de anulación.

Etiquetas
: El color de los nombres de etiquetas dentro de los bloques de anulación.

Parámetros
: El color de los parámetros para anular las etiquetas.

Error
: El color de error para una sintaxis no válida dentro de un bloque de anulación.

Fondo de errores
: Color de fondo para errores.

salto de línea
: Color para \\N, \\n y \\h fuera de los bloques de anulación.

Plantillas karaoke
: Color para bloques de plantilla de karaoke en líneas de plantilla.

<!-- TODO confirm
Variables karaoke
: Color de variables de karaoke en líneas de plantilla.
-->

#### Rejilla de subtítulos

Primer plano estándar
Fondo estándar
: El color normal de las líneas de la cuadrícula. "Primer plano" es el color del texto y "Fondo" es obviamente el color de fondo.

Primer plano de selección
Fondo de selección
: El color de las líneas seleccionadas en la cuadrícula.

Primer plano de colisiones
: El color del texto de las líneas cuyos tiempos se superponen con la línea actualmente activa.

Fondo en cuadro
: El color de fondo de las líneas actualmente visibles en el fotograma del video.

Fondo de comentarios
Fondo de comentario seleccionado
: El color de fondo de las líneas comentadas y de las líneas comentadas seleccionadas, respectivamente.

Fondo de encabezado
Columna izquierda
Borde de línea activa
Líneas
: El color de las líneas de la cuadrícula y las columnas/encabezados fijos.

Error de CPS
: El color de fondo de líneas donde hay un error de caracteres por segundo.

## Accesos rápidos

![preferences-hotkeys](/img/3.2/preferences-hotkeys.png#center)

Esta página enumera todas las teclas de acceso rápido configuradas actualmente en Aegisub y le permite agregar, eliminar y cambiarlas.

### Contextos de atajos de tecla

Aegisub admite la configuración de diferentes teclas de acceso rápido dependiendo de qué parte del programa esté enfocada.

El grupo "Predeterminado" es para teclas de acceso rápido que deben de funcionar independientemente de lo que en Aegisub tenga actualmente el foco del teclado. Las teclas de acceso rápido configuradas de forma predeterminada se reemplazan por categorías más específicas cuando corresponde.  

El grupo "Siempre" establece teclas de acceso rápido habilitadas por el modo Medusa, que se aplican en todas partes del programa y anulan todas las demás pulsaciones de teclas, incluida la escritura normal en cuadros de edición.

Todos los demás contextos de teclas de acceso rápido deben explicarse por sí solos.

### Definir atajos de tecla

Para modificar una tecla de acceso rápido, primero haga clic en la fila para seleccionarla, luego haga clic en el campo de tecla de acceso rápido de la fila y luego presione las teclas que deberían activar el comando. Acepte la nueva tecla de acceso rápido haciendo clic en otra fila.

Para agregar una nueva tecla de acceso rápido, seleccione el contexto al que desea agregar la tecla de acceso rápido y luego haga clic en el botón Nuevo. Ingrese el [nombre del comando]({{<relref path="Commands" lang="en">}}), luego configure la tecla de acceso rápido como cuando se las edita.

## Copia de seguridad

![preferences-backup](/img/3.2/preferences-backup.png#center)

### Guardado automático

Permitir
: Si está habilitado, Aegisub guardará periódicamente una copia del guion en el que está trabajando en la ruta de guardado automático.

Intervalo en segundos
: Con qué frecuencia Aegisub debe guardar automáticamente.

Ruta
: decide dónde guardar los respaldos automáticos de los guiones en los que está trabajando. De forma predeterminada, establece `autosave` en su directorio `?user` de Aegisub (consulte la página de [variables Aegisub de rutas]({{<relref path="Aegisub_path_specifiers" lang="en">}}) para más detalles).

Guardar automáticamente tras cada cambio
: Si está habilitado, Aegisub guardará el archivo después de cada cambio realizado. Tenga en cuenta que esto actualmente causa algunos problemas con el sistema de deshacer.

### Copias de seguridad automáticas

Activar
: Si está habilitado, Aegisub guardará una copia de seguridad de cada guion que abra inmediatamente al abrirlo. De forma predeterminada, se guarda en `?user/autoback/`, pero esto se puede cambiar (ver más abajo).

Ruta
: Decide dónde guardar las copias de seguridad automáticas de los guiones. Por defecto está configurado en `autoback` en su directorio Aegisub `?user`.

## Automatización

![preferences-automation](/img/3.2/preferences-automation.png#center)

Ruta base
: Un directorio base donde se colocan las secuencias de automatización no cargadas automáticamente. Se utiliza sólo para guardar rutas a archivos de secuencia en los subtítulos.

Ruta de inclusión
: Lista de directorios donde se buscan archivos y módulos incluidos. Los directorios están separados por un carácter de barra vertical, `|`.

Ruta de carga automática
: Lista de directorios en los que se buscan secuencias al inicio, que luego se cargan automáticamente. Los directorios están separados por un carácter de barra vertical, `|`.

Nivel de traza
: Cuando una secuencia de comandos envía un mensaje a la consola de depuración, también puede especificar un nivel de seguimiento. Si el nivel de seguimiento de un mensaje es inferior al valor proporcionado aquí, el mensaje no se registra. Los nombres dados a los niveles son sólo sugerencias y no tienen ningún efecto en la ejecución de la secuencia (es decir, un mensaje de nivel "Fatal" no hará que la secuencia finalice).

Prioridad de hilo
: Prioridad dada al hilo de ejecución de la secuencia. Si está en un sistema de un solo núcleo/una sola CPU, tener esto a un nivel más bajo de lo normal hará que otros programas respondan mejor mientras las secuencias de ejecución prolongada estén activos.

Autorecargar al exportar
: Recarga automáticamente los conjuntos de secuencias especificados cuando el diálogo de [Exportar]({{<relref path="Exporting" lang="en">}}) se abre. En ese caso tendrá que pasar a la ventana [Automation/Manager]({{<relref path="Automation/Manager" lang="en">}}) y determinar la causa del error.

## Audio avanzado

![preferences-advanced-audio](/img/3.2/preferences-advanced-audio.png#center)

Proveedor de audio
: Qué proveedor usar para cargar audio. Actualmente sólo existen dos métodos.

_avisynth_ (solo Windows)
: Utiliza [Avisynth](http://www.avisynth.org) para cargar audio. Todos los tipos de archivos se cargarán con DirectShowSource(), excepto los archivos AVS que se abrirán con Import().

_FFmpegSource_
: Utiliza [FFMS2](http://code.google.com/p/ffmpegsource/) para cargar audio. Generalmente es más confiable que abrir a través de DirectShowSource, pero más lento debido a que primero tiene que indexar los archivos.

Independientemente de esta configuración, el lector PCM WAV interno siempre se probará primero para los archivos WAV.

Reproductor de audio
: Qué método utilizar para reproducir audio. Las opciones dependen de la plataforma.

_DirectSound_ (solo Windows)
: Utiliza Microsoft DirectSound para reproducir audio. Este es el reproductor de audio mejor probado y más estable.

_DirectSound-antiguo_ (solo Windows)
: Implementación original de Aegisub del reproductor DirectSound. Si tiene problemas de reproducción de audio cuando utiliza el reproductor DirectSound, este puede funcionar mejor (pero probablemente no).

_alsa_ (solo Linux)
: Utiliza la [Arquitectura de sonido avanzada de Linux](http://www.alsa-project.org/) para reproducir audio. ALSA es la arquitectura de sonido nativa de Linux y no está disponible en ningún otro sistema.

_pulse_ (Linux y otros sistemas tipo \*NIX)
: Reproduce sonido a través de un servidor de sonido [PulseAudio](http://pulseaudio.org/). Este es el reproductor de audio menos probado y con menos probabilidades de funcionar, y solo se recomienda si su configuración de audio hace que los reproductores que no sean de pulso sean indeseables.

_portaudio_
: Utiliza la API [PortAudio](http://www.portaudio.com/) para reproducir sonido. PortAudio tiene diferentes implementaciones de reproducción en diferentes plataformas. En la mayoría de los Unices utiliza Open Sound System (OSS) para la salida. Actualmente es el único reproductor de audio de Windows que admite la selección del dispositivo de salida.

_openal_
: Utiliza la API [OpenAL](http://www.openal.com/) para reproducir audio. Este es el reproductor recomendado en OS X. Normalmente no se incluye en las compilaciones de Windows debido a que agrega una dependencia adicional con pocos beneficios.

### Caché

Tipo de caché
: Usa RAM a menos que tenga muy poca, luego usa el disco duro. El caché no es necesario ni se utiliza cuando se abren archivos PCM WAV. Si desactiva el almacenamiento en caché, la reproducción de audio puede volverse muy poco confiable.

Ruta
: Estas opción determina dónde se ubicará el caché de audio del disco duro. Sólo se utiliza si la caché está configurada en el disco duro. No debería necesitar cambiar esto a menos que tenga poco espacio en el disco. Para el nombre, la cadena espera un parámetro "%i" de estilo printf, que será reemplazado por un número. "%02i" se utiliza de forma predeterminada. No cambies eso a menos que sepa lo que está haciendo.

### Espectro

Calidad
: Determina la calidad de la visualización del espectro de audio. Una configuración de mayor calidad da como resultado un mayor uso de CPU y RAM. Cada configuración consecutiva utiliza un poco más de CPU que la anterior y el doble de RAM. Para audio con una frecuencia de muestreo de 48 kHz, un minuto de audio utiliza esta cantidad de memoria en las diferentes configuraciones:

<table class="table table-bordered table-condensed">
  <tr><th>0 "regular"</th><td>11 MB</td>
  <tr><th>1 "buena"</th><td>22 MB</td>
  <tr><th>2 "alta"</th><td>44 MB</td>
  <tr><th>3 "demente"</th><td>88 MB</td>
</table>

La cantidad de memoria utilizada no depende del número de canales
(Aegisub siempre funciona en mono) ni de la profundidad de bits (el espectro siempre se calcula en punto flotante de 32 bits) del audio.

{{<todo>}}this is probably wrong {{</todo>}}

Máximo de memoria caché
: La cantidad máxima de memoria que se utilizará para el almacenamiento en caché del espectro de audio. Los resultados de los cálculos para mostrar el espectro de audio se almacenan en caché para que el desplazamiento por el audio sea más fluido. La cantidad de visualización del espectro que se puede almacenar en caché en una determinada cantidad de memoria depende de la configuración de calidad anterior. El tamaño de caché predeterminado de 128 MB da como resultado un poco menos de 6 minutos de audio a 48 kHz en calidad 1. Si lo configura en menos de 5 MB, se utilizará el valor predeterminado de 128 MB. Probablemente no deberías configurar esto en más de 1/4 de la cantidad de RAM física instalada.

### Avisynth (solo Windows)

Mezclador descendente Avisynth
: Aegisub sólo puede utilizar audio mono (un solo canal). Esta opción determina qué función de Avisynth utilizar para convertir audio a mono.

Forzar frecuencia de muestreo
: Convierte todo el audio abierto a la frecuencia de muestreo dada. Forzar la frecuencia de muestreo a la frecuencia de muestreo utilizada por su tarjeta de sonido (en lugar de que el reproductor de audio lo haga) puede mejorar potencialmente el rendimiento del audio y solucionar problemas de reproducción.

### FFmpegSource

Modo de manejo de errores de indexado de audio
: Qué hacer si se produce un error al indexar una pista de audio.

   _Ignorar_
   : Ignora el error y continúa decodificando el archivo. Este modo puede permitirle abrir algunos archivos corruptos, pero puede causar desincronización de audio/video.

   _Limpiar_
   : Finge que la pista con el error no existe en el archivo.

   _Detener_ (predeterminado)
   : Detiene la indexación en el punto del error y devuelve todos los datos de audio antes del error. Este es el valor predeterminado debido a que los paquetes de audio corruptos al mero final de los archivos son bastante comunes.

   _Abortar_
   : Se niega a abrir el archivo en absoluto.

Siempre indexar todas las pistas de audio
: Si está deshabilitado, abrir un archivo de video solo indexará las pistas de video, lo que le obligará a volver a indexar el archivo para abrir pistas de audio del mismo archivo.

### Portaudio

Dispositivo de portaudio
: Qué dispositivo de salida usar al reproducir audio a través de portaudio.

## Video avanzado

![preferences-advanced-video](/img/3.2/preferences-advanced-video.png#center)

Proveedor de video
: Decide qué método debe utilizar Aegisub para cargar el video. Las opciones que tiene disponibles aquí dependen de cómo se compiló su copia de Aegisub y del sistema operativo que esté ejecutando. Existen las siguientes alternativas:

   _avisynth_ (solo Windows)
   : Utiliza [Avisynth](http://www.avisynth.org) para cargar video. Versátil, admite la carga de casi todos los formatos comunes, así como archivos .d2v (DVD VOB indexados) si se suministra el complemento correcto. Tenga en cuenta que Aegisub puede instalar su propio `avisynth.dll` en lugar de utilizar la instalación de su sistema si así lo desea. Requiere decodificadores de Video para Windows para archivos AVI para obtener el mejor rendimiento. Utiliza DirectShow para la mayoría de los formatos, por lo que no se recomienda para nada más que AVI, d2v y abrir guiones de Avisynth.

   _FFmpegSource_
   : Utiliza [FFMS2](http://code.google.com/p/ffmpegsource/) para cargar videos. Generalmente la opción más confiable.

Proveedor de subtítulos
: Decide qué proveedor utiliza Aegisub para representar los subtítulos en el video. Si instala renderizadores CSRI adicionales como VSFilterMod o xy-VSFilter (colocando los archivos dll en el directorio CSRI dentro del directorio de Aegisub), se enumerarán aquí junto con los predeterminados.

   *CSRI/vsfilter_textsub* (solo Windows)
   : Utiliza VSFilter 2.40 para representar subtítulos. Este es el procesador de subtítulos estándar que define el formato ASS utilizado por Aegisub.

   _libass_
   : Utiliza [libass](http://code.google.com/p/libass/) para representar subtítulos. libass es mucho más rápido que VSFilter y (en cierto modo) multiplataforma, pero desafortunadamente todavía tiene algunas diferencias de representación con respecto a VSFilter y problemas relacionados con las fuentes en Windows. Si está realizando una composición tipográfica compleja que será [de subtítulos sueltos]({{<relref path="Attaching_subtitles_to_video#subtítulos-sueltossoftsubbing">}}), es una buena idea comprobar su trabajo tanto con VSFilter como con libass, ya que un número cada vez mayor de usuarios utiliza libass.

Forzar BT.601
: Suponer que todos los videos YUV son BT.601, para compatibilidad con VSFilter.

   Cuando VSFilter se utiliza como filtro DirectShow, siempre utiliza la matriz de color BT.601 para convertir los subtítulos de RGB a YUV. Esto significa que si el video usa BT.709 (como lo hacen la mayoría de los videos HD y ocasionalmente los DVD), los colores que coinciden con el video en Aegisub no coincidirán con el video en el reproductor. Esta opción hace que Aegisub siempre convierta videos a RGB usando BT.601, lo que hace que los colores que se muestran en Aegisub sean incorrectos, pero si los colores coinciden en Aegisub, coincidirán en el reproductor.

   Para hacer las cosas más interesantes, VSFilter usará el espacio de color *correcto* cuando se use como renderizador de subtítulos interno en MPC-HC, por lo que habilitar esta opción dará como resultado colores *no coincidentes* en ese caso. Como el ISR actualmente está roto de muchas maneras (por ejemplo, es imposible colocar los subtítulos con precisión), recomendamos no preocuparse por eso por ahora.

   Esta comparación puede aclarar esto:

   ![bt601](/img/3.2/bt601.png)

   Aegisub ahora escribe qué espacio de color se debe usar para las conversiones RGB -> YUV al archivo de subtítulos, por lo que esperamos que este lío se resuelva mediante mejoras en el renderizador en algún momento en el futuro.

### Avisynth

Permitir Avisynth anterior a 2.56a
: Admite el uso de versiones antiguas de Avisynth que algunas personas se niegan a actualizar por varias malas razones.

Límite de memoria de Avisynth
: Límite de memoria caché de fotogramas para Avisynth. Por lo general, aumentar esto no mejora el rendimiento y solo debe hacerse si está abriendo directamente guiones de Avisynth demasiado complicados.

### FFmpegSource

Nivel de detalle del registro de depuración
: Establece el nivel de detalle de ffmpeg/libav. Sólo tiene efecto cuando tienes un depurador adjunto a Aegisub.

Subprocesos de decodificación
: Número máximo de hilos a usar para decodificar video, o -1 para elegir automáticamente. Establecer esto en 1 puede solucionar algunos problemas de decodificación a costa del rendimiento. Rara vez hay algún motivo para establecerlo en un valor distinto de 1 o -1.

Habilitar desplazamiento inseguro
: Deshabilita algunas de las comprobaciones de cordura de FFMS2 cuando hace saltos en el video. Hace posible abrir algunos archivos en los que FFMS2 no puede saltar entre fotogramas con precisión.
