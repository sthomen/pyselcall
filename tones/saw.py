from .tone import Tone

class Saw(Tone):
	def __iter__(self):
		value = self.full
		step = self.full / (self.rate / self.frequency)

		while True:
			yield value
			value = value-step if value > 0 else self.full
