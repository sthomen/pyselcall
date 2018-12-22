import unittest
from . import *

class BaseTest(unittest.TestCase):
	def setUp(self):
		self.frequency = 1000
		self.rate = 44100
		self.samplecount = int(self.rate / self.frequency)

	def assertLow(self, value, minimum, tolerance=0.1):
		assert minimum <= value <= (minimum - (minimum * tolerance)), "Low value {} is not within a minimum tolerance of {:%}".format(value, tolerance)

	def assertHigh(self, value, maximum, tolerance=0.1):
		assert (maximum - (maximum * tolerance)) <= value <= maximum, "High value {} is not within a maximum tolerance of {:%}".format(value, tolerance)

	def _test_waveform_range(self, wave):
		iterator = iter(wave)

		low = wave.mid
		high = wave.mid

		for _ in range(0, self.samplecount):
			value = next(iterator)
		
			if value < low:
				low = value

			if value > high:
				high = value

		self.assertLow(low, wave.low)
		self.assertHigh(high, wave.high)

class TestUnsigned(BaseTest):
	def test_range_of_sine(self):
		wave = Sine(self.frequency, self.rate, signed=False)
		self._test_waveform_range(wave)

	def test_range_of_square(self):
		wave = Square(self.frequency, self.rate, signed=False)
		self._test_waveform_range(wave)

	def test_range_of_saw(self):
		wave = Saw(self.frequency, self.rate, signed=False)
		self._test_waveform_range(wave)

	def test_range_of_ramp(self):
		wave = Ramp(self.frequency, self.rate, signed=False)
		self._test_waveform_range(wave)

class TestSigned(BaseTest):
	def test_range_of_sine(self):
		wave = Sine(self.frequency, self.rate, signed=True)
		self._test_waveform_range(wave)

	def test_range_of_square(self):
		wave = Square(self.frequency, self.rate, signed=True)
		self._test_waveform_range(wave)

	def test_range_of_saw(self):
		wave = Saw(self.frequency, self.rate, signed=True)
		self._test_waveform_range(wave)

	def test_range_of_ramp(self):
		wave = Ramp(self.frequency, self.rate, signed=True)
		self._test_waveform_range(wave)
