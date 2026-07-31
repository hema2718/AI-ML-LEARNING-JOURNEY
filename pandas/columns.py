import pandas as pd

student = {
    "Name": ["Hema", "Rahul", "Priya"],
    "Branch": ["ISE", "CSE", "AIML"],
    "CGPA": [8.32, 8.75, 9.10]
}

df = pd.DataFrame(student)

print(df["Name"])
print(df["Branch"])
print(df["CGPA"])