import pandas as pd
import matplotlib.pyplot as plt
# from ImportAlpha import change_column_names, input_from_array
import os

def alf_loadData(path):

    "Imports data, changes names, and reduces memory usage!"

    df = pd.read_csv(path, encoding = "ISO-8859-1", sep=';', parse_dates=['Timestamp'], header = 0).iloc[::6]
    df = change_column_names(df)

    timedates=df.iloc[:,0]

    df=df.iloc[:,1:].astype('float32')
    df.insert(0,"Timestamp",timedates)

    return df


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

    columns_new = ['FF_MS01', 'FF_MS02', 'FF_MS03', 'FF_MS04', 'FF_MS05', 'FF_MS06', 'FF_MS07', 'FF_MS08', 
               'Impp_MS01', 'Impp_MS02', 'Impp_MS03', 'Impp_MS04', 'Impp_MS05', 'Impp_MS06', 'Impp_MS07', 'Impp_MS08', 'irradiance_MS01', 'irradiance_MS02', 'irradiance_MS03', 'irradiance_MS04', 'irradiance_MS05', 'irradiance_MS06', 'irradiance_MS07', 'irradiance_MS08', 
               'irradiance_yield_MS01', 'irradiance_yield_MS02', 'irradiance_yield_MS03', 'irradiance_yield_MS04', 'irradiance_yield_MS05', 'irradiance_yield_MS06', 'irradiance_yield_MS07', 'irradiance_yield_MS08', 'Isc_MS01', 'Isc_MS02', 'Isc_MS03', 'Isc_MS04', 'Isc_MS05', 'Isc_MS06', 'Isc_MS07', 'Isc_MS08', 'MPP_MS01', 'MPP_MS02', 'MPP_MS03', 'MPP_MS04', 'MPP_MS05', 'MPP_MS06', 'MPP_MS07', 'MPP_MS08', 
               'temp_MS01', 'temp_MS02', 'temp_MS03', 'temp_MS04', 'temp_MS05', 'temp_MS06', 'temp_MS07', 'temp_MS08','Vmpp_MS01', 'Vmpp_MS02', 'Vmpp_MS03', 'Vmpp_MS04', 'Vmpp_MS05', 'Vmpp_MS06', 'Vmpp_MS07', 'Vmpp_MS08', 'Voc_MS01', 'Voc_MS02', 'Voc_MS03', 'Voc_MS04', 'Voc_MS05', 'Voc_MS06', 'Voc_MS07', 'Voc_MS08']


    columns_old = columns_old[1:-1]
    for (i,j) in zip(columns_old, columns_new):
        dataframe = dataframe.rename(columns={i:j}) 
    
    meteo_columns_old = ['Timestamp', 'humidity_1 - Ambient Humidity [%] (Alpha Centauri - Meteo)', 'irradiation_1 - CMP10-1 Tracker [W/m²] (Alpha Centauri - Meteo)', 'irradiation_2 - CMP10-2 Tracker [W/m²] (Alpha Centauri - Meteo)', 'irradiation_3 - Pyrheliometer Tracker [W/m²] (Alpha Centauri - Meteo)', 'precipitation_1 - Rain Amount [mm] (Alpha Centauri - Meteo)', 'temperature_1 - Ambient Temperature [°C] (Alpha Centauri - Meteo)', 'winddirection_1 - Wind Direction [°] (Alpha Centauri - Meteo)', 'windspeed_1 - Wind Speed [m/s] (Alpha Centauri - Meteo)', '¹ Calculated value']
 
    meteo_columns_new = ["ambient_humidity", "irradiation_1", "irradiation_2", 
                     "irradiation_3", "rain", "ambient_temperature", "wind_direction", 
                     "wind_speed"]
    
    meteo_columns_old = meteo_columns_old[1:-1]
    for (i,j) in zip(meteo_columns_old, meteo_columns_new):
        dataframe = dataframe.rename(columns={i:j})
    return dataframe




def alf_plotMPP(df):
    
    aux = input('Enter module name(s) separated by space comma (ex. MSXX, MSXX, MSXX): ').split(', ')
    string='MPP '
    moduleMPP=[string + i for i in aux]

    df_sliced=date_slicer(df) 
    df_sliced.plot(x = 'Timestamp', y = moduleMPP, figsize=(10,8))
    plt.legend(aux)


# def slicer(df):

#     aux_inpt=input('Enter start and end dates separated by semicolon space (YYYY-MM-DD; YYYY-MM-DD): ').split('; ')

#     start_date,end_date = aux_inpt[0], aux_inpt[1]

#     start_time = df[df['Timestamp'].astype(str).str.contains(start_date)].iloc[0].astype(str).iloc[0][-8:]
#     end_time = df[df['Timestamp'].astype(str).str.contains(end_date)].iloc[-1].astype(str).iloc[0][-8:]

