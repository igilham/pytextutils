#!/usr/bin/env python
import sys
import getopt

#parser = optparse.OptionParser()
#parser.add_options('-n' '--omit-newline', dest="omit_newline", 
#					action="store-true", help='omit trailing newline',
#					default=False)


def main():
	options, args = getopt.getopt(sys.argv[1:], 'n')
	
	newline = '\n'
	if '-n' in options:
		newline = ''
	for arg in args:
		print(arg, end=newline)


if __name__ == "__main__":
	main()

