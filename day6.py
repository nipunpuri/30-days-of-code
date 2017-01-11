# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:58:23 2017

@author: nipun
"""
numCase = int(input()) #The first line in the input is the number of lines in the program
for a in range(numCase): #Iterate the loop for each input value.
        
    S = input() #The default input is a string
    myLst = str.split(S , " ") #Since, 
    
    for j in myLst:
        evenS = "" #Initialising the string where I'll store my even chars
        oddS = ""
        for i in range(0, len(j)):
            if i%2 == 0:#i.e. if it is even
                evenS+=S[i]
            else:
                oddS+=S[i]        
        print(evenS + " " + oddS)
    