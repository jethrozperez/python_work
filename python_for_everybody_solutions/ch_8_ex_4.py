### Python Ch 8 Ex 4
## Open file romeo.txt and read it line by line
## For each line split the line into a list of words using split()
## check each word in the list and if not append it in the list.
## When the program comples sort and print the resulting words in alphebetical order


## Input file name
jp_list = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()                
    for word in words:
        if word in jp_list:
            continue
        jp_list.append(word)
print(sorted(jp_list))
