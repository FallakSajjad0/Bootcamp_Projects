# Importes Libreries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = pd.read_csv("Boston1.csv")

# df_1feet = data[['LSTAT', 'MEDV']]
# print(df_1feet)

# ploting graph

data.plot(x= "LSTAT", y = "MEDV", style= '.')
plt.xlabel("Lstat ")
plt.ylabel("Medv")
plt.show()

# spliting into train and test

X = pd.DataFrame(data.iloc[:,:-1])
y = pd.DataFrame(data.iloc[:,-1])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"X_train SHape is {X_train.shape}")
print(f"y_train SHape is {y_train.shape}")
print("-"*30)
print(f"X_test SHape is {X_test.shape}")
print(f"y_test SHape is {y_test.shape}")

# creating Models

model = LinearRegression()
print(model)

model.fit(X_train, y_train)

print(model.coef_)
print(model.intercept_)

# Predictions 

y_pred = model.predict(X_test)
y_pred = pd.DataFrame(y_pred, columns= ['Predicted'])

print(y_pred)

# Calculating Errors

print(f"MAE : {metrics.mean_absolute_error(y_test, y_pred)}")
print(f"MsE : {metrics.mean_squared_error(y_test, y_pred)}")
print(f"RMSE : {metrics.root_mean_squared_error(y_test, y_pred)}")
print(f"RSquared : {metrics.r2_score(y_test, y_pred)}")
