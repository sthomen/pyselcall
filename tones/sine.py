from math import sin, pi

from .tone import Tone

class Sine(Tone):
	def __iter__(self):
		mid = self.full / 2

		x = -(self.rate / self.frequency) / 4

		while True:
			value = sin(x * (2 * pi) / (self.rate / self.frequency)) * mid + mid

			x += 1

			yield value
