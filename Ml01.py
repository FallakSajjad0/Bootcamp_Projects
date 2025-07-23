import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

# self provided data
data = {"Names": ['Fallak', 'Ahmad', 'Ali'], 
        "RollNo": [1122, 1023, 1524]
        }

df = pd.DataFrame(data)

# ploting graph of data

df.plot(x= "Names", y= "RollNo", kind= "bar", color="Black")
plt.title("Name and RollNO")
plt.xlabel("Names")
plt.ylabel("RollNo")
plt.show()

# loading data

iris = load_iris()

x = iris.data[:, :2]
y = iris.target

# ploting loaded data

plt.figure(figsize= (8, 6))
for species in range(3):
    plt.scatter(x[y== species, 0], x[y == species, 1], label = iris.target_names [species])

plt.xlabel('Sepal Length(cm)')
plt.ylabel('Sepal Width(cm)')
plt.title('Irise dataset - Sepal Features')
plt.legend()
plt.show()


