[[!template id=toc depth=2]]

Aegisub has a fairly advanced, customizable audio mode with both the
traditional waveform display as well as an alternative spectrum display.
Several different timing modes are available for both normal dialog timing
and karaoke timing.

## Opening audio ##
To load an audio file into Aegisub, just go to the _Audio_ menu and press
_Open audio file_. If you have a video file (with an included audio track)
already loaded, you can use _Open audio from video_ instead, which obviously
will load the audio track from the video file you currently have loaded. You
can open any type of audio file that your [[audio
provider|Options#advancedaudio]] can decode (more on this below). In
addition, if you simply wish to use the audio display without loading any
real audio, you can choose _Open 2h30 Blank Audio_ or _Open 2h30 Noise
Audio_.

If opening audio fails with an error that mentions the audio player, or if
playing audio results in no sound, switching to a [[different audio
player|Options#advancedaudio]] may help.

### Supported formats ###
Aegisub normally uses FFMS2 to open audio, which can reliably open audio is
nearly any format you an think of. On Windows, Aegisub can also use
DirectShow (via Avisynth), which can be faster as it does not have to index
the audio files before opening them. However, DirectShow is considerably
less reliable, and extremely insane things may happen if you open a file
with multiple audio tracks via Avisynth.

Aegisub only supports mono audio. Multichannel audio will be automatically
downmixed, but the results may be of poor quality for sources of more than
two channels.

### Audio caching ###
If you're loading any audio format that isn't an uncompressed (PCM)
Microsoft WAV file, Aegisub needs to decode and cache it first. When loaded,
the audio is downmixed to mono (see the [[audio downmixer
option|Options#avisynthwindowsonly]] if you want to grab one channel only
instead), decompressed to PCM (a.k.a. WAV), and (by default) loaded into a
RAM cache. This means that you will need a _large amount_ of RAM to open a
long compressed audio file. If your computer doesn't have a lot of RAM, or
if you're working with a full-length movie, refer to the [[audio cache
option|Options#cache]] for instructions on how to make Aegisub use its
(slower) hard drive cache instead; or decompress the file to WAV first since
Aegisub can read from WAVs directly without need for caching.

The exact amount of memory used for any given audio file can be calculated
with the following formula:
    s = ( b * r * l ) / 8
where _s_ is the amount of memory (in bytes - divide by 1024 to get kB), _b_
is the number of bits per sample (always 16 in the current implementation),
_r_ is the sample rate in Hz (usually 48000, or 44100 in some cases), and
_l_ is the length of the audio (in seconds).

For example, for a 25 minute audio clip at 48 kHz, you will need (16 * 48000
* 25 * 60)/8 = 144000000 bytes ~= 137 MB.

Loading and decompressing the audio into the cache will take a few seconds;
Aegisub will display a progress indicator while loading the audio.
