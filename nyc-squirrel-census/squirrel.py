
import pandas

data=pandas.read_csv('squirrel-data.csv')

print(f'Unique primary fur colors: {data["Primary Fur Color"].unique()}')
print(f'Unique fur color count: {data["Primary Fur Color"].nunique()}')
print(f'Value Counts: {data["Primary Fur Color"].value_counts()}')
# gray_count = 0
# cinnamon_count = 0
# black_count = 0
# other_count = 0

# for sq in data.values:
#     if sq[5] == 'Gray':
#         gray_count += 1
#     elif sq[5] == 'Cinnamon':
#         cinnamon_count += 1
#     elif sq[5] == 'Black':
#         black_count += 1
#     else:
#         other_count += 1
#
# print(f'Total Gray colored squirrels: {gray_count}')
# print(f'Total Cinnamon colored squirrels: {cinnamon_count}')
# print(f'Total Black colored squirrels: {black_count}')
# print(f'Total Nan colored squirrels: {other_count}')
#
# count_dict = {
#     "Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_count, cinnamon_count, black_count]
# }
#
# df = pandas.DataFrame(count_dict)
# df.to_csv('color-count.csv')

# Simpler approach using pandas
gray_count = len(data[data["Primary Fur Color"] == 'Gray'])
cinnamon_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_count = len(data[data["Primary Fur Color"] == 'Black'])

count_dict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(count_dict)
#df.to_csv('color-count.csv')

# How does the data look like?
squirrel_records = data.head(3)
print('Data samples \n', squirrel_records)
print(f'Data types in this data set: {data.dtypes}')

print(f'Columns: {list(data.columns)}')
data["Park ID"] = data["Park ID"].astype("float")
print(f'Data types in this data set (post-modification): {data.dtypes}')