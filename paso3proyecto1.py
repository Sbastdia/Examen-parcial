from paso2proyecto1 import separarUrl, separarUrlColumnaDDF, sacarunaURL
import pandas as pd
conversiones=pd.read_csv("conversiones.csv", sep=";")
navegacion=pd.read_csv("navegacion.csv", sep=";")

nav=pd.DataFrame(navegacion)
conv=pd.DataFrame(conversiones)

#para identificar si hay elementos repetidos
def identificarRepetidos (DataFrame):

    for i in range (0,len(DataFrame)):
        if(DataFrame.iloc[i]["id_user"]!= ''):
            DataFrame= DataFrame.duplicated(DataFrame.columns[~DataFrame.columns.isin(['id_user'])])
        elif(DataFrame.iloc[i]["gclid"]!= ''):
            DataFrame= DataFrame.duplicated(DataFrame.columns[~DataFrame.columns.isin(['gclid'])])
        else:
            DataFrame= DataFrame.duplicated(DataFrame.columns[~DataFrame.columns.isin(['url_landing'])])

    DataFrame.sort_values(by='ts', ignore_index= True)
    return DataFrame

def eliminarRepetidos (DataFrame):

    for i in range (0, len(DataFrame)):
        if(DataFrame.iloc[i]["id_user"]!= ''):
            DataFrame = DataFrame.drop_duplicates(DataFrame.columns[~DataFrame.columns.isin(['id_user'])])
        elif(DataFrame.iloc[i]["gclid"]!= ''):
            DataFrame = DataFrame.drop_duplicates(DataFrame.columns[~DataFrame.columns.isin(['gclid'])])
        else:
            DataFrame = DataFrame.drop_duplicates(DataFrame.columns[~DataFrame.columns.isin(['url_landing'])])

    DataFrame.sort_values(by='ts', ignore_index= True)
    return DataFrame

nav.sort_values(by=["ts"], inplace=True)