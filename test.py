from tonegen import Square, Ramp, Saw, Triangle, Sine
from time import sleep

frequency = 1000
sample_rate = 10000
depth = 6

classes = (Square, Ramp, Saw, Triangle, Sine)

waves=[]

for wavetype in classes:
	waves.append(wavetype(frequency, sample_rate, depth))


sample=0

strlen = (1 << depth) + 1

for i,j,k,l,m in zip(*waves):
	if (sample % int(sample_rate / frequency)) == 0:
		print('-' * strlen)
	else:

		buf=[' '] * strlen

		for index, char in enumerate(str(sample)):
			buf[index]=char

#		buf[i]='s'
		buf[j]='r'
		buf[k]='w'
#		buf[l]='t'
#		buf[m]='i'

		print(''.join(buf))

	sample+=1
	sleep(0.1)
