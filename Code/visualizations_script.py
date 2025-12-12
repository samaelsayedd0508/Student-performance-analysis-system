# Auto-generated visualization script
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("/mnt/data/students.db")
df_student = pd.read_sql_query("SELECT * FROM Student;", conn)
df_subject = pd.read_sql_query("SELECT * FROM Subject;", conn)
df_assess = pd.read_sql_query("SELECT * FROM Assessment;", conn)

df = df_assess.merge(df_student, left_on='Student_ID', right_on='Student_ID', how='left')
df = df.merge(df_subject, left_on='Subject_ID', right_on='Subject_ID', how='left')
df['Score'] = pd.to_numeric(df['Score'], errors='coerce')

# Average Score per Subject
avg_sub = df.groupby('Subject_name', as_index=False)['Score'].mean().sort_values('Score', ascending=False)
plt.figure(figsize=(8,5))
plt.bar(avg_sub['Subject_name'], avg_sub['Score'])
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.title("Average Score per Subject")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("avg_score_per_subject.png")
plt.close()

# Score Distribution
plt.figure(figsize=(8,5))
plt.hist(df['Score'].dropna(), bins=15)
plt.xlabel("Score")
plt.ylabel("Count")
plt.title("Score Distribution (All Assessments)")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.close()

# Attendance Counts
attendance_counts = df['Attendance'].fillna("Unknown").value_counts().reset_index()
attendance_counts.columns = ['Attendance', 'Count']
plt.figure(figsize=(6,4))
plt.bar(attendance_counts['Attendance'], attendance_counts['Count'])
plt.xlabel("Attendance Status")
plt.ylabel("Count")
plt.title("Attendance Counts")
plt.tight_layout()
plt.savefig("attendance_counts.png")
plt.close()

# Average Score per Level (if exists)
if 'Level' in df.columns:
    avg_level = df.groupby('Level', as_index=False)['Score'].mean().sort_values('Score', ascending=False)
    plt.figure(figsize=(7,5))
    plt.bar(avg_level['Level'], avg_level['Score'])
    plt.xlabel("Level")
    plt.ylabel("Average Score")
    plt.title("Average Score per Level")
    plt.tight_layout()
    plt.savefig("avg_score_per_level.png")
    plt.close()

# Top Students by Average Score
top_students = df.groupby(['Student_ID','Student_name'], as_index=False)['Score'].mean().sort_values('Score', ascending=False).head(10)
plt.figure(figsize=(8,6))
plt.barh(top_students['Student_name'][::-1], top_students['Score'][::-1])
plt.xlabel("Average Score")
plt.title("Top 10 Students by Average Score")
plt.tight_layout()
plt.savefig("top_students.png")
plt.close()

# Boxplot by Subject
plt.figure(figsize=(8,6))
df.boxplot(column='Score', by='Subject_name', rot=45)
plt.suptitle("")
plt.title("Score Distribution by Subject")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("boxplot_by_subject.png")
plt.close()
