#!/usr/bin/env ruby
#textme extract

puts ARGV[0].scan(/[A-Z\s]+/).join
