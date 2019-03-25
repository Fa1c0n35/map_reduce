#!/usr/bin/env python

from operator import itemgetter
import sys

if __name__ == '__main__':
	for line in sys.stdin:
		for word in line.split():
			sys.stdout.write('{0}\t1\n'.format(word))
