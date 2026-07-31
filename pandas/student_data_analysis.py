import pandas as pd

student = {
    "Name": ["Hema", "Rahul", "Priya", "Anjali"],
    "Branch": ["ISE", "CSE", "AIML", "ECE"],
    "CGPA": [8.32, 8.75, 9.10, 7.95]
}

df = pd.DataFrame(student)

print("Highest CGPA:", df["CGPA"].max())
print("Lowest CGPA:", df["CGPA"].min())
print("Average CGPA:", df["CGPA"].mean())