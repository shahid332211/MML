import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

height = np.array([150, 155, 160, 165, 170, 175]).reshape(-1, 1)
weight = np.array([45, 50, 55, 60, 65, 70])

model = LinearRegression()
model.fit(height, weight)

height_new = np.array([154, 163]).reshape(-1, 1)
predicted_weight = model.predict(height_new)
slope = model.coef_[0]
intercept = model.intercept_

print(f"slope (M): {slope}")
print(f"intercept (C): {intercept}" )

for i, h in enumerate(height_new):
    print(f"predicted weight for height{height_new[i][0]}: {predicted_weight[i]} ")

plt.scatter(weight, height, color= 'blue', label= 'Actual data')
plt.plot(model.predict(height), height, color='red', label= 'linear regression line')
plt.scatter(predicted_weight, height_new, color= 'green', label= 'Predicted data')

plt.xlabel('weight')
plt.ylabel('height')
plt.legend
plt.title('linear regression: height vs weight')

plt.show()