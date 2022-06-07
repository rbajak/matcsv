from cProfile import label
from datetime import datetime
import glob
import os
from textwrap import indent 
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter
import datetime

def GetCityName(files):
    dict = {}
    for f in files:
        basename = os.path.basename(f)
        name = basename.split('.')[0]
        dict.update({name: f})
    return dict


csvs = glob.glob('.\dane\*')
dict = GetCityName(csvs)

while True:
    print("Wybierz miasto:")
    for key, value in dict.items() :
        print ("  " + key)
    city = input("> ")
    if city in dict:
        break
    else:
        print("Takie miasto jak " + city + " nie istnieje. Spróbuj jeszcze raz.")

columns = ["N", "M", "D", "H", "DBT"]
df = pd.read_csv(dict[city], skiprows=[0], usecols=columns, delim_whitespace=True)

dict2 = {}
for i, a in df.iterrows():
    time = datetime.datetime(2022, int(a['M']), int(a['D']), int(a['H']), 0)
    dict2.update({time: a['DBT']})

df=pd.DataFrame({'N': dict2.keys(), 'DBT': dict2.values()})

fig, ax = plt.subplots(figsize=(12, 12))
ax.plot(df.N, df.DBT, label=city)
date_form = DateFormatter("%m-%d %H:00")
ax.xaxis.set_major_formatter(date_form)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.xlabel('Czas')
plt.ylabel('Temperatura')
plt.legend()
plt.title('Średnia temperatura na daną godzinię i dzień w roku.')
plt.show()