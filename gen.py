import sys
from argparse import ArgumentParser

from selcall import Code, Durations
from melody import Melody

parser = ArgumentParser()
parser.add_argument('numbers', metavar='N', type=int, nargs='+', help='SelCall numbers')
parser.add_argument('-w', metavar='name', dest='waveform', default='Sine', help='the waveform to use; one of Sine, Square, Saw, Ramp, defaults to \'Sine\'')
parser.add_argument('-a', metavar='value', dest='attennuation', type=int, default=8, help='output volume attennuation, 1..n where 1 is full volume, defaults to 8')
parser.add_argument('-f', metavar='filename', dest='filename', default='output.wav', help='output filename, defaults to \'output.wav\'')

args = parser.parse_args()
try:
	waveform = getattr(sys.modules[__name__], args.waveform)
except AttributeError:
	quit("Invalid waveform: {}".format(args.waveform))

melody = Melody(Code(args.numbers, duration=Durations.ERICSSON), waveform=waveform)

melody.wave(args.filename)
