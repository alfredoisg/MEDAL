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
from importAlf import *


  

# Kjør:
    

df = alf_JoinAndLoad()
    
# input: ../Arbeid/Spyder/data/testJoin/
# input: C:\Users\minah\SINTEF\SEP-FS 22 Method Development of Alfa Centauri - Dokumenter\Arbeid\Spyder\data\testJoin

#%%    
mainMenu = ["1. Energy production",
            "2. Plot output power","3. Create several plots", "4. Create plot with 2 variables", "5. Compare parameters from PV modules", "6. Exit"]
while True:
    menuDisplay = [" ","---------------------------"," ","Select a parameter to be investigated:",""]
    for e in menuDisplay:
        print(e)
    for i in range(len(mainMenu)):
        print(mainMenu[i])
    
    mainMenuChoice = input("Please enter a menu item number: ")
    
    if mainMenuChoice == "1": 
        printEnergy = energyProd(df)
            
    elif mainMenuChoice == "2":
        alf_plotMPP(df)
        
    elif mainMenuChoice == "3":
        alf_plotter(df)

    elif mainMenuChoice == "4": 
        alf_2var_plotter(df)
        
    elif mainMenuChoice == "5":
       compareSCmodules(df) 
    
    elif mainMenuChoice == "6":
        break
    else:
        print("")
        print("{} is not a menu item number.".format(MainMenuChoice))
    
    
        
    
# testet alf_plotter, men ingenting skjedde etter at jeg skrev inn variabler
# Plott genereres ikke før programmet er ferdig. Selv om jeg kommer tilbake til meny, må menyen avsluttes før plottet kommer opp
#select_panel: feilmelding hvis panelet ikke er i dataframe?
#fjerne x-aksetittel "Timestamp" i plot





