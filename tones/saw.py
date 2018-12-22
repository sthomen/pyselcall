from .tone import Tone

class Saw(Tone):
	def __iter__(self):
		value = self.high
		step = self.full / (self.rate / self.frequency)

		while True:
			yield value
			value = value-step if value > self.low else self.high
