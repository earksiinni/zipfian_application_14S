#!/usr/bin/env ruby

min, max = ARGV[0].to_i, ARGV[1].to_i

extras = lambda { |mlt, off| (((max - (min - min % mlt + mlt * (min % mlt == 0 ? 0 : 1))) / mlt).floor + 1) * off }

puts max - min + 1 + extras.call(3, 2) + extras.call(5, 4) + extras.call(15, 8)