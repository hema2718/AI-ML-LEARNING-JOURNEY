import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]
students = [45, 20, 15, 20]

plt.pie(students, labels=languages, autopct="%1.1f%%")

plt.title("Programming Language Preference")

plt.show()