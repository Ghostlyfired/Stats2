import numpy as np
import matplotlib.pyplot as plt
from scipy.special import psi
from scipy.stats import gamma
import pandas as pd

# Load data and calculate rhs
data = pd.read_csv('Final Data1.csv')
sampled_data = data['Volume (in Million)'].sample(frac=0.2, random_state=42)
# sampled_data = sampled_data[sampled_data > 0]  # Remove zeros or negatives

mean_x = sampled_data.mean()
log_mean_x = np.log(sampled_data).mean()

rhs = log_mean_x - np.log(mean_x) 

# Define the function to find root of
def g(alpha):
    return psi(alpha) - np.log(alpha) - rhs

# Full-range plot
alpha_vals_full = np.linspace(0.1, 10, 1000)
g_vals_full = g(alpha_vals_full)

plt.figure(figsize=(12, 5))

# --- Subplot 1: Full view ---
plt.subplot(1, 2, 1)
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.plot(alpha_vals_full, g_vals_full, label='g(α) = ψ(α) - log(α) - rhs', color='blue')
plt.title('Full Range: g(α) from α = 0.1 to 10')
plt.xlabel('α (alpha)')
plt.ylabel('g(α)')
plt.grid(True)
plt.legend()

# --- Subplot 2: Zoomed view ---
alpha_vals_zoom = np.linspace(2.0, 2.1, 1000)
g_vals_zoom = g(alpha_vals_zoom)

plt.subplot(1, 2, 2)
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.plot(alpha_vals_zoom, g_vals_zoom, label='Zoomed g(α)', color='green')
plt.title('Zoomed In: g(α) from α = 2.0 to 2.1')
plt.xlabel('α (alpha)')
plt.ylabel('g(α)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('gamma_mle_full_and_zoomed.png', dpi=300)
plt.show()



# Take the estimated value of alpha from the user
alpha_est = float(input("Enter the estimated alpha value: "))
beta_est = mean_x / alpha_est  # scale

# Plot histogram and overlay Gamma PDF
plt.figure()
plt.hist(sampled_data, bins=30, density=True, alpha=0.5, label='Sample Data')
x_vals = np.linspace(sampled_data.min(), sampled_data.max(), 1000)
plt.plot(x_vals, gamma.pdf(x_vals, alpha_est, scale=beta_est),'r-', label=f'Gamma(α={alpha_est:.2f}, β={beta_est:.2f})')
plt.title('Histogram and Fitted Gamma Distribution')
plt.xlabel('Volume (in Million)')
plt.ylabel('Density')
plt.legend()
plt.savefig('gamma_mle_hist.png', dpi=300)
plt.show()