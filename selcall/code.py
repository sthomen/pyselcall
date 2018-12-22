from .durations import Durations
from .tones import Tones

class Code(object):
	"""
	This class takes a given code (a sequence of numbers 0x0 - 0xf) and feeds
	them into Durations and Tones objects, combining the output into a frequency
	(Hz) and duration (ms) tuple.
	"""
	def __init__(self, code, duration=None, codec=None):
		self.code = code
		self.codec = codec
		self.duration = duration

	def __iter__(self):
		durations = Durations(self.duration, len(self.code))
		tones = Tones(self.code, self.codec)

		for tone, duration in zip(tones, durations):
			yield (tone, duration)
