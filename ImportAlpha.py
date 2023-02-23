# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:51:46 2022

@author: minah

This script contains functions to be imported to main script meant for data from Alpha Centauri laboratory   ..Functions to be imported to main file 

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def input_from_array(prompt, array, message):
    """
    Gives the user a new chance to enter a valid input if they enter an invalid input. The message to be printed if the value is invalid is an input. The input array is valid alternatives.
    
    Parameters:
        prompt : str
        array : array
        message : str
    Returns:
        value : str
    """
    
    while True:
        try:
            value = input(prompt)
            if value in array:
                return value
            else:
                raise ValueError
        except ValueError:
            print(message)
            
            
            
def change_column_names(dataframe):
    """
    Replaces long columnn names with shorter and better column names

    Parameters:
        dataframe : DataFrame
    Returns
        dataframe : DataFrame
    """
    
    columns_old = ['Timestamp', 'Fill factor ¹ (Alpha Centauri - M2-MS01)', 'Fill factor ¹ (Alpha Centauri - M2-MS02)', 'Fill factor ¹ (Alpha Centauri - M3-MS03)', 'Fill factor ¹ (Alpha Centauri - M3-MS04)', 'Fill factor ¹ (Alpha Centauri - M4-MS05)', 'Fill factor ¹ (Alpha Centauri - M4-MS06)', 'Fill factor ¹ (Alpha Centauri - M1-MS07)', 'Fill factor ¹ (Alpha Centauri - M1-MS08)', 
                   'Impp [A] (Alpha Centauri - M2-MS01)', 'Impp [A] (Alpha Centauri - M2-MS02)', 'Impp [A] (Alpha Centauri - M3-MS03)', 'Impp [A] (Alpha Centauri - M3-MS04)', 'Impp [A] (Alpha Centauri - M4-MS05)', 'Impp [A] (Alpha Centauri - M4-MS06)', 'Impp [A] (Alpha Centauri - M1-MS07)', 'Impp [A] (Alpha Centauri - M1-MS08)',
                   'irradiance [W/m²] (Alpha Centauri - M2-MS01)', 'irradiance [W/m²] (Alpha Centauri - M2-MS02)', 'irradiance [W/m²] (Alpha Centauri - M3-MS03)', 'irradiance [W/m²] (Alpha Centauri - M3-MS04)', 'irradiance [W/m²] (Alpha Centauri - M4-MS05)', 'irradiance [W/m²] (Alpha Centauri - M4-MS06)', 'irradiance [W/m²] (Alpha Centauri - M1-MS07)', 'irradiance [W/m²] (Alpha Centauri - M1-MS08)', 
                   'Irradiation Yield ¹ [Wh/m²] (Alpha Centauri - M2-MS01)', 'Irradiation Yield ¹ [Wh/m²] (Alpha Centauri - M2-MS02)', 'Irradiation Yield ¹ [Wh/m²] (Alpha Centauri - M3-MS03)', 'Irradiation Yield ¹ [Wh/m²] (Alpha Centauri - M3-MS04)', 'Irradiation Yield ¹ [Wh/m²] (Alpha Centauri - M4-MS05)', 'Irradiation Yield ¹ [Wh/m²] (Alpha Centauri - M4-MS06)', 'Irradiation Yield ¹ [Wh/m²] (Alpha Centauri - M1-MS07)', 'Irradiation Yield ¹ [Wh/m²] (Alpha Centauri - M1-MS08)', 
                   'isc [A] (Alpha Centauri - M2-MS01)', 'isc [A] (Alpha Centauri - M2-MS02)', 'isc [A] (Alpha Centauri - M3-MS03)', 'isc [A] (Alpha Centauri - M3-MS04)', 'isc [A] (Alpha Centauri - M4-MS05)', 'isc [A] (Alpha Centauri - M4-MS06)', 'isc [A] (Alpha Centauri - M1-MS07)', 'isc [A] (Alpha Centauri - M1-MS08)', 
                   'MPP ¹ [W] (Alpha Centauri - M2-MS01)', 'MPP ¹ [W] (Alpha Centauri - M2-MS02)', 'MPP ¹ [W] (Alpha Centauri - M3-MS03)', 'MPP ¹ [W] (Alpha Centauri - M3-MS04)', 'MPP ¹ [W] (Alpha Centauri - M4-MS05)', 'MPP ¹ [W] (Alpha Centauri - M4-MS06)', 'MPP ¹ [W] (Alpha Centauri - M1-MS07)', 'MPP ¹ [W] (Alpha Centauri - M1-MS08)', 
                   'tm [°C] (Alpha Centauri - M2-MS01)', 'tm [°C] (Alpha Centauri - M2-MS02)', 'tm [°C] (Alpha Centauri - M3-MS03)', 'tm [°C] (Alpha Centauri - M3-MS04)', 'tm [°C] (Alpha Centauri - M4-MS05)', 'tm [°C] (Alpha Centauri - M4-MS06)', 'tm [°C] (Alpha Centauri - M1-MS07)', 'tm [°C] (Alpha Centauri - M1-MS08)', 
                   'vmpp [V] (Alpha Centauri - M2-MS01)', 'vmpp [V] (Alpha Centauri - M2-MS02)', 'vmpp [V] (Alpha Centauri - M3-MS03)', 'vmpp [V] (Alpha Centauri - M3-MS04)', 'vmpp [V] (Alpha Centauri - M4-MS05)', 'vmpp [V] (Alpha Centauri - M4-MS06)', 'vmpp [V] (Alpha Centauri - M1-MS07)', 'vmpp [V] (Alpha Centauri - M1-MS08)', 
                   'voc [V] (Alpha Centauri - M2-MS01)', 'voc [V] (Alpha Centauri - M2-MS02)', 'voc [V] (Alpha Centauri - M3-MS03)', 'voc [V] (Alpha Centauri - M3-MS04)', 'voc [V] (Alpha Centauri - M4-MS05)', 'voc [V] (Alpha Centauri - M4-MS06)', 'voc [V] (Alpha Centauri - M1-MS07)', 'voc [V] (Alpha Centauri - M1-MS08)', '¹ Calculated value']
    columns_new = ['FF MS01', 'FF MS02', 'FF MS03', 'FF MS04', 'FF MS05', 'FF MS06', 'FF MS07', 'FF MS08', 
                   'Impp MS01', 'Impp MS02', 'Impp MS03', 'Impp MS04', 'Impp MS05', 'Impp MS06', 'Impp MS07', 'Impp MS08', 
                   'irradiance MS01', 'irradiance MS02', 'irradiance MS03', 'irradiance MS04', 'irradiance MS05', 'irradiance MS06', 'irradiance MS07', 'irradiance MS08', 
                   'irradiance yield MS01', 'irradiance yield MS02', 'irradiance yield MS03', 'irradiance yield MS04', 'irradiance yield MS05', 'irradiance yield MS06', 'irradiance yield MS07', 'irradiance yield MS08', 
                   'Isc MS01', 'Isc MS02', 'Isc MS03', 'Isc MS04', 'Isc MS05', 'Isc MS06', 'Isc MS07', 'Isc MS08', 
                   'MPP MS01', 'MPP MS02', 'MPP MS03', 'MPP MS04', 'MPP MS05', 'MPP MS06', 'MPP MS07', 'MPP MS08', 
                   'temp MS01', 'temp MS02', 'temp MS03', 'temp MS04', 'temp MS05', 'temp MS06', 'temp MS07', 'temp MS08',
                   'Vmpp MS01', 'Vmpp MS02', 'Vmpp MS03', 'Vmpp MS04', 'Vmpp MS05', 'Vmpp MS06', 'Vmpp MS07', 'Vmpp MS08', 
                   'Voc MS01', 'Voc MS02', 'Voc MS03', 'Voc MS04', 'Voc MS05', 'Voc MS06', 'Voc MS07', 'Voc MS08']
    columns_old = columns_old[1:-1]
    for (i,j) in zip(columns_old, columns_new):
        dataframe = dataframe.rename(columns={i:j}) 
    meteo_columns_old = ['Timestamp', 'humidity_1 - Ambient Humidity [%] (Alpha Centauri - Meteo)', 'irradiation_1 - CMP10-1 Tracker [W/m²] (Alpha Centauri - Meteo)', 'irradiation_2 - CMP10-2 Tracker [W/m²] (Alpha Centauri - Meteo)', 'irradiation_3 - Pyrheliometer Tracker [W/m²] (Alpha Centauri - Meteo)', 'precipitation_1 - Rain Amount [mm] (Alpha Centauri - Meteo)', 'temperature_1 - Ambient Temperature [°C] (Alpha Centauri - Meteo)', 'winddirection_1 - Wind Direction [°] (Alpha Centauri - Meteo)', 'windspeed_1 - Wind Speed [m/s] (Alpha Centauri - Meteo)', '¹ Calculated value']
    meteo_columns_new = ["ambient humidity", "irradiation 1", "irradiation 2", "irradiation 3", "rain", "ambient temperature", "wind direction", "wind speed"]
    meteo_columns_old = meteo_columns_old[1:-1]
    for (i,j) in zip(meteo_columns_old, meteo_columns_new):
        dataframe = dataframe.rename(columns={i:j})
    return dataframe
            




