import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("iris.csv")
df = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(df)

df = pd.DataFrame({"names": ['Fallak', 'Ahmad', 'Ali'], 
                  "RollNo": [1122, 1123, 1124],
                  "city" : ['Havelian', 'Mansehra', 'Mansehra']})
print(df)

def fx(a):
    return a*a
df['sqrofsepllength'] = df['Sepallengthincm'].apply(fx)
df['zeros'] = [i for i in range(len(df))]

print(df.head())
print(df.info())

print(df.to_csv("irise2.csv", index=False))

a = np.array([84, 85 ,81, 89, 88, 86]
             )

b = np.array(['Hassan', 'Haider', 'Fallak', 'Ahmad', 'Ali']
            )

x_values = [1, 2, 3, 4, 6]
y_values = [6, 5, 8, 9, 10]
plt.plot(x_values, y_values, color = 'red')

plt.show()

