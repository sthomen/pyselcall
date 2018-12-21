from .tone import Tone

class Ramp(Tone):
	def __iter__(self):
		value = 0
		step = self.full / (self.rate / self.frequency)

		while True:
			yield value
			value = (value + step) % self.full
