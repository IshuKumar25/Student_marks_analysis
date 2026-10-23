import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\Pythonfiles\students.csv")

# Basic cleaning
df = df.drop_duplicates()
df = df.dropna()

subject_cols = ["Maths", "Python", "DBMS", "English"]
df[subject_cols] = df[subject_cols].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=subject_cols)

# Student-level calculations
df["Total"] = df[subject_cols].sum(axis=1)
df["Average"] = df["Total"] / len(subject_cols)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)
df["Status"] = df[subject_cols].ge(35).all(axis=1).map({True: "Pass", False: "Fail"})

# Subject-wise analysis
subject_summary = df[subject_cols].agg(["mean", "max", "min"]).T
print(subject_summary)

# Top 5 students
top_students = df.sort_values("Average", ascending=False).head(5)
print(top_students[["Name", "Average", "Grade"]])

# Grade distribution
print(df["Grade"].value_counts())

# Charts
plt.figure(figsize=(8, 5))
sns.barplot(x=subject_cols, y=df[subject_cols].mean().values)
plt.title("Average Marks by Subject")
plt.ylabel("Average Marks")
plt.show()

plt.figure(figsize=(6, 5))
df["Grade"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.ylabel("")
plt.show()

plt.figure(figsize=(7, 5))
sns.scatterplot(x="Attendance", y="Average", data=df)
plt.title("Attendance vs Average Marks")
plt.show()