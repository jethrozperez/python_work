import re

fhand = open('regex_test.txt')
lst = list()
count = 0
for line in fhand:
   line = line.rstrip()
   x = re.findall('([0-9]+)', line)
   if len(x) > 0:
       lst = lst + x

y = 0
count = 0
for item in lst:
    item = int(item)
    y = y + item
    count = count + 1

print('total is',y,'\ncount is', count)
