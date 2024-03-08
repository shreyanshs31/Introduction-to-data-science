import pandas as pd

# mydataset = {
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings':[3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)
# print(myvar)

# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)

# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# myvar = pd.DataFrame(data)
# print(myvar.loc[0])
# print(myvar.loc[[0, 1]])

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df)

# df = pd.read_csv('baking_supplies.csv')
# print(df)

df = pd.read_csv('baking_supplies.csv')
# print(df.tail(3))
# print(df.info())

# new_df = df.dropna()
# print(new_df)

# df["Calories"].fillna(130, inplace = True)