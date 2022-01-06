#!/usr/bin/env ruby
#textme extract

puts ARGV[0].scan(/(?<=from:|to:|flags:).*?(?=\])/).join(',')
