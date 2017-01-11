# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:58:23 2017

@author: nipun
"""

S = "YellowSubmarine"
evenS = "" #Initialising the string where I'll store my even chars
oddS = ""
for i in range(0 , len(S)):
    if i%2 == 0:#i.e. if it is even
        evenS+=S[i]
    else:
        oddS+=S[i]
        
print(evenS)
    