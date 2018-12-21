class Tone(object):
	def __init__(self, frequency, rate=44100, bits=16):
		self.frequency=frequency
		self.rate=rate
		self.bits=bits
		self.full = (1 << self.bits)-1
