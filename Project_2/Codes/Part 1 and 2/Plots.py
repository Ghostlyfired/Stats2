import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Ask user for parameters
alpha_mom = float(input("Enter alpha (MoM): "))
beta_mom = float(input("Enter beta (MoM): "))
alpha_mle = float(input("Enter alpha (MLE): "))
beta_mle = float(input("Enter beta (MLE): "))

# Load the dataset
data = pd.read_csv('Final Data1.csv')
sampled_data = data['Volume (in Million)'].sample(frac=0.2, random_state=42)

# Plot histogram of data
plt.figure(figsize=(8, 6))
count, bins, _ = plt.hist(sampled_data, bins=30, density=True, alpha=0.4, color='gray', label='Data Histogram')

# Prepare points for PDF curves
x_vals = np.linspace(sampled_data.min(), sampled_data.max(), 200)

# Plot Gamma PDFs for MoM and MLE
pdf_mom = gamma.pdf(x_vals, a=alpha_mom, scale=beta_mom)
pdf_mle = gamma.pdf(x_vals, a=alpha_mle, scale=beta_mle)

plt.plot(x_vals, pdf_mom, 'r-', label=f'Gamma (MoM) α={alpha_mom:.2f}, β={beta_mom:.2f}')
plt.plot(x_vals, pdf_mle, 'b--', label=f'Gamma (MLE) α={alpha_mle:.2f}, β={beta_mle:.2f}')

plt.title('Histogram with Gamma (MoM & MLE)')
plt.xlabel('Volume (in Million)')
plt.ylabel('Density')
plt.legend()
plt.savefig('gamma_mom_mle_hist.png', dpi=300)
plt.show()