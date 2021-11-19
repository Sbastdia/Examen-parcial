from paso2proyecto1 import separarUrl, separarUrlColumnaDDF, sacarunaURL
import pandas as pd

#para identificar si hay elementos repetidos
def identificarRepetidos (DataFrame):

    for i in range (0,len(DataFrame)):
        DataFrame= DataFrame.duplicated(DataFrame.columns[~DataFrame.columns.isin(['id_user'])])

def eliminarRepetidos (DataFrame):

    for i in range (0, len(DataFrame)):
        DataFrame = DataFrame.drop_duplicates(DataFrame.columns[~DataFrame.columns.isin(['id_user'])])