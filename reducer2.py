#!/usr/bin/env python

from operator import itemgetter
import sys
import collections

if __name__ == '__main__':

    word2count = dict()

    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)
        count = int(count)

        if word in word2count:
            word2count[word] = word2count[word] + count
        else:
            word2count[word] = count

    for word in word2count.keys():
        sys.stdout.write('{0}\t{1}\n'.format(word, word2count[word]))
