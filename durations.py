class Durations(object):
	# Durations in milliseconds
	ERICSSON = (700, 100)

	def __init__(self, delay=None, count=1):
		if not delay:
			delay = 33

		self.delay = delay
		self.count = count

	def __iter__(self):
		if type(self.delay) == int:
			delays = (self.delay,) * self.count
		else:
			delays = self.delay

		for i in range(0, self.count):
			# repeat last duration if the length of the message exceeds our duration table,
			# this is just here to accommodate the varying length of Ericsson selcalls
			if (i >= len(delays)):
				yield delays[-1]
			else:
				yield delays[i]
