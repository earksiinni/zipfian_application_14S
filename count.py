#!/usr/bin/env python

import sys

low, high = int(sys.argv[1]), int(sys.argv[2])

def sum_extras(mlt, extra):
    hump  = mlt if low % mlt else 0   # Don't double count first multiple
    soff  = low - (low % mlt) + hump  # Offset starting point for counting no. of multiples
    count = (high - soff) / mlt + 1   # No. of multiples between offset start and max
    total = count * extra             # Add the extra value for each multiple
    return total

print high - low + 1 + sum_extras(3, 2) + sum_extras(5, 4) + sum_extras(15, 8)