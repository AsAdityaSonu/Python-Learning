# Q1 - Linear Regression from Scratch w/o sklearn
import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = sb.load_dataset('tips')
x = tips['total_bill'].values
y = tips['tip'].values

plt.scatter(x, y)
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Scatter Plot of Total Bill vs Tip")
plt.show()

mean_x = np.mean(x)
mean_y = np.mean(y)

slope = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
intercept = mean_y - slope * mean_x

y_pred = slope * x + intercept

residuals = y - y_pred

ss_total = np.sum((y - mean_y) ** 2)
ss_residual = np.sum(residuals ** 2)
r_squared = 1 - (ss_residual / ss_total)

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_squared)

plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Linear Regression of Total Bill vs Tip")
plt.show()

# Q2. Generate best fit line for trained dataset where the dataset is divided into 80% trained and 20% test dataset

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x_train, x_test, y_train, y_test = train_test_split(x.reshape(-1, 1), y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(x_train, y_train)

y_pred_test = model.predict(x_test)

plt.scatter(x_train, y_train)
plt.plot(x_train, model.predict(x_train), color='red')
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Best Fit Line for Training Data")
plt.show()

plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred_test, color='red')
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Best Fit Line for Testing Data")
plt.show()
