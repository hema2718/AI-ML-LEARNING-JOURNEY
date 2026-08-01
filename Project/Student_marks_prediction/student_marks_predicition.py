import pandas as pd
import mathplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data=pd.read_csv("Student_marks.csv")
x=data[["Hours"]]
y=data["Marks"]
model=LinearRegression()
model.fit(x,y)
hours=float(input("Enter study hours: "))
prediction=model.predict([[hours]])
print(f"Predicted Marks : {prediction[0]:.2f}")
plt.scatter(x,y,color="blue",label="Actual Data")
plt.plot(x,model.predict(x),color="red",label="Regression Line")
plt.title("Student Marks prediction")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()
