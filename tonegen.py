from math import sin, floor, pi

class Tone(object):
	def __init__(self, frequency, rate=44100, bits=16):
		self.frequency=frequency
		self.rate=rate
		self.bits=bits
		self.full = (1 << self.bits)-1

class Square(Tone):
	def __iter__(self):
		switch = (self.rate / self.frequency) / 2
		value = 0
		x = switch / 2

		while True:
			if floor(x % switch) == 0:
				value = self.full if value == 0 else 0

			x += 1

			yield value

class Saw(Tone):
	def __iter__(self):
		value = 0
		step = self.full / (self.rate / self.frequency)

		while True:
			value = floor(value + step)
			value = value if value < self.full else 0

			yield value

class Triangle(Tone):
	def __iter__(self):
		value = 0
		step = floor((self.full / (self.rate / self.frequency)) / 2)

		while True:
			value += step

			if value > self.full or value <= 0:
				step=-step

			yield value

class Sine(Tone):
	def __iter__(self):
		mid = self.full / 2

		x = -(self.rate / self.frequency) / 4

		while True:
			value = sin(x * (2 * pi) / (self.rate / self.frequency)) * mid + mid

			x += 1

			yield floor(value)

