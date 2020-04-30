### Write a program to read through mbox-short.txt and figure out who has send the
### greatest number of mail messages. The program looks for 'From ' lines
### and takes the second word of those lines as the person who sent the mail
### The program creates a Python dictionary that maps the sender's mail address
### to a count of the number of times they appear in the file. The program then
### reads through the dictionary using a maximum loop to find the most prolific committer

email_list = dict()
fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('Error. Cannot fine file', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        word = words[1]
        if words[1] not in email_list:
            email_list[words[1]] = 1
        else:
            email_list[words[1]] += 1
largest = 0
for key in email_list:
    if email_list[key] > largest:
        largest = email_list[key]
        largest_email = key
print(largest_email,largest)
    ##print(key,email_list[key])
