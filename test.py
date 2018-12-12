from selcall import Code, Durations

code = Code((7, 0, 0, 5, 0), Durations.ERICSSON)

for t in code:
	print(t)
