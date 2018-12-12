from math import sin, floor, pi

class Tone(object):
	def __init__(self, frequency, rate=44100, bits=16):
		self.frequency=frequency
		self.rate=rate
		self.bits=bits
		self.full = (1 << self.bits)-1

class Square(Tone):
	def __iter__(self):
		i = 0
		value = 0
		switch = self.rate / self.frequency

		while True:
			if floor(i % switch) == 0:	# XXX aliasing!
				value = self.full if value == 0 else 0

			i += 1

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
		x = 0

		mid = self.full/2

		while True:
			value = sin(x*(2*pi)/(self.rate / self.frequency))*mid+mid

			x += 1

			yield floor(value)
