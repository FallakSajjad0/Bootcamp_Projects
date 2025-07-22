import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt


data3 = {"Names": ['Fallak', 'Ahmad', 'Ali'], 
        "RollNo": [1122, 1123, 1124]
        }


iris = load_iris()

x = iris.data[:, :2]
y = iris.target

print(iris.target_names)
print(data3.target_names)
plt.figure(figsize= (8, 6))
for species in range(3):
    plt.scatter(x[y== species, 0], x[y == species, 1], label = iris.target_names [species])

plt.xlabel('Sepal Length(cm)')
plt.ylabel('Sepal Width(cm)')
plt.title('Irise dataset - Sepal Features')
plt.legend()
# plt.show()

# df = pd.DataFrame(data2)
# df1 = pd.DataFrame(data3)
# grouped2 = df.groupby('Id')
# grouped = df1.groupby("Names").mean()
# print(grouped)
# print(grouped2)

# grouped2.plot(kind= 'bar', color = 'black')
# plt.title("Irise Graph")
# plt.xlabel("headers")
# plt.ylabel("data")
# plt.show()

# grouped.plot(kind= 'bar', color='blue')
# plt.title("Names&RollNo")
# plt.xlabel("Names")
# plt.ylabel("RollNo")

# plt.show()

