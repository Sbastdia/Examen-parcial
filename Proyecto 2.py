import pandas as pd


conversiones=pd.read_csv("conversiones.csv", sep=";")
navegacion=pd.read_csv("navegacion.csv", sep=";")

nav=pd.DataFrame(navegacion)
conv=pd.DataFrame(conversiones)

#Ejercicio 1
#nav.dropna(subset=["url_landing"], inplace=True)
print("Ejercicio 1")
nav["Convertido"]=0
conv["Convertido"]=1
numeroVisitas=nav.shape[0]
print("El número de visitas es",numeroVisitas)
#union= juntarTablas(nav, conv)
numeronoconvertidos=len(nav["Convertido"])
numeroconvertidos=len(conv["Convertido"])
numerototal=numeronoconvertidos+numeroconvertidos
print("no convertidos",numeronoconvertidos)
print("convertidos", numeroconvertidos)
print("El porcentaje de convertidos:",(numeroconvertidos/numerototal *100))
rec= nav["Convertido"].value_counts(normalize=True)
print(rec)
#Ejercicio 2
print("Ejercicio 2")
freq = conv["lead_type"].value_counts()
print(freq)

#Ejercicio 3
print("Ejercicio 3")
rec2= nav["user_recurrent"].value_counts(normalize=True)
print(rec2)

#Ejercicio 4
print("Ejercicio 4")
def SacarCoche(URL):
    URL_parts=URL.split("=")
    URL_PARTS=URL_parts[0].split("/")
    if(URL_PARTS[-2]!="es"):
        car=URL_PARTS[-2]
    else:
        car=""
    return car

def contarCoches(Dataframe):
    Coches=pd.DataFrame(columns=["Coches"])
    for i in range (0,len(Dataframe)):
        coche=SacarCoche(Dataframe.iloc[i]["url_landing"])
        if(coche!=""):
            Coches=Coches.append({'Coches':coche}, ignore_index=True)
    return Coches

nav.dropna(subset=["url_landing"], inplace=True)
nav2=nav.loc[0:10]
Coches=contarCoches(nav)
freqcoche=Coches.value_counts()
print(freqcoche)
# url2=nav.iloc[1]["url_landing"]
# print(url2)
# url="https://www.metropolis.com/es/ixs-electrico/gclid=Cj0KCQjw1dGJBhD4ARIsANb6OdmYnQIBLDemeVg6nbOtVVlqgU02Z3FgfQEefr98pUEyPdUTCj-CQWAaAlhyEALw_wcB&idUser=5fcc8b47-8fa0-4791-a6b8-6260f2ab0888&uuid=2ae80a9e-4a1d-495f-bfc7-24a2ee462cda&camp=1646697023&adg=61477462725&device=c&sl=&adv=379120564696&rec=false&"
# print(type(SacarCoche(url)))