import matplotlib.pyplot as plt

marks = [35, 45, 55, 65, 75, 85, 95, 60, 70, 80]

plt.hist(marks, bins=5)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()