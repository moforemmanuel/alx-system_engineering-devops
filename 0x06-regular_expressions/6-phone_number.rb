#!/usr/bin/env ruby
#phone number digits (10)

puts ARGV[0].scan(/^\d{10,10}$/).join
