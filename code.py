from durations import Durations
from tones import Tones

class Code(object):
	def __init__(self, code, duration=None, codec=None):
		self.code = code
		self.codec = codec
		self.duration = duration

	def __iter__(self):
		durations = Durations(self.duration, len(self.code))
		tones = Tones(self.code, self.codec)

		for tone, duration in zip(tones, durations):
			yield (tone, duration)
