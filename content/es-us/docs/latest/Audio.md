---
title: Trabajando con audio
menu:
  docs:
    parent: timing
weight: 5000
---

Aegisub tiene un modo audio bastante avanzado y configurable, tanto con la vista tradicional de forma de onda como con una vista alternativa de espectrograma.
Varios modos diferentes de sincronización están disponibles para la sincronía normal de diálogo y para la de karaoke.

## Abrir audio

Para abrir un archivo de audio en Aegisub, solo pase al menú _Audio_ y dele a _Abrir archivo de audio_. Si tiene un archivo de video (con pista de audio incluído) ya abierto, se puede usar _Abrir audio desde video_ en su lugar, el cual obviamente abre la pista de audio desde el archivo de video que tiene actualmente abierto. Podrá abrir cualquier tipo de archivo de audio que su [proveedor de audio]({{<relref path="Options#audio-avanzado">}}) puede decodificar (más info de esto abajo). Además, si simplemente quiere usar la vista de audio sin cargar ningún audio de verdad, puede elegir _Abrir audio 2h30 silencio_ o _Abrir audio 2h30 ruido_.

Si abrir el audio falla con un error que menciona el reproductor de audio, o si al reproducir el audio se falta el sonido, cambiar a un [reproductor diferente de audio]({{<relref path="Options#audio-avanzado">}}) puede que ayude.

### Formatos soportados

Aegisub usa típicamente [FFMS2](https://github.com/FFMS/ffms2) para abrir audio,
que confiablemente puede abrir audio en casi cualquier formato en que uno puede pensar. En Windows, Aegisub puede también usar DirectShow (via Avisynth), que puede ser más rápido ya que no tiene que indexar los archivos de audio antes de abrirlos. Sin embargo, DirectShow es considerablemente menos consistente, y completas locuras pueden pasar si uno abre un archivo con múltiples pistas de audio con Avisynth.

Aegisub solo maneja audio mono. Audio multicanal será automáticamente downmixed (reducido a un canal), pero los resultados pueden ser de baja calidad de fuentes de más de dos canales.

### Caché de audio

Si uno abre cualquier formato de audio que no es un archivo Microsoft WAV sin compresión (PCM), Aegisub necesita decodificar y guardarlo en caché primero. Ya cargado, el audio se reduce a mono (véase la [opción downmixer de audio]({{<relref path="Options#avisynth-solo-windows">}}) si quiere agarrar solo un canal en su lugar), se descomprime a PCM (alias WAV) y (por defecto) se carga en un caché RAM. Esto significa que va a necesitar una _alta cantidad_ de RAM para abrir un archivo de audio comprimido largo. Si su computadora no cuenta con mucha RAM, o si uno trabaja con una película completa, pase a la [opción audio caché]({{<relref path="Options#caché">}}) para ver instrucciones de cómo hacer que Aegisub use su caché de unidad de disco (más lento) en su lugar; o descomprima el archivo a WAV de primer paso, ya que Aegisub puede leer desde WAV directamente sin necesidad del caché.

La cantidad exacta de memoria usada para cualquier archivo de audio se puede calcular con la fórmula siguiente:
s = ( b * r * l ) / 8
donde _s_ es la cantidad de memoria (en bytes - divide entre 1024 para kB), _b_ es la cantidad de bits por muestra (siempre 16 en la actual implementación),
_r_ es la frecuencia de muestreo en Hz (usualmente 48000, o 44100 en algunos casos), y _l_ es la duración del audio (en segundos).

Por ejemplo, con un audio de 25 minutos en 48 kHz, se va a necesitar (16 * 48000 * 25 * 60)/8 = 144000000 B ~= 137 MB.

Cargar y descomprimir el audio hasta el caché lleva tiempo. Una barra de progreso se muestra en la barra de desplazamiento de la vista de audio mientras el audio esté cargando.
