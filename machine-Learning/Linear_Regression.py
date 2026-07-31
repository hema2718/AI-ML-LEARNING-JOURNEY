from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([20, 35, 50, 65, 80, 95])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[7]])

print("Predicted Marks:", prediction[0])