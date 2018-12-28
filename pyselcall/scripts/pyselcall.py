from argparse import ArgumentParser

import pyselcall

def run():
	parser = ArgumentParser()

	parser.add_argument('numbers', metavar='N', type=int, nargs='+', help='numbers 0-9')
	parser.add_argument('-w', dest='waveform', default='Sine', help='the waveform to use; one of Sine, Square, Saw, Ramp, defaults to \'Sine\'')
	parser.add_argument('-a', dest='attennuation', type=int, default=8, help='output volume attennuation, 1..n where 1 is full volume, defaults to 8')
	parser.add_argument('-f', dest='filename', help='output audio to a wav file with the given filename')

	args = parser.parse_args()
	try:
		waveform = getattr(pyselcall.tones, args.waveform)
	except AttributeError:
		quit("Invalid waveform: {}".format(args.waveform))

	melody = pyselcall.Melody(pyselcall.Code(args.numbers, duration=pyselcall.Durations.ERICSSON), waveform=waveform)

	if args.filename:
		melody.wave(args.filename, args.attennuation)
	else:
		melody.play(args.attennuation)
