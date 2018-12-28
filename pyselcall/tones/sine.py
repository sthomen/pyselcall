from math import sin, pi

from .tone import Tone

class Sine(Tone):
	"""
	This class continually produces a sine wave. It offsets the sine wave as to
	always start at 0 to reduce pops in the output.
	"""
	def __iter__(self):
		x = 0 if self.signed else -(self.rate / self.frequency) / 4

		mid = (self.full / 2)

		while True:
			value = sin(x * (2 * pi) / (self.rate / self.frequency)) * mid

			if not self.signed:
				value += mid

			x += 1

			yield value
