import pandas as pd
import matplotlib.pyplot as plt
# from ImportAlpha import change_column_names, input_from_array
import os


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
               'Impp_MS01', 'Impp_MS02', 'Impp_MS03', 'Impp_MS04', 'Impp_MS05', 'Impp_MS06', 'Impp_MS07', 'Impp_MS08', 'Irradiance_MS01', 'Irradiance_MS02', 'Irradiance_MS03', 'Irradiance_MS04', 'Irradiance_MS05', 'Irradiance_MS06', 'Irradiance_MS07', 'Irradiance_MS08', 
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
    """
    This function generates a plot of multiple modules' maximum power point (MPP) values.

    Input:
    A dataframe containing the MPP values of the modules

    Output:
    A plot of the MPP values of the selected modules

    Steps:
    1) Prompt the user to enter the names of the modules to be plotted, separated by commas and spaces.

    2) Use the date_slicer function (not defined in this code) to slice the dataframe by date.

    3) Generate a plot of the MPP values of the selected modules using the plot function from the matplotlib library. The x-axis is the Timestamp column and the y-axis is the MPP values of the selected modules. The plot is displayed using the show function from the matplotlib library.

    4) Return nothing.
    """
    
    aux = input('Enter module name(s) separated by space comma (ex. MSXX, MSXX, MSXX): ').split(', ')
    string='MPP_'
    moduleMPP=[string + i for i in aux]

    df_sliced=date_slicer(df) 
    df_sliced.plot(x = 'Timestamp', y = moduleMPP, figsize=(10,8))
    plt.legend(aux)


def alf_JoinAndLoad():
    """
    This function reads in a directory containing .csv files and combines them into a single dataframe.

    Input:
    None

    Output:
    A dataframe with the contents of the combined .csv files

    Steps:
    1) Prompt the user for the path of the directory containing the .csv files. If the path is invalid (i.e. the directory does not exist), an error message is displayed and the user is prompted again.

    2) Find all .csv files in the specified directory and store their filenames in a list.

    3) Read each .csv file into a separate dataframe and store them in a list.

    4) Concatenate the list of dataframes into a single dataframe.

    5) Reset the index of each dataframe in the list to remove any duplicate rows. Drop any duplicate columns in the final dataframe.

    6) Rename the columns of the final dataframe using the change_column_names function (not defined in this code).

    7) Reduce the memory usage of the final dataframe by casting the columns to the float32 data type, except for the first column (Timestamp).

    8) Return the final dataframe.
    """

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
    """
    This function generates a plot of a specified number of variables from a given dataframe.

    Input:
    A dataframe containing the variables to be plotted

    Output:
    A plot of the selected variables

    Steps:
    1) Prompt the user to enter the number of plots to be generated.

    2) Prompt the user to enter the variables to be plotted, separated by semicolon and space. If the user does not enter the correct number of valid variables (i.e. columns in the dataframe), an error message is displayed and the user is prompted again.

    3) Use the plot function from the matplotlib library to generate a plot of each of the selected variables. The x-axis is the Timestamp column and the y-axis is the selected variable. The plot is displayed using the show function from the matplotlib library.

    4) Return nothing.
    """

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
    """
    This function generates a plot of two variables from a given dataframe.

    Input:
    A dataframe containing the variables to be plotted

    Output:
    A plot of the two selected variables

    Steps:
    1) Use the date_slicer function (not defined in this code) to slice the dataframe by date.

    2) Prompt the user to enter two variables to be plotted, separated by a semicolon and space. If the user does not enter two valid variables (i.e. columns in the dataframe), an error message is displayed and the user is prompted again.

    3) Use the plot function from the matplotlib library to generate a plot of the two selected variables. The x-axis is the Timestamp column and the y-axes are the two selected variables. The plot is displayed using the show function from the matplotlib library.

    4) Return nothing.
    """

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
    """
    This function slices a dataframe by date range.

    Input:
    A dataframe containing a Timestamp column

    Output:
    A sliced dataframe

    Steps:
    1) Prompt the user to enter a start and end date, separated by a semicolon and space, in the format YYYY-MM-DD; YYYY-MM-DD.
    
    2) If the input is invalid (e.g. not in the correct format, or the dates do not exist in the Timestamp column), an error message is displayed and the user is prompted again.
    3) Set the Timestamp column as the index of the dataframe.

    4) Slice the dataframe by the start and end dates entered by the user.

    5) Reset the index of the sliced dataframe.

    6) Return the sliced dataframe.
    """

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
    """
    This function selects a panel's data from a given dataframe.

    Input:
    A dataframe containing the data for multiple panels

    Output:
    A dataframe containing the data for the selected panel

    Steps:
    1) Prompt the user to select a panel from the list. If the panel is not in the list, an error message is displayed and the user is prompted again.

    2) Select the data for the selected panel from the dataframe by filtering the columns that contain the panel name.

    3) Return the data for the selected panel.
    """

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
    
    df_panel.insert(0,"Timestamp",df.iloc[:,0])

    return df_panel



def getSCparam(df):
    """
    This function allows the user to select a parameter from a list of predefined parameters and returns a dataframe containing only the columns corresponding to the selected parameter.

    Input:
    A pandas dataframe containing the data to be filtered by parameter.
    
    Output:
    A pandas DataFrame containing only the columns corresponding to the selected parameter, and an additional 'Timestamp' column with the corresponding timestamps.
    
    Steps:
    1) Print the list of predefined parameters and prompt the user to choose one of them.
    
    2) If the user input is not in the list of predefined parameters, raise an error and ask the user to try again.
    
    3) If the user input is valid, create a copy of the dataframe containing only the columns corresponding to the selected parameter.
    
    4) Add a 'Timestamp' column to the resulting dataframe with the corresponding timestamps.
    
    5) Return the resulting dataframe.
    """
    params = ['Voc', 'Isc', 'FF', 'Vmpp', 'Impp', 'MPP',
              'Irradiace', 'irradiance_yield', 'irradiation',
              'temp','rain', 'ambient_temperature','wind_direction', 
              'wind_speed']
    print(params)

    while True:
        try:
            param = input('Choose a parameter from the list:')
            if param not in params:
                raise ValueError('Parameter not in list')
            break
        except ValueError as e:
            print(e)
            print('Try again')
    
    df_sc =df[[i for i in df.columns if param in i]].copy()
    df_sc.insert(0,'Timestamp',df.iloc[:,0])

    return df_sc


def compareSCmodules(df):
    """
    This function allows the user to select a parameter from a list of predefined parameters, filter the data by a specified time range, and plot the resulting data for all available solar panel modules.

    Input:
    A pandas dataframe containing the data to be filtered by parameter and time range.

    Output:
    A plot comparing the selected parameter for all available solar panel modules over the specified time range.
    
    Steps:
    1) Call the getSCparam function to select a parameter from a list of predefined parameters and return a dataframe containing only the columns corresponding to the selected parameter.
    
    2)Call the date_slicer function to filter the data by a specified time range.
    
    3) Plot the resulting data for all available solar panel modules over the specified time range.
    """
    
    df = getSCparam(df)
    df = date_slicer(df)
    df.plot(x='Timestamp', y=df.columns[1:].tolist(), figsize=(10,8))