#!/usr/bin/env python3
import sys
import getopt

newline = '\n'
space = ' '
omitnewline = False

def main():
	global omitnewline
	options, args = getopt.getopt(sys.argv[1:], 'n')
	sys.stdout.write(space.join(args))
	
	for opt in options:
		if '-n' in opt:
			omitnewline = True
			break
	if not omitnewline:
		sys.stdout.write(newline)


if __name__ == "__main__":
	main()

