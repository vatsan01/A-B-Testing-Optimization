# Import necessary libraries
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load dataset (replace 'experiment_data.csv' with actual dataset)
df = pd.read_csv('experiment_data.csv')

# Define Control and Treatment groups
control_group = df[df['group'] == 'control']['conversion_rate']
treatment_group = df[df['group'] == 'treatment']['conversion_rate']

# Perform T-test to evaluate statistical significance
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)
print(f"T-statistic: {t_stat:.2f}, P-value: {p_value:.5f}")

# Determine statistical significance
alpha = 0.05
if p_value < alpha:
    print("The result is statistically significant, Treatment performs better.")
else:
    print("No significant difference between Control and Treatment.")

# Visualizing results
plt.figure(figsize=(8, 5))
plt.hist(control_group, alpha=0.5, label="Control Group")
plt.hist(treatment_group, alpha=0.5, label="Treatment Group")
plt.xlabel("Conversion Rate")
plt.ylabel("Frequency")
plt.legend()
plt.title("A/B Test Results")
plt.show()
