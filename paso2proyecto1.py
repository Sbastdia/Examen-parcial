import pandas as pd
from pandas.core.frame import DataFrame
conversiones=pd.read_csv("conversiones.csv", sep=";")
navegacion=pd.read_csv("navegacion.csv", sep=";")

nav=pd.DataFrame(navegacion)
conv=pd.DataFrame(conversiones)

#para eliminar los elementos que estén mal buscamos aquellos que no tengan sl(Site link) y los eliminamos
def separarUrl(URL,palabraclave):
    url_parts=URL.split("&")
    camp=0
    for part in url_parts:
        if "=" in part:
            key, value=part.split("=")
            #print(key,value)
            if key==palabraclave:
                camp=value
                break
    return camp

def sacarunaURL(Dataframe,i):
    url=""
    url=Dataframe.iloc[i]["url_landing"]
    return url

def separarUrlColumna(Dataframe,palabraclave):
    Campa=[]
    for i in range (0,len(Dataframe)):
        camp=separarUrl(sacarunaURL(Dataframe,i),palabraclave)
        #print(type(Campa))
        Campa.append(camp)
    return Campa

def separarUrlColumnaDDF(Dataframe,palabraclave):
    Campa=pd.DataFrame(columns=[palabraclave])
    for i in range (0,len(Dataframe)):
        camp=separarUrl(sacarunaURL(Dataframe,i),palabraclave)
        #print(type(Campa))
        Campa=Campa.append({palabraclave:camp}, ignore_index=True)
    return Campa
nav3=nav.loc[1:100]
#camp,adg, adv, sl
Campaña=separarUrlColumnaDDF(nav3,"camp")
adgroup=separarUrlColumnaDDF(nav3,"adg")
Campaf=nav3.assign(Campaña=Campaña["campaña"])
print(Campaf.head)