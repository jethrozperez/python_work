### Find the number in the text
### below and using find() and slicing
### Convert the number extracted into floating point

text = "X-DSPAM-Confidence:    0.8475";
numb = '0.8475'

indx = (text.find(numb))

print(float(text[indx:]))
