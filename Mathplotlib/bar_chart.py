import matplotlib.pyplot as plt

subjects = ["Python", "NumPy", "Pandas", "ML"]
marks = [90, 85, 88, 92]

plt.bar(subjects, marks)

plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()