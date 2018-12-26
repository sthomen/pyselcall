import sys

import pyaudio

from selcall import Code, Durations
from melody import Melody

args=tuple(int(a) for a in sys.argv[1:])

melody = Melody(Code(args, duration=Durations.ERICSSON))

# load all the sample data because pyaudio seems to require a length, and our generators work on-demand
data=bytes()
for frame in melody:
	data+=frame.to_bytes(melody.bits//8, 'little', signed=melody.signed)

pa = pyaudio.PyAudio()

stream = pa.open(format=pa.get_format_from_width(melody.bits//8, melody.signed), channels=1, rate=melody.rate, output=True)

stream.write(data)

stream.stop_stream()
stream.close()

pa.terminate()
