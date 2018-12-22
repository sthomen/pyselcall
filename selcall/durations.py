class Durations(object):
	"""
	This class is an iterable that produces the duration values for use in the
	Code class to build frequency, duration pairs. It is designed to always
	provide a value, even if the duration-tuple has fewer values than what is
	requested, repeating the last value of the duration infinitely if given
	a tuple of frequencies.

	It's really only doing this because the Ericsson style has a different
	duration of the first note than all the others, but can act as a place to
	insert other weird timing schemes if one is ever needed.
	"""
	# Durations in milliseconds
	ERICSSON = (700, 100)

	def __init__(self, duration=None, count=1):
		if not duration:
			duration = 33

		self.duration = duration
		self.count = count

	def __iter__(self):
		if type(self.duration) == int:
			durations = (self.duration,) * self.count
		else:
			durations = self.duration

		for i in range(0, self.count):
			# repeat last duration if the length of the message exceeds our duration table,
			# this is just here to accommodate the varying length of Ericsson selcalls
			if (i >= len(durations)):
				yield durations[-1]
			else:
				yield durations[i]
