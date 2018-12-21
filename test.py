from tones import *
from time import sleep

frequency = 1000
sample_rate = 50000
depth = 7

wave = Sine(frequency, sample_rate, depth)

sample=0

strlen = (1 << depth) + 1 

for v in wave:
	if (sample % int(sample_rate / frequency)) == 0:
		print('-' * strlen)

	buf=[' '] * strlen

	for index, char in enumerate(str(sample)):
		buf[index]=char

	buf[int(v)]='*'

	print(''.join(buf))

	sample+=1
	sleep(0.1)
