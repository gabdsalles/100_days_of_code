"""import csv


with open('./Day 25 - CSV/weather_data.csv') as f:
    #data = f.readlines()
    #data = [i.strip() for i in data]
    #print(data)

    data = csv.reader(f)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures)"""

import pandas as pd

data = pd.read_csv('./Day 25 - CSV/weather_data.csv')
#print(data)

data_dict = data.to_dict()
#print(data_dict)

#Pegar informações das colunas
#print(data['temp'].mean())
#print(data.temp.max())

#Pegar informações das linhas
#print(data[data.temp == data.temp.max()]) #linha em que a temperatura é igual à temperatura máxima

#Pegar a temperatura de Monday e transformar pra fahrenheit
monday = data[data.day == 'Monday']
print(f"Celsius:{monday.temp[0]}")
monday_f = (1.8 * monday.temp[0]) + 32
print(f"Fahrenheit:{monday_f}")

# Criar um DataFrame do zero
data_dict = {
    "students": ['harry', 'ron', 'hermione'],
    "grades": [90, 100, 80]
}

df = pd.DataFrame(data_dict)
print(df)

