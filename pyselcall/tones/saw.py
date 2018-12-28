from .tone import Tone

class Saw(Tone):
	"""
	This class infinitely generates a sinking value that goes from the maximum
 	value to 0 over the course of a cycle and then repeats.
	"""
	def __iter__(self):
		value = self.high
		step = self.full / (self.rate / self.frequency)

		while True:
			yield value
			value = value-step if value > self.low+step else self.high
