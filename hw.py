import re

file = open('regex_sum_641768.txt')

ints = re.findall('[0-9]+', file.read())
sum = sum([int(i) for i in ints])
print(sum)
