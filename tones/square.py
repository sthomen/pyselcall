from math import floor

from .tone import Tone

class Square(Tone):
	def __iter__(self):
		switch = (self.rate / self.frequency) / 2
		value = 0
		x = switch / 2

		while True:
			if floor(x % switch) == 0:
				value = self.high if value == self.low else self.low

			x += 1

			yield value
