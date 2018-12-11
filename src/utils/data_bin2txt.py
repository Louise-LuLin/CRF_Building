__author__ = 'lulin'

import pickle

prefix = '../dataset/'
source = 'filtered'

labels = []
strings = []
with open(prefix + source + "_dataset.bin", "rb") as ibm_dataset:
    labels = pickle.load(ibm_dataset)
with open(prefix + source + "_string.bin", "rb") as ibm_string:
    strings = pickle.load(ibm_string)

f = open(prefix + source + '_label.txt', 'w')
for sample in labels:
    for label in sample:
        f.write(str(label[2]) + ',')
    f.write('\n')
f.close()

f = open(prefix + source + '_string.txt','w')
for string in strings:
    f.write(str(string) + '\n')
f.close()
