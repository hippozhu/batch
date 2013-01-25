#!/usr/bin/python

f_crux_test = open('crux2.test')
ninst = 0
correct = 0
for line in f_crux_test:
  if int(line.split()[0]) == 0:
    correct += 1
  ninst += 1

f_crux_test.close()

print 1.0*correct/ninst

