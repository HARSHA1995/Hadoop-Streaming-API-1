#!/usr/bin/env python

import sys
for line in sys.stdin:
        line = line.strip()
        count=0
        words = line.split(",")
        if words[0] != "DATE":
                for word in reversed(words):
                        count=count+1
                        if count<6 and word != "" and word[0]!="\"" and word[-1]!="\"":
                                print '%s\t%s' % (word,1)