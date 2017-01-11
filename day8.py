# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:37:53 2017

@author: nipun
"""

n = int(input().strip())
dict = {}#Initialise the dictionary
#arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(n):
    arrTemp = input().split(' ') #The input is a string and the split method returns a list of 2 elements
    dict[arrTemp[0]] = int(arrTemp[1]) #Store the elements in the dictinary as a key value pair
    

while True:
    keyTemp = input()
    if len(keyTemp) == 0:
        break
    elif keyTemp in dict:
        print(keyTemp + "=" + str(dict[keyTemp]))
    else:
        print("Not found")