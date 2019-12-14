import unittest
from . import *

class TestTones(unittest.TestCase):
	def test_that_all_tones_work(self):
		tones = Tones([0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf])

		for tone in tones:
			pass

	@unittest.expectedFailure
	def test_that_tones_less_than_0x0_throws(self):
		tones = Tones([-0x1])

		for tone in tones:
			pass

	@unittest.expectedFailure
	def test_that_tones_larger_than_0xf_throws(self):
		tones = Tones([0x10])

		for tone in tones:
			pass
