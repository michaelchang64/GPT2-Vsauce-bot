import os
import re

train_doc = []
val_doc = []

with open("vsauce_transcripts.txt",'r') as f:
    file_input=f.readlines()

count = 0
for count, line in enumerate(file_input):
    if count <= len(file_input) * 0.9:
        train_doc.append(line)
        count += 1
    else:
        val_doc.append(line)

f = open('train_vsauce.txt', "w+")
count = 0
for line in train_doc:
    count += 1
    f.write(str(line))
    f.write("\n")

print("lines in training:", count)

f.close()

f = open('val_vsauce.txt', "w+")
count = 0
for line in val_doc:
    count += 1
    f.write(str(line))
    f.write("\n")

print("lines in val:", count)

f.close()
