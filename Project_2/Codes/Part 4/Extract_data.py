import pandas as pd
import numpy as np # for checking nan values

# Contains the original dataset from kaggle
df = pd.read_csv('data.csv')

# Function to compare the previous and final exam scores and check which is larger
def compare_scores(prev, final): 
    if pd.isna(prev) or pd.isna(final): # Checking those records in which one of previous or final marks are not specified 
                                        # Note that there are no null values in our particular dataset although for these attributes
        return np.nan
    return int(prev < final)

# Create a new attribute to store the improvement status, i.e. 1 if final > prev and 0 if final <= prev
df['Improved'] = df.apply(lambda row: compare_scores(row['Previous_Scores'], row['Exam_Score']), axis=1)
df.to_csv('modified_data.csv', index=False) # contains the original dataset along with the improvement status of students

df = pd.read_csv("modified_data.csv")
df_valid = df.dropna(subset=['Previous_Scores', 'Exam_Score', 'Improved']) # Ignore rows with null values before taking the sample

sampled_df = df_valid.sample(n=min(100, len(df_valid)), random_state=50) # Create a random sample of size 100 with seeding

# Maintain the necessary attributes in a separate excel file for better presentation
sampled_df = sampled_df[['Previous_Scores', 'Exam_Score', 'Improved']] 
sampled_df.to_excel("sample_data.xlsx", index=False) 

# Count the number of students who have not improved and who have improved respectively
count_0 = (sampled_df['Improved'] == 0).sum()
count_1 = (sampled_df['Improved'] == 1).sum()
total = count_0 + count_1

# Store the probability of success
prob_success = count_1 / total 

# Summarizing the results in a separate excel file
summary_df = pd.DataFrame ({
    'Labels': ['Failure', 'Success', 'Success prob.'],
    'Value': [count_0, count_1, prob_success]
})
summary_df.to_excel("summary.xlsx", index=False)
