from .tone import Tone

class Ramp(Tone):
	"""
	This class generates an infinte series of ramps that go from 0 to the
	maximum value over the course of a cycle and then repeats.
	"""
	def __iter__(self):
		value = self.low
		step = self.full / (self.rate / self.frequency)

		while True:
			yield value
			value = value + step if value < self.high else self.low
