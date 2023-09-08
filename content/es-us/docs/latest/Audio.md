---
title: Trabajando con audio
menu:
  docs:
    parent: timing
weight: 5000
---

Aegisub tiene un modo audio bien avanzado y configurable, con tanto la vista tradicional de forma de onda como también una vista alternativa de espectrograma.
Varios diferentes modos de sincronizar están disponibles para la sincronía normal de diálogo y para la de karaoke.

## Abrir audio

Para abrir un archivo de audio en Aegisub, solo pase al menú _Audio_ y dele a _Abrir archivo de audio_. Si tiene un archivo de video (con pista de audio incluído) ya abierto, se puede usar _Abrir audio desde video_ en su lugar, el cual obviamente abre la pista de audio desde el archivo de video que tiene actualmente abierto. Podrá abrir cualquier tipo de archivo de audio que su [proveedor de audio]({{<relref path="Options#advancedaudio" lang="en">}}) puede decodificar (más info de esto abajo). Además, si simplemente quiere usar la vista de audio sin cargar ningún audio de verdad, puede elegir _Abrir audio 2h30 silencio_ o _Abrir audio 2h30 ruido_.

Si abrir el audio falla con un error que menciona el reproductor de audio, o si al reproducir el audio se falta el sonido, cambiar a un [reproductor diferente de audio]({{<relref path="Options#advancedaudio" lang="en">}}) puede que ayude.

### Formatos soportados

Aegisub usa típicamente [FFMS2](https://github.com/FFMS/ffms2) para abrir audio,
que confiablemente puede abrir audio en casi cualquier formato en que uno puede pensar. En Windows, Aegisub puede también usar DirectShow (via Avisynth), que puede ser más rápido ya que no tiene que indexar los archivos de audio antes de abrirlos. Sin embargo, DirectShow es considerablemente menos consistente, y completas locuras pueden pasar si uno abre un archivo con múltiples pistas de audio con Avisynth.

Aegisub solo maneja audio mono. Audio multicanal será automáticamente downmixed (reducido a un canal), pero los resultados pueden ser de baja calidad de fuentes de más de dos canales.

### Caché de audio

If you're loading any audio format that isn't an uncompressed (PCM)
Microsoft WAV file, Aegisub needs to decode and cache it first. When loaded,
the audio is downmixed to mono (see the [opción downmixer de audio]({{<relref path="Options#avisynthwindowsonly" lang="en">}}) if you want to grab one channel only
instead), decompressed to PCM (a.k.a. WAV), and (by default) loaded into a
RAM cache. This means that you will need a _large amount_ of RAM to open a
long compressed audio file. If your computer doesn't have a lot of RAM, or
if you're working with a full-length movie, refer to the [opción audio caché]({{<relref path="Options#cache" lang="en">}}) for instructions on how to make Aegisub use its
(slower) hard drive cache instead; or decompress the file to WAV first since
Aegisub can read from WAVs directly without need for caching.

The exact amount of memory used for any given audio file can be calculated
with the following formula:
s = ( b * r * l ) / 8
where _s_ is the amount of memory (in bytes - divide by 1024 to get kB), _b_
is the number of bits per sample (always 16 in the current implementation),
_r_ is the sample rate in Hz (usually 48000, or 44100 in some cases), and
_l_ is the length of the audio (in seconds).

For example, for a 25 minute audio clip at 48 kHz, you will need (16 * 48000 * 25 * 60)/8 = 144000000 bytes ~= 137 MB.

Loading and decompressing the audio into the cache takes some time.
A progress bar is shown in the scroll bar of the audio display while audio is loading.
