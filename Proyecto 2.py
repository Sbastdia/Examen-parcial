import pandas as pd
conversiones=pd.read_csv("conversiones.csv", sep=";")
navegacion=pd.read_csv("navegacion.csv", sep=";")

nav=pd.DataFrame(navegacion)
conv=pd.DataFrame(conversiones)
#Ejercicio 2
freq = conv["lead_type"].value_counts()
print(freq)

#Ejercicio 3
rec= union["user_recurrent"].value_counts(normalize=True)
print(rec)

#Ejercicio 4
def SacarCoche(URL):
    URL_parts=URL.split("&")
    URL_PARTS=URL_parts[0].split("/gclid")
    car=URL_PARTS[0].split("es/")[1]
    return car

url="https://www.metropolis.com/es/ixs-electrico/gclid=Cj0KCQjw1dGJBhD4ARIsANb6OdmYnQIBLDemeVg6nbOtVVlqgU02Z3FgfQEefr98pUEyPdUTCj-CQWAaAlhyEALw_wcB&idUser=5fcc8b47-8fa0-4791-a6b8-6260f2ab0888&uuid=2ae80a9e-4a1d-495f-bfc7-24a2ee462cda&camp=1646697023&adg=61477462725&device=c&sl=&adv=379120564696&rec=false&"
print(SacarCoche(url))