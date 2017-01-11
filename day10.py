#!/bin/python3

import sys

n = int(input().strip())

bin = []
while n != 0:
    binTemp = n%2
    bin.insert(0 , binTemp)
    n = n//2

count = 0
oneCounterArr = []
for i in range(len(bin)):
    if bin[i] == 1:
        count+=1
    elif bin[i] == 0:
        if count > 0:        
            oneCounterArr.append(count)
            count = 0
            
print(max(oneCounterArr))
        