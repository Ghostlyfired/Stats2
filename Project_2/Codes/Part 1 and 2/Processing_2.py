# Now we will be assuming that Xi belonging to our population follow normal distribution with unknown mean and variance
# We will be using the chi-distrbution to construct (alpha = 95%) confidence intervals for the Variance of a normal population
# We will be using the following formula to calculate the confidence interval for the variance of a normal population
# P(chi^2(alpha/2) < (n-1)s^2/sigma^2 < chi^2(1-alpha/2)) = 1-alpha with degree of freedom n-1
# here s^2 is the sample variance and n is the sample size
# We will start with randomly choosing a sample of size 20%of the popluation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Load the dataset
data = pd.read_csv('Final Data1.csv')

# Randomly sample 20% of the data
sampled_data = data['Volume (in Million)'].sample(frac=0.2, random_state=42)

# Calculate the sample size, and variance
n = len(sampled_data)
sample_variance = sampled_data.var(ddof=1)  # Unbiased variance (n-1 in denominator)

# Calculate the 95% confidence interval for the variance
alpha = 0.05
chi2_lower = chi2.ppf(1 - alpha / 2, df=n - 1)   # P(X < chi2_lower) = 1 - alpha/2
chi2_upper = chi2.ppf(alpha / 2, df=n - 1)       # P(X < chi2_upper) = alpha/2
variance_lower = (n - 1) * sample_variance / chi2_lower
variance_upper = (n - 1) * sample_variance / chi2_upper

print(f"95% Confidence Interval for Variance: ({variance_lower}, {variance_upper})")

# Note that here the definition of chi^2(alpha) is different then what we have used in our book.
# P(X < chi^2(alpha)) = alpha