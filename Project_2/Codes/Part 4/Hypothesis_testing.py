import pandas as pd
import math
from scipy.stats import norm

# Load summary.xlsx to retrieve the probability of success and number of successes which was computed in Extract_data.py
df = pd.read_excel("summary.xlsx")
prob_succ = float(df.iloc[2, 1])
succ = float(df.iloc[1, 1])

alpha = 0.05 # Level of significance
p0 = 0.5 # Probability under H0
n = 100 # Sample size

z_score = (succ - n * p0 - 0.5) / math.sqrt(n * p0 * (1 - p0)) # Apply continuity correction to the test statistic
# print(z_score)
p_value = 1 - norm.cdf(z_score) # Calculate p-value for the given one-sided test 

# Compare p-value and level of significance for final decision
if p_value <= alpha:
    print(f"We should reject the null hypothesis since the p_value {p_value:.6f} is less than or equal to the level of significance {alpha}")
else:
    print(f"We should accept the null hypothesis since the p_value {p_value:.6f} is greater than the level of significance {alpha}")
