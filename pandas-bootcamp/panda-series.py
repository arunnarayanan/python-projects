
import pandas as pd
import numpy as np

my_series = pd.Series([10, 20, 30])
my_series.index = ['a', 'b', 'c'] # or pd.Series([10,20], index=['a', 'b'])

print(my_series)
print(f'Is Unique? {my_series.is_unique}')

names = ['Arun', 'Raji', 'Amri', 'Riya']
ages = [48, 45, 16, 13]
birth_loc = ['Namakkal', 'Devakottai', 'Dallas', 'Austin']
sports = ['Chess', 'Cooking', 'Dress', 'Dance']

family_dict = {"Name": names, "Age": ages, "Birth Location": birth_loc, "Sport": sports}

df = pd.DataFrame(family_dict)
print(df)
print('Dataframe dimensions: ', df.shape)

print(f'Name and Sport Report \n {df.loc[0:3, ["Name", "Sport"]]}')

df2 = pd.DataFrame(
    np.random.randint(10, size=(4,4)),
    index = ["a", "b", "c", "d"],
    columns = ["col_a", "col_b", "col_c", "col_d"]
)

print(df2)
print(f"Select two rows and two cols using loc: \n {df2.loc[['b', 'd'], ['col_a', 'col_c']]}")

staff_df = pd.read_csv('staff.csv')
staff_df["state"] = staff_df["city"].str.split(",", expand=True)[1].str.strip()
staff_df["state"].replace(
    {"TX": "Texas", "CA": "California"},
    inplace=True
)

# Salary > 65000
staff_df["salary_cleaned"] = staff_df["salary"].str[1:].str.replace(",","").astype("int")
print(f'Staff with salaries > 65,000 \n {staff_df.query("salary_cleaned > 65000")}')

# Staff age when hired
staff_df = staff_df.astype(
    {
        "date_of_birth": "datetime64[ns]",
        "start_date": "datetime64[ns]"
    }
)

print(staff_df.dtypes)


staff_df["age"] = (staff_df["start_date"] - staff_df["date_of_birth"]).dt.days / 365
staff_df["age"] = staff_df["age"].astype("int")
print(staff_df[["name", "age"]])

