import wave

from tones import Tone, Sine

class Melody(object):
	def __init__(self, code, waveform=Sine, rate=44100, bits=16):
		if not issubclass(waveform, Tone):
			raise ValueError("The waveform parameter must be a a class derived from tones.Tone")

		self.code = code
		self.waveform = waveform
		self.rate = rate
		self.bits = bits

	def __iter__(self):
		for frequency, duration in self.code:
			waveform = iter(self.waveform(frequency, self.rate, self.bits, signed=True))

			frames = int((duration / 1000) * self.rate)

			for _ in range(0,frames):
				yield int(next(waveform))

	def wave(self, fn):
		with wave.open(fn, 'wb') as fp:
			fp.setnchannels(1)
			fp.setsampwidth(self.bits//8)
			fp.setframerate(self.rate)
			fp.setcomptype('NONE', 'Not Compressed')

			for frame in self:
				fp.writeframesraw(frame.to_bytes(self.bits//8, 'little', signed=True))

			fp.close()