#     df = df.set_index(['Timestamp'])



#     aux=df.loc[str(start_date)+' '+start_time:str(end_date)+' '+end_time]
#     aux.reset_index(inplace=True) 

#     return aux



def alf_JoinAndLoad():

    while True:
        try:
            path =input('Please enter the directory containing the csv files: ')
            filenames = [f for f in os.listdir(path) if f.endswith('.csv')]
            break
        except FileNotFoundError:
            print('Invalid path. Please try again')
       

    # Read each file into a separate dataframe and store them in a list
    df_list = []
    for file in filenames:
        df_list.append(pd.read_csv(path+str(file), encoding = "ISO-8859-1", sep=';', parse_dates=['Timestamp'], header = 0).iloc[::6])

    # Concatenate the list of dataframes into a single dataframe
    for f in df_list:
        f.reset_index(drop=True,inplace=True)

    df = pd.concat(df_list, axis=1)

    

    timedates=df.iloc[:,0]


    # Drop possible duplicate columns
    # df = df.T.drop_duplicates().T
    df = df.loc[:,~df.columns.duplicated()].copy()

    # Rename columns
    df = change_column_names(df)

    # Reduce memory usage
    df=df.iloc[:,1:].astype('float32')
    df.insert(0,"Timestamp",timedates)


    return df



def alf_plotter(df):

    numPlots = int(input('How namy plots?:'))


    print(df.columns)

    

    while True:
        try:
            variables=input('Enter variables from the list separated by semicolon space: ').split('; ')
            check =  any(item in variables for item in df.columns)


            if not check:
                raise ValueError("Invalid input")
            

            if len(variables) != numPlots:
                raise ValueError(f"Choose {numPlots} variables")
            break

        except ValueError as e:
            print(e)
            print('Try again')

    

    for i in range(numPlots):
        df.plot(x='Timestamp', y=variables[i], figsize=(10,8))

def alf_2var_plotter(df):

    df = date_slicer(df)

    from matplotlib import rc
    rc('font', weight='bold')

    

    print(df.columns)

    while True:
        try:
            variables=input('Enter 2 variables from the list separated by semicolon space: ').split('; ')
            check =  all(item in df.columns for item in variables)


            if not check:
                raise ValueError("Invalid input")
            

            if len(variables) != 2:
                raise ValueError(f"Choose only {2} variables")
            break

        except ValueError as e:
            print(e)
            print('Try again')

    

    fig, ax = plt.subplots()

    colors = ['gray','tab:blue']

    df.plot(color=colors[0],x='Timestamp',y = variables[0], figsize=(10,8), ax=ax)

    ax1 = ax.twinx()
    df.plot(color=colors[1],x='Timestamp',y = variables[1], ax = ax1, grid=False)

    ax1.spines['top'].set_linewidth(3.5)
    ax1.spines['bottom'].set_linewidth(3.5)

    ax1.spines['left'].set_color(colors[0])
    ax1.spines['left'].set_linewidth(3.5)

  

    ax1.spines['right'].set_color(colors[1])
    ax1.spines['right'].set_linewidth(3.5)

    ax.legend(loc=( 0.15, 1.02))
    ax1.legend(loc=(0.55, 1.02))

def date_slicer(df):

    while True:
        try:
            aux_inpt=input('Enter start and end dates separated by semicolon space (YYYY-MM-DD; YYYY-MM-DD): ').split('; ')

            if len(aux_inpt) != 2:
                raise ValueError('Invalid input')


            if not df['Timestamp'].astype(str).str.contains(aux_inpt[0]).any():
                raise ValueError('Invalid start date')
            if not df['Timestamp'].astype(str).str.contains(aux_inpt[1]).any():
                raise ValueError('Invalid end date')
            break

        except ValueError as e:
            print(e)
            print('Try again')


    start_date,end_date = aux_inpt[0], aux_inpt[1]

    start_time = df[df['Timestamp'].astype(str).str.contains(start_date)].iloc[0].astype(str).iloc[0][-8:]
    end_time = df[df['Timestamp'].astype(str).str.contains(end_date)].iloc[-1].astype(str).iloc[0][-8:]

    df = df.set_index(['Timestamp'])



    aux=df.loc[str(start_date)+' '+start_time:str(end_date)+' '+end_time]
    aux.reset_index(inplace=True) 

    return aux




def select_panel(df):

    panels = ['MS01','MS02','MS03','MS04',
              'MS05','MS06','MS07','MS08',]

    print(panels)

    while True:
        try:
            panel = input('Select one panel from the list: ')

            if panel not in panels:
                raise ValueError('Panel not in list')
            break
        except ValueError as e:
            print(e)
            print('Try again')

    df_panel = df[[i for i in df.columns if panel in i]].copy()

    return df_panel