import sys

from argparse import ArgumentParser
import pyaudio

from selcall import Code, Durations
from melody import Melody
from tones import *

parser = ArgumentParser()
parser.add_argument('numbers', metavar='N', type=int, nargs='+', help='SelCall numbers')
parser.add_argument('-w', metavar='name', dest='waveform', default='Sine', help='the waveform to use; one of Sine, Square, Saw, Ramp, defaults to \'Sine\'')
parser.add_argument('-a', metavar='value', dest='attennuation', type=int, default=8, help='output volume attennuation, 1..n where 1 is full volume, defaults to 8')

args = parser.parse_args()
try:
	waveform = getattr(sys.modules[__name__], args.waveform)
except AttributeError:
	quit("Invalid waveform: {}".format(args.waveform))

melody = Melody(Code(args.numbers, duration=Durations.ERICSSON), waveform=waveform)

# load all the sample data because pyaudio seems to require a length, and our generators work on-demand
data=bytes()
for frame in melody:
	frame//=args.attennuation
	data+=frame.to_bytes(melody.bits//8, 'little', signed=melody.signed)

pa = pyaudio.PyAudio()

stream = pa.open(format=pa.get_format_from_width(melody.bits//8, melody.signed), channels=1, rate=melody.rate, output=True)

stream.write(data)

stream.stop_stream()
stream.close()

pa.terminate()
