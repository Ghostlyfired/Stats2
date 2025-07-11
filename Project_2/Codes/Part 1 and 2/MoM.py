# Assuming that our data follows a gamma distribution.
# let X ~ Gamma(α, β) be the random variable representing the volume of trades.
# The probability density function (PDF) of a gamma distribution is given by:
# f(x; α, β) = (1 / (β^α * Γ(α))) * x^(α - 1) * e^(-x / β) for x > 0
# The mean of the gamma distribution is given by:
# E[X] = α * β
# The variance of the gamma distribution is given by:
# Var[X] = α * β^2
# The moment-generating function (MGF) of the gamma distribution is given by:
# M_X(t) = (1 - βt)^(-α) for t < 1 / β



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Load the dataset
data = pd.read_csv('Final Data1.csv')

# Randomly sample 20% of the data
sampled_data = data['Volume (in Million)'].sample(frac=0.2, random_state=42)

# Calculate the first and second moments
m1 = sampled_data.mean()  # E(X)
m2 = (sampled_data**2).mean()  # E(X^2)

# Calculate β and α using the Method of Moments
beta_mom = (m2 - m1**2) / m1
alpha_mom = m1 / beta_mom

# Print the estimated parameters
print(f"Estimated Parameters using Method of Moments:\nAlpha (Shape): {alpha_mom}\nBeta (Scale): {beta_mom}")

# Plot histogram and the corresponding Gamma PDF
plt.figure(figsize=(8, 6))
count, bins, _ = plt.hist(sampled_data, bins=30, density=True, color='gray', alpha=0.4, label='Data Histogram')

x_vals = np.linspace(sampled_data.min(), sampled_data.max(), 200)
pdf_vals = gamma.pdf(x_vals, a=alpha_mom, scale=beta_mom)
plt.plot(x_vals, pdf_vals, 'r-', label=f'Gamma (MoM) α={alpha_mom:.2f}, β={beta_mom:.2f}')

plt.title('Histogram with Gamma Distribution (MoM)')
plt.xlabel('Volume (in Million)')
plt.ylabel('Density')
plt.legend()
plt.savefig('gamma_mom_hist.png', dpi=300)
plt.show()