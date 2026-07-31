from sklearn.tree import DecisionTreeClassifier

X = [[25], [35], [45], [55]]
y = ["No", "No", "Yes", "Yes"]

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict([[40]])

print("Loan Approved:", prediction[0])