def load_data(FileName):
    """
    Loads data file
    Turn Timestamp column from str type to datetime64 type
    Trims the frame from 6 measurements per minute to 1 measurement per minute
    Changes column names
    
    Parameters:
        FileName : str
    Returns:
        data : DataFrame
    """
    data = pd.read_csv(FileName, encoding = "ISO-8859-1", sep=';', parse_dates=['Timestamp'], header = 0).iloc[::6]
 
    data.set_index('Timestamp', inplace=True)
    
    data = change_column_names(data)
    
    return data






def set_timeframe(dataframe): # må fikse feilmelding
    print("")
    print("The data file starts at {}.".format(dataframe.index[0]))
    print("The data file ends at {}.".format(dataframe.index[-1]))
    start = input("In the same time-format, what date and time would you like to start at? ")
    end = input("In the same time-format, what date and time would you like to end at? ")
    return start, end



def energyProd(data):
    """
    Calculates energy production from one day in kWh 
    
    Parameters
    ----------
    data : DataFrame
        
    Returns
    -------
    energy : float64

    """
    MS = []
    mpp = 'MPP_MS01', 'MPP_MS02', 'MPP_MS03', 'MPP_MS04', 'MPP_MS05', 'MPP_MS06', 'MPP_MS07', 'MPP_MS08'
    for e in mpp:
        if e in list(data):
            MS.append(e[-4:])
    while True: 
        if len(MS) == 1:
            energy = np.sum(data['MPP_{}'.format(MS[0])]) *60/3600000 # 60 sec between measurements, 3600000 for conversion to kWh
            print("")
        
            break
        else:
            print(" ")
            print("-------------------------------------------------")          
            menu = ["Calculate energy production from which PV-module?", "Alternatives:"]
            for e in MS:
                menu.append(e)
            for i in menu:
                print(i)
            module = input_from_array("Please enter module name: ", menu, "Value error. This is not an accessible module name.")
            energy = np.sum(data['MPP_{}'.format(module)]) *60/3600000 # 60 sec between measurements, 3600000 for conversion to kWh
            print("")
            
            break

    return print ("Energy production this period for {} was {:.2f} kWh.".format(module,energy))





