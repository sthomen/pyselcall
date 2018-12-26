import sys

from selcall import Code, Durations
from melody import Melody

args=tuple(int(a) for a in sys.argv[1:])

melody = Melody(Code(args, duration=Durations.ERICSSON))

melody.wave('output.wav')
