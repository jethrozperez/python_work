## Open the file mbox-short.txt and read it line by line.
## When you find a line that starts with 'From' parse the From line using split()
## and print out the second word in the line and then print the count in the end.

fname = input('Enter a file name: ')
count = 0

try:
    fhand  = open(fname)
except:
    print(fhand, 'is not a file.')
    quit()

for line in fhand:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[1])
    count = 1 + count
print("There were", count, "lines in the file with From as the first word")
