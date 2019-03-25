#!/usr/bin/env python

from operator import itemgetter
import sys

if __name__ == '__main__':
	curkey = None
	total = 0
	for line in sys.stdin:
		key, val = line.split('\t',1)
		val = int(val)

		if key == curkey:
			total += val
		else:
			if curkey is not None:
				sys.stdout.write('{0}\t{1}\n'.format(curkey, total))
			curkey = key
			total = val

	sys.stdout.write('{0}\t{1}\n'.format(curkey, total))
