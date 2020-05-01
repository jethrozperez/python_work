### Write a program to read through mbox-short.txt and figure out the distribution by
### hour of the day for each of the messages. You can pull the hour of
## from the 'From:' line by finding the time and then spitting the string a second time
## using a colon
name = input('Enter file: ')
hours_dict = dict()
lst = list()
try:
    fhand = open(name)
except:
    print('Not a file')
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    indx = words[5].find(':')
    hour = words[5][:indx]
    if hour not in hours_dict:
        hours_dict[hour] = 1
    else:
        hours_dict[hour] += 1


for k,v in list(hours_dict.items()):
    lst.append((k,v))

lst.sort()


for key, val in lst:
    print(key,val)
