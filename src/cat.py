import fileinput
import sys

def _simple_cat():
	"""Cannonical implementation that doesn't work like UNIX cat for stdin"""
	for line in fileinput.input():
		sys.stdout.write(line)


def cat(paths):
	"""Concatenates the input files and writes to stdout
	
	Parameters:
	pathlist: a list of files to concatenate
	
	"""
	for path in paths:
		try:
			fd = open(path, 'r')
			sys.stdout.write(fd.read())
		finally:
			fd.close()

def stdincat():
	"""Writes stdin to std out one line at a time"""
	for line in sys.stdin:
		sys.stdout.write(line)


def main(args):
	if len(args) == 0:
		stdincat()
	else:
		cat(args)


if __name__ == '__main__':
	main(sys.argv[1:])
