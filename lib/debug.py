"""Some of my frequently used utilities for when debugging Python projects."""

from pprint import pprint
def print_stop(msg, obj):
	"""Prints a message, the debug variable `obj`, and stops execution.

	Nice to pair with piping the output into a local file to understand variables.

	Args:
		msg (str)
		obj (Any)
	Returns: None.
	"""
	print(msg)
	pprint(obj)
	raise KeyboardInterrupt
	
