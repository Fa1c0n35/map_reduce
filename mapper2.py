#!/usr/bin/env python

from operator import itemgetter
import sys
import collections

if __name__ == '__main__':
    for line in sys.stdin:
        words = line.split()
        words2 = collections.deque(words)
        words2.rotate(1)

        words = list(map(lambda a, b: a + " " + b, list(words2), words))
        del words[0]

        for word in words:
            sys.stdout.write('{0}\t1\n'.format(word))
