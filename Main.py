# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 12:49:20 2022

@author: minah

This script is meant for data from Alpha Centauri laboratory downloaded from PV.analyzer.
"""


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
#import math as m
from ImportAlpha import *
import os





  

# Kjør:
    

    
df = joinAndLoad()
    
# input: ../data/testJoin/

#%%    
mainMenu = ["1. Energy production",
            "2. Output power", "3. Exit"]
while True:
    menuDisplay = [" ","---------------------------"," ","Select a parameter to be investigated:",""]
    for e in menuDisplay:
        print(e)
    for i in range(len(mainMenu)):
        print(mainMenu[i])
    
    mainMenuChoice = input("Please enter a menu item number: ")
    
    if mainMenuChoice == "1": 
        printEnergy = energyProdDay(df)
        
        
    elif mainMenuChoice == "2":
        

        plotMPP(df)
        #plotPowerOneDay(data)

        
    elif MainMenuChoice == "3":
        break
    else:
        print("")
        print("{} is not a menu item number.".format(MainMenuChoice))
    
    
        
    
    



"""
lage liste av alle kolonner

kolonner =list(data)
kolonner.insert(1,MS01_old_names[0])
kolonner.insert(1,MS01_old_names[0])
kolonner[2] = kolonner[2][:-2]
kolonner[2] = kolonner[2] + "2)"
kolonner.insert(9,MS01_old_names[1])
kolonner.insert(9,MS01_old_names[1])
kolonner[10] = kolonner[10][:-2]
kolonner[10] = kolonner[10] + "2)"
kolonner.insert(17,MS01_old_names[2])
kolonner.insert(17,MS01_old_names[2])
kolonner[18] = kolonner[18][:-2]
kolonner[18] = kolonner[18] + "2)"
kolonner.insert(25,MS01_old_names[3])
kolonner.insert(25,MS01_old_names[3])
kolonner[26] = kolonner[26][:-2]
kolonner[26] = kolonner[26] + "2)"
kolonner.insert(33,MS01_old_names[4])
kolonner.insert(33,MS01_old_names[4])
kolonner[34] = kolonner[34][:-2]
kolonner[34] = kolonner[34] + "2)"
kolonner.insert(41,MS01_old_names[5])
kolonner.insert(41,MS01_old_names[5])
kolonner[42] = kolonner[42][:-2]
kolonner[42] = kolonner[42] + "2)"
kolonner.insert(49,MS01_old_names[6])
kolonner.insert(49,MS01_old_names[6])
kolonner[50] = kolonner[50][:-2]
kolonner[50] = kolonner[50] + "2)"
kolonner.insert(57,MS01_old_names[7])
kolonner.insert(57,MS01_old_names[7])
kolonner[58] = kolonner[58][:-2]
kolonner[58] = kolonner[58] + "2)"
kolonner.insert(65,MS01_old_names[8])
kolonner.insert(65,MS01_old_names[8])
kolonner[66] = kolonner[66][:-2]
kolonner[66] = kolonner[66] + "2)"
"""







"""
tips 

  # Velger kolonner
    RawData = RawData[['Timestamp','Device number', 'Open circuit voltage value 1 [V]',
                 'Short circuit current value 1 [A]','MPP voltage value 1 [V]',
                 'Maximum current value 1 [A]']] 

Gjøre streng om til variabelnavn
streng = "variabelnavn"
myVars = locals()
myVars[streng] = "variabelverdi"

"""


