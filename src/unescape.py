#!/usr/bin/env python
import sys

def unescape(s):
	return s.encode('utf-8').decode('unicode-escape')

def main(args):
	for arg in args:
		try:
			infile = open(arg, 'r')
			s = infile.read()
		finally:
			infile.close()
		s = unescape(s)
		try:
			outfile = open(arg + '.unescaped', 'w', encoding='utf-8')
			outfile.write(s)
		finally:
			outfile.close()
		return True

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))

