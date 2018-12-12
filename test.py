from tonegen import Square, Saw, Triangle, Sine
from time import sleep

square = Square(1000)
saw = Saw(1000)
triangle = Triangle(1000)
sine = Sine(1000)

for i,j,k,l in zip(square, saw, triangle, sine):
	print(" " * int(i/512) + "square")
	print(" " * int(j/512) + "saw")
	print(" " * int(k/512) + "triangle")
	print(" " * int(l/512) + "sine")
	sleep(0.001)
