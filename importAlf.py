import pandas as pd
import matplotlib.pyplot as plt
from ImportAlpha import change_column_names, input_from_array
import os

def alf_loadData(path):

    "Imports data, changes names, and reduces memory usage!"

    df = pd.read_csv(path, encoding = "ISO-8859-1", sep=';', parse_dates=['Timestamp'], header = 0).iloc[::6]
    df = change_column_names(df)

    timedates=df.iloc[:,0]

    df=df.iloc[:,1:].astype('float32')
    df.insert(0,"Timestamp",timedates)

    return df


## this is a commit comment

def alf_plotMPP(df):
    
    aux = input('Enter module name(s) separated by space comma (ex. MSXX, MSXX, MSXX): ').split(', ')
    string='MPP '
    moduleMPP=[string + i for i in aux]

    df_sliced=slicer(df) 
    df_sliced.plot(x = 'Timestamp', y = moduleMPP, figsize=(10,8))
    plt.legend(aux)


def slicer(df):

    aux_inpt=input('Enter start and end dates separated by semicolon space (YYYY-MM-DD; YYYY-MM-DD): ').split('; ')

    start_date,end_date = aux_inpt[0], aux_inpt[1]

    start_time = df[df['Timestamp'].astype(str).str.contains(start_date)].iloc[0].astype(str).iloc[0][-8:]
    end_time = df[df['Timestamp'].astype(str).str.contains(end_date)].iloc[-1].astype(str).iloc[0][-8:]

    df = df.set_index(['Timestamp'])



    aux=df.loc[str(start_date)+' '+start_time:str(end_date)+' '+end_time]
    aux.reset_index(inplace=True) 

    return aux



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
    df = df.T.drop_duplicates().T

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




# def alf_plotter(df):

#     numPlots = input('How namy plots?:')

#     numPlots = int(numPlots)

#     print(df.columns)

#     variables=input('Enter variables from the list separated by semicolon space: ').split('; ')

#     # start_date,end_date = aux_inpt[0], aux_inpt[1]

#     for i in range(numPlots):
#         df.plot(x='Timestamp', y=variables[i], figsize=(10,8))

#     # return variables



