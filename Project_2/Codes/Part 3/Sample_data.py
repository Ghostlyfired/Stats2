import pandas as pd

# Load the dataset
df = pd.read_csv("StudentPerformanceFactors.csv")

# Filter, select, shuffle, and limit
filtered_df = df[df['Parental_Education_Level'] != ""]
selected_df = filtered_df[['Parental_Education_Level', 'Exam_Score']]
shuffled_df = selected_df.sample(frac=1, random_state=42)
final_df = shuffled_df.head(1000)

# Save to CSV
final_df.to_csv("filtered_student_data.csv", index=False)

# Optional: Save to Excel
# final_df.to_excel("filtered_student_data.xlsx", index=False)

# Optional: Save to JSON
# final_df.to_json("filtered_student_data.json", orient="records", lines=True)
