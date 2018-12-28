from argparse import ArgumentParser

import pyselcall

def run():
	parser = ArgumentParser(epilog='If the -f option is not given, then this script will attempt to play the sounds through pyaudio.')

	parser.add_argument('numbers', metavar='N', type=int, nargs='+', help='numbers 0-9')
	parser.add_argument('-w', dest='waveform', default='Sine', help='the waveform to use; one of Sine, Square, Saw, Ramp. Defaults to "Sine"')
	parser.add_argument('-s', dest='standard', default='CCIR', help='the frequency standard to use; one of CCIR, EEA, EIA, ZVEI_I, ZVEI_II, ZVEI_III, DZVEI, PZVEI. Defaults to "CCIR"')

	group = parser.add_mutually_exclusive_group()

	group.add_argument('-d', dest='duration', type=int, default=33, help='duration in milliseconds')
	group.add_argument('-e', dest='duration', action='store_const', const=pyselcall.Durations.ERICSSON, help='Use Ericsson 700ms, 100ms, 100ms... durations')

	parser.add_argument('-a', dest='attennuation', type=int, default=8, help='output volume attennuation, 1..n where 1 is full volume, defaults to 8')
	parser.add_argument('-f', dest='filename', help='output audio to a wav file with the given filename')

	args = parser.parse_args()

	try:
		standard = getattr(pyselcall.selcall.Tones, args.standard)
	except AttributeError:
		quit("Invalid standard: {}".format(args.standard))

	try:
		waveform = getattr(pyselcall.tones, args.waveform)
	except AttributeError:
		quit("Invalid waveform: {}".format(args.waveform))

	melody = pyselcall.Melody(pyselcall.Code(args.numbers, args.duration, standard), waveform=waveform)

	if args.filename:
		melody.wave(args.filename, args.attennuation)
	else:
		melody.play(args.attennuation)
