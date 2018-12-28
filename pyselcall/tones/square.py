from math import floor

from .tone import Tone

class Square(Tone):
	"""
	This class continually produces a 50% duty cycle square wave centered in
	the cycle (meaning it starts at halfway through the low cycle and then
	shifts to high for 50% of the cycle and then back down to 0 at 75%.
	"""
	def __iter__(self):
		switch = (self.rate / self.frequency) / 2
		value = 0
		x = switch / 2

		while True:
			if floor(x % switch) == 0:
				value = self.high if value == self.low else self.low

			x += 1

			yield value