def plotPowerOneDay(data):
    """
    Creates a plot of power output one day from PV-moules 
    User decides time interval and PV-modules

    Parameters:
        data : DataFrame
    Returns
        plot
    """
    loaded_modules = []
    mpp = ['MPP MS01', 'MPP MS02', 'MPP MS03', 'MPP MS04', 'MPP MS05', 'MPP MS06', 'MPP MS07', 'MPP MS08']
    for e in mpp:
        if e in list(data):
            loaded_modules.append(e[-4:]) # creates a list of the loaded module names
    while True: 
        break_out_flag = False
        print(" ")
        print("-------------------------------------------------")
        time_int = int(input("How many minutes as time interval? ")) # enter time interval

        start,end = set_timeframe(data)
        

        data2 = data.loc[::time_int] # new dataframe with selected indexes 
        time = data2.index.astype(str).tolist()
        print(" ")
        print("-------------------------------------------------")          
        N = len(loaded_modules)
        menu = ["Plot power from from which PV-module(s)?"]
        for e in loaded_modules:
            menu.append(e)
        for i in menu:
            print(i) # prints the names of the selectable modules
        module = input("The limit is {0} modules. Enter module name(s) separated by comma(ex. MSXX,MSXX,MSXX): ".format(N))
        modules = module.split(",")
        plotted = [] # list with plottet modules
        time2 = [] # list of ticks
        symb = ['^','s','v','o','d','*','X','.']
        for e in time:
            time2.append(e[11:])
        for n, i in zip(modules,range(len(modules))): 
            if n in menu: # creates a plot if selected modules are loaded
                plotted.append(n)           
                power = data2['MPP {}'.format(n)] # creates a list of power measurements from the selected modules and timestamps
                if len(time2) >= 24: # plot whit line instead of points if more than 24 points
                    ax = plt.plot(time, power,'-', label = n)        
                else:
                    ax = plt.plot(time, power,'{}'.format(symb[i]), label = n)                
                # Design the plot
                plt.xlabel("Time [h]")
                plt.ylabel("Power [W]")
                plt.legend()
                plt.title("{}".format(time[0][:10]))
                ax = plt.gca()
                plt.draw()
                plt.style.library['seaborn-whitegrid']
                plt.style.use('seaborn-whitegrid')
                # Creates 7 ticks 
                ax.set_xticks((time[0], time[int(len(time)/6)], time[int(len(time)/6)*2], time[int(len(time)/6)*3],time[int(len(time)/6)*4], time[int(len(time)/6)*5], time[-1]))
                ax.set_xticklabels((time2[0], time2[int(len(time2)/6)],time2[int(len(time2)/6)*2], time2[int(len(time2)/6)*3],time2[int(len(time2)/6)*4], time2[int(len(time2)/6)*5], time2[-1]))
                ax.tick_params(axis='x', labelrotation=90)

                        
                if n == modules[-1]: # break if the last module is plotted
                    break_out_flag = True
                    plotted = str(plotted)[1:-1]
                    print("Plot including {} is created.".format(plotted))
                    break
            else:
                print("----------------------------------------")
                print("The module name(s) {} could not be interpreted.".format(n))
                print("") 
        if break_out_flag:
            break
                
    return plt.show()


# test change