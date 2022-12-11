
import csv

with open('./weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temps = []

    for row in data:
        print(row)
        temperature = row[1]
        if temperature.isnumeric():
            temps.append(int(temperature))

    print(temps)

## Now do the same thing with pandas

import pandas

data = pandas.read_csv('./weather_data.csv', header=0)
print(data['temp'])