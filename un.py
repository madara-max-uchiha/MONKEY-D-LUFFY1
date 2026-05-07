import pandas as py

data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = py.DataFrame(data, columns=['Names','Country','City'])
print(df.columns)
heights = df['Height']
print(heights)
print(df)
