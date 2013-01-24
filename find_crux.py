#!/usr/bin/python
import sys

def crux(tt):
  labels = []
  f_class = open(tt + '.class')
  f_predict = open('svm_' + tt + '.predict')
  for line in f_class:
    real = int(line)
    predict = int(f_predict.readline())
    if real == 1 and predict == 1:
      labels.append(1)
    elif real == -1 and predict == -1:
      labels.append(0)
    elif real == 1 and predict == -1:
      labels.append(3)
    else:
      labels.append(2)
  f_class.close()
  f_predict.close()
  
  f_out = open('crux' + sys.argv[2] + '.' + tt, 'w')
  f_data = open('svm_' + tt + '.scale')
  ino = 0
  for line in f_data:
    output_label = labels[ino]
    if nc == 2:
      output_label /= 2	
    f_out.write(str(output_label))
	
    features = [.0] * nf
    for feat in line.strip().split()[1:]:
      idx = int(feat.split(':')[0])
      features[idx - 1] = float(feat.split(':')[1])	
    
    for i in range(nf):
      f_out.write(' ' + str(i + 1) + ':' + str(features[i]))
	
    f_out.write('\n')
    ino += 1
	
  f_out.close()
  f_data.close()

nf = int(sys.argv[1])
nc = int(sys.argv[2])

crux('train')
crux('test')
