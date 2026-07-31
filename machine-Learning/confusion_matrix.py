from sklearn.metrics import confusion_matrix

actual = [1, 0, 1, 1, 0]
predicted = [1, 0, 1, 0, 0]

cm = confusion_matrix(actual, predicted)

print(cm)