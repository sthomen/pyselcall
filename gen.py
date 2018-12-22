from selcall import Code, Durations
from melody import Melody

melody = Melody(Code((7,0,0,5,0), duration=Durations.ERICSSON))

melody.wave('output.wav')
