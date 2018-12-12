class Tones(object):
	# Frequencies in Hz for the tone sets 0x0 - 0xF
	CCIR     = (1981, 1124, 1197, 1275, 1358, 1446, 1540, 1640, 1747, 1860, 2400,  930, 2247,  991, 2110, 1055)
	EEA      = (1981, 1124, 1197, 1275, 1358, 1446, 1540, 1640, 1747, 1860, 1055,  930, 2400,  991, 2110, 2247)
	EIA      = ( 600,  741,  882, 1023, 1164, 1305, 1446, 1587, 1728, 1869, 2151, 2433, 2010, 2292,  459, 1091) 
	ZVEI_I   = (2400, 1060, 1160, 1270, 1400, 1530, 1670, 1830, 2000, 2200, 2800,  810,  970,  885, 2600,  680)
	ZVEI_II  = (2400, 1060, 1160, 1270, 1400, 1530, 1670, 1830, 2000, 2200,  885,  825,  740,  680,  970, 2600)
	ZVEI_III = (2400, 1060, 1160, 1270, 1400, 1530, 1670, 1830, 2000, 2200,  885,  810, 2800,  680,  970, 2600)
	DZVEI    = (2200,  970, 1060, 1160, 1270, 1400, 1530, 1670, 1830, 2000,  825,  740, 2600,  885, 2400,  680)
	PZVEI    = (2400, 1060, 1160, 1270, 1400, 1530, 1670, 1830, 2000, 2200,  970,  810, 2800,  885, 2600,  680)

	def __init__(self, code, codec=None):
		if not codec:
			codec = self.CCIR

		self.code=code
		self.codec=codec

	def __iter__(self):
		last=-1
		for number in self.code:
			if number not in range(0x0, 0xf):
				raise ValueError("Invalid code, individual values must be 0x0 - 0xF")

			if last == number:
				number = 0xe

			last = number

			yield self.codec[number]
