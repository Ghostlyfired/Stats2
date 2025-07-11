import pandas as pd

# Load the dataset
df = pd.read_csv("Sample.csv")  # Replace with your actual file name

# Filter for "High School"
high_school_df = df[df['Parental_Education_Level'] == "High School"]

# Filter for NOT "High School"
not_high_school_df = df[df['Parental_Education_Level'] != "High School"]

# Function to calculate metrics
def get_exam_score_stats(df_subset):
    return {
        "Count": df_subset['Exam_Score'].count(),
        "Average": df_subset['Exam_Score'].mean(),
        "Variance": df_subset['Exam_Score'].var()
    }

# Get stats
high_school_stats = get_exam_score_stats(high_school_df)
not_high_school_stats = get_exam_score_stats(not_high_school_df)

# Display the results
print("📘 Stats for 'High School':")
print(high_school_stats)

print("\n📗 Stats for NOT 'High School':")
print(not_high_school_stats)
