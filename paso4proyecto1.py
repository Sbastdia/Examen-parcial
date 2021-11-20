import pandas as pd
def juntarTablas(Dataframe1,Dataframe2):
    if "id_suite" in Dataframe1.columns() and "id_suite" in Dataframe2.columns():
        pd.merge(Dataframe1, Dataframe2, on='id_suite', how='outer')
    elif "gclid" in Dataframe1.columns() and "gclid" in Dataframe2.columns():
        pd.merge(Dataframe1, Dataframe2, on='gclid', how='outer')
    else:
        pd.merge(Dataframe1, Dataframe2, on='url_landing', how='outer')