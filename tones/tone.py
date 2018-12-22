class Tone(object):
	def __init__(self, frequency, rate=44100, bits=16, signed=False):
		self.frequency=frequency
		self.rate = rate
		self.bits = bits
		self.signed = signed

		self.full = (1 << self.bits)-1


		if self.signed:
			self.high = self.full / 2
			self.mid = 0
			self.low = -self.high
		else:
			self.high = self.full
			self.mid = self.full / 2
			self.low = 0
