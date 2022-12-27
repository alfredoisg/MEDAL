from ImportAlpha import change_column_names

def alf_loadData(path):

    "Imports data, changes names, and reduces memory usage!"

    df = pd.read_csv(path, encoding = "ISO-8859-1", sep=';', parse_dates=['Timestamp'], header = 0).iloc[::6]
    df = change_column_names(df)

    timedates=df.iloc[:,0]

    df=df.iloc[:,1:].astype('float32')
    df.insert(0,"Timestamp",timedates)

    return df




def slicer(df):

    aux_inpt=input('Enter start and end dates separated by semicolon space (YYYY-MM-DD; YYYY-MM-DD): ').split('; ')

    start_date,end_date = aux_inpt[0], aux_inpt[1]

    start_time = df[df['Timestamp'].astype(str).str.contains(start_date)].iloc[0].astype(str).iloc[0][-8:]
    end_time = df[df['Timestamp'].astype(str).str.contains(end_date)].iloc[-1].astype(str).iloc[0][-8:]

    df = df.set_index(['Timestamp'])



    aux=df.loc[str(start_date)+' '+start_time:str(end_date)+' '+end_time]
    aux.reset_index(inplace=True) 

    return aux




