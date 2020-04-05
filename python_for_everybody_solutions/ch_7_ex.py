### Write a program that prompts for a file name then opens that file
### and reads through looking for ''X-DSPAM-Confidence:    0.8475'
### Count those lines and extract floating point values, extract the
### value and average those values to produce the output 'Average spam confidence: 0.750718518519'


fname = input('Enter file name: ')
count = 0
tot = 0
col = ':'

try:
    fn = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()


for line in fn:
    if not line.startswith('X-DSPAM-Confidence:') : continue
    indx = (line.find(col))
    value = (line[indx + 1:]).strip()
    num = float(value)
    tot = tot + num
    count = count + 1

average = round(tot/count,12)
print('Average spam confidence:',average)
