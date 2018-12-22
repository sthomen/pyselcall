from .tone import Tone

class Ramp(Tone):
	def __iter__(self):
		value = self.low
		step = self.full / (self.rate / self.frequency)

		while True:
			yield value
			value = value + step if value < self.high else self.low
