import pandas as pd


# df = pd.DataFrame({"Neeraj": [50, 21], "bhaskar": [121, 131]}, index=['Maths', 'English'])
# print(df)

# s = pd.Series([1,2,3,4,5], index=['2015 sales in k', '2016 sales in k', '2017 sales in k', '2018 sales in k', '2019 sales in k'], name="sales report")
# print(s)

df = pd.read_csv("./cardio_train.csv")
print(df)