

threshold = 0.6
data = data[data.columns[data.isnull().mean() < threshold]]

data = data.loc[data.isnull().mean(axis=1) < threshold]
threshold = 0.6
data = data[data.columns[data.isnull().mean() < threshold]]

data = data.loc[data.isnull().mean(axis=1) < threshold]
print(data)