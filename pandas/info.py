import pandas as pd

student = {
    "Name": ["Hema", "Rahul", "Priya", "Anjali"],
    "Branch": ["ISE", "CSE", "AIML", "ECE"],
    "CGPA": [8.32, 8.75, 9.10, 7.95]
}

df = pd.DataFrame(student)

df.info()