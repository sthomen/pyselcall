# PySelCall

This package is a series of generators that build up a SelCall squelch tone from
a set of numbers (the tones were 5 or 11 numbers, but this generator lets you
use any number of numbers.)

Note that this (while possibly serviceable, I tried to make the tone and
frequency generators produce correct frequencies) isn't a serious attempt to
make call tones for analog radios, it is just a silly project that stemmed out
of me hearing a sound in a Let's Play of *Mutant Year Zero* that I recognized
from old Swedish TV that had cops with radios in them; a shrill beeping sound.

I googled around, and it turns out it was a SelCall tone for Ericsson radios
from the system called S70 or S80 from the 70's and 80's.

## Module overview

### Melody

Melody generator, feed this class an iterable list or tuple of tuples with
first a frequency value (in Hz) and then a duration (in ms) and it will generate
audio samples in the given sample rate and bit depth. This is most usefully
done with a selcall.Code object.

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

The setup script automatically installs a *pyselcall* script that lets you
easily interface with (almost) all the features of the package.

The one thing that you can do that the script doesn't do is that you can feed
arbitrary frequencies and durations to the Melody class, and thus make any
melody you like (I tried a simple music scale and it worked perfectly)
