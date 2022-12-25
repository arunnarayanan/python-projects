
# import csv
#
# with open('./weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temps = []
#
#     for row in data:
#         print(row)
#         temperature = row[1]
#         if temperature.isnumeric():
#             temps.append(int(temperature))
#
#     print(temps)

## Now do the same thing with pandas

import pandas

data = pandas.read_csv('./weather_data.csv', header=0)

data_dict = data.to_dict()
print(data_dict)
print(f'Average temperature: {data["temp"].mean()}')
temp__max = data["temp"].max()
print(f'Max temperature: {temp__max}')
## Print the day the temp was maximum
print(f'Day with MAX temperature: {data[data["temp"] == temp__max]}')