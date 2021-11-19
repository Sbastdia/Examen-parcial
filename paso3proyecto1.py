from paso2proyecto1 import separarUrl, separarUrlColumnaDDF, sacarunaURL
import pandas as pd

#para identificar si hay elementos repetidos
def identificarRepetidos (DataFrame):

    for i in range (0,len(DataFrame)):
        if(DataFrame.iloc[i]["id_user"]!= ''):
            DataFrame= DataFrame.duplicated(DataFrame.columns[~DataFrame.columns.isin(['id_user'])])
        elif(DataFrame.iloc[i]["gclid"]!= ''):
            DataFrame= DataFrame.duplicated(DataFrame.columns[~DataFrame.columns.isin(['gclid'])])
        else:
            DataFrame= DataFrame.duplicated(DataFrame.columns[~DataFrame.columns.isin(['url_landing'])])

def eliminarRepetidos (DataFrame):

    for i in range (0, len(DataFrame)):
        if(DataFrame.iloc[i]["id_user"]!= ''):
            DataFrame = DataFrame.drop_duplicates(DataFrame.columns[~DataFrame.columns.isin(['id_user'])])
        elif(DataFrame.iloc[i]["gclid"]!= ''):
            DataFrame = DataFrame.drop_duplicates(DataFrame.columns[~DataFrame.columns.isin(['gclid'])])
        else:
            DataFrame = DataFrame.drop_duplicates(DataFrame.columns[~DataFrame.columns.isin(['url_landing'])])
