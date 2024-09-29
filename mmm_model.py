import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate larger media spend ($1.5M across channels over time)
np.random.seed(42)
n = 100  # Number of data points

# Simulate ad spends across multiple channels (TV, Radio, Digital)
tv_ad_spend = np.random.uniform(20000, 80000, n)   # Offline: TV
radio_ad_spend = np.random.uniform(10000, 30000, n)  # Offline: Radio
digital_ad_spend = np.random.uniform(40000, 100000, n)  # Online: Digital Ads

# Simulate conversions based on spends (target variable with some noise)
conversions = (
    0.35 * tv_ad_spend + 
    0.15 * radio_ad_spend + 
    0.50 * digital_ad_spend + 
    np.random.normal(0, 7000, n)
)

# Create a DataFrame
df = pd.DataFrame({
    'TV_Spend': tv_ad_spend,
    'Radio_Spend': radio_ad_spend,
    'Digital_Spend': digital_ad_spend,
    'Conversions': conversions
})

# Visualization: Pairplot of ad spends vs conversions
sns.pairplot(df)
plt.show()

# Marketing Mix Model: Linear Regression
X = df[['TV_Spend', 'Radio_Spend', 'Digital_Spend']]
y = df['Conversions']

# Add a constant (intercept)
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()

# Show the model summary
print(model.summary())

# Predict conversions
df['Predicted_Conversions'] = model.predict(X)

# Plot actual vs predicted conversions
plt.figure(figsize=(10, 6))
plt.scatter(df['Conversions'], df['Predicted_Conversions'], alpha=0.7)
plt.plot([df['Conversions'].min(), df['Conversions'].max()], [df['Conversions'].min(), df['Conversions'].max()], 'r--', lw=2)
plt.title('Actual vs Predicted Conversions')
plt.xlabel('Actual Conversions')
plt.ylabel('Predicted Conversions')
plt.show()

# Calculate the ROI for each channel
roi_tv = (model.params['TV_Spend'] / df['TV_Spend'].mean()) * 100
roi_radio = (model.params['Radio_Spend'] / df['Radio_Spend'].mean()) * 100
roi_digital = (model.params['Digital_Spend'] / df['Digital_Spend'].mean()) * 100

print(f"ROI for TV: {roi_tv:.2f}%")
print(f"ROI for Radio: {roi_radio:.2f}%")
print(f"ROI for Digital: {roi_digital:.2f}%")

# Analyze uplift from offline channels (TV + Radio)
offline_channels = df['TV_Spend'] + df['Radio_Spend']
offline_contrib = model.params['TV_Spend'] * df['TV_Spend'] + model.params['Radio_Spend'] * df['Radio_Spend']
offline_uplift = (offline_contrib / offline_channels.mean()) * 100
print(f"Offline Uplift (TV + Radio): {offline_uplift:.2f}%")

# Save results to CSV
df.to_csv('marketing_mix_results.csv', index=False)

# Example: Uplift analysis for a specific campaign scenario
campaign_tv_investment = 50000  # TV spend for a specific month
campaign_radio_investment = 20000  # Radio spend for a specific month
campaign_digital_investment = 80000  # Digital spend for a specific month

campaign_total_conversions = (
    model.params['TV_Spend'] * campaign_tv_investment +
    model.params['Radio_Spend'] * campaign_radio_investment +
    model.params['Digital_Spend'] * campaign_digital_investment
)
print(f"Estimated Conversions for the campaign: {campaign_total_conversions:.2f}")
