#!/bin/bash

# usage: ./find_crux.sh diabetes 8

for i in {0..9}
do
  cd ~/crux/$1/fold$i
  ~/crux/find_crux.py $2 2 
  ~/crux/find_crux.py $2 4
done

