#!/usr/bin/env python3
import sys

def unescape_file(path):
	r"""Returns the unicode-unescaped string representing the content of a file
	
	Reads a file containing unicode escape sequences (\uXXXX) returns a 
	unicode string containing the correct unicode representation of the 
	contents
	
	Note: this simple implementation will probably not scale to very large
	files
	
	"""
	with open(path, 'r') as fd:
		s = fd.read()
	return unescape_str(s)


def unescape_str(s):
	r"""Returns the unicode-unescaped but otherwise unmodified input string
	
	Re-encodes a string to replace unicode escape sequences (\uXXXX) with
	their unicode equivalents
	
	"""
	return s.encode('utf-8').decode('unicode-escape')


def main(args):
	for arg in args:
		s = unescape_file(arg)
		with open(arg + '.unescaped', 'w', encoding='utf-8') as outfile:
			outfile.write(s)


if __name__ == '__main__':
	main(sys.argv[1:])

