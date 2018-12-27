# PySelCall

This is just a silly project that stemmed out of me hearing a sound in a Let's
Play that I recognized from old Swedish TV that had cops with radios in them, a 
shrill beeping sound.

I investigated, and it turns out it was a SelCall tone for Ericsson radios from
the system called S70 or later S80.

It is a series of generators that build up a SelCall squelch tone from a set
of numbers (the tones were 5 or 11 numbers, but this generator lets you use any
number of numbers.)

## Module overview

### selcall.Tones

Maps numbers to various frequency standards, the default is CCIR


### selcall.Durations

Tone durations, mostly here because the first tone of Ericsson devices is 700ms
followed by 100ms for subsequent tones.

### selcall.Code

Ties the selcall.Tones and selcall.Durations generators into one that outputs
tuples with (frequency, duration) in Hz and ms, respectively.

### tones.Sine, tones.Saw, tones.Ramp, tones.Square

The subclasses of tones.Tone infintely generates samples at a given rate from
the waveform that they represent.

## Scripts

### gen.py

Generate wav files with selcall tones (handy for ringtones)

### play.py

Play selcall tones using pyaudio, annoy your cat and/or neighbours

