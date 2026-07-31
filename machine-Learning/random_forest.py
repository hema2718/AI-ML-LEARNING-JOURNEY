from sklearn.ensemble import RandomForestClassifier

X = [[25], [35], [45], [55]]
y = ["No", "No", "Yes", "Yes"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

prediction = model.predict([[40]])

print("Loan Approved:", prediction[0])