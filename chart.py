import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- 1. Setup & Styling ---
sns.set_theme(style="whitegrid")
sns.set_context("talk")

# --- 2. Generate Data (Long-Form) ---
# Best Practice: Create data in 'long' format (Database style), then pivot.
# Scenario: Customer Engagement by Day vs Hour
np.random.seed(42)
days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
hours_list = list(range(24))

data_records = []
for day in days_list:
    for hour in hours_list:
        # Business Logic: Higher engagement in evenings & weekends
        base_engagement = 20
        
        # Weekend boost
        if day in ['Sat', 'Sun']:
            base_engagement += 30
            
        # Time of day patterns
        if 18 <= hour <= 23:   # Evening peak
            time_factor = 40
        elif 9 <= hour <= 17:  # Work hours
            time_factor = 15
        else:                  # Late night
            time_factor = 0
            
        # Add randomness
        noise = np.random.randint(-10, 10)
        score = max(0, base_engagement + time_factor + noise)
        
        data_records.append({
            'Day': day,
            'Hour': hour,
            'Engagement Score': score
        })

df_long = pd.DataFrame(data_records)

# --- 3. Data Transformation ---
# Pivot the data for Heatmap (Rows=Day, Cols=Hour, Values=Score)
heatmap_data = df_long.pivot(index="Day", columns="Hour", values="Engagement Score")

# Reorder index to ensure Mon-Sun order
heatmap_data = heatmap_data.reindex(days_list)

# --- 4. Create Visualization ---
# Requirement: 512x512 output -> 8 inches * 64 DPI
plt.figure(figsize=(8, 8))

# Generate Heatmap
# Using 'fmt' and 'annot' makes it clearer this is a heatmap
ax = sns.heatmap(heatmap_data, cmap="coolwarm", linewidths=.5, 
                 cbar_kws={'label': 'Engagement Level'})

# --- 5. Professional Styling ---
plt.title('Customer Engagement Heatmap', fontsize=18, pad=20)
plt.xlabel('Hour of Day', fontsize=14)
plt.ylabel('Day of Week', fontsize=14)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(rotation=0, fontsize=12)

# Use tight_layout to ensure labels fit within the 512x512 box
plt.tight_layout()

# --- 6. Save Chart ---
# Validating strict 512x512 dimensions.
# Note: We omit bbox_inches='tight' as it alters dimensions.
plt.savefig('chart.png', dpi=64)

print("Chart generated successfully: chart.png (512x512)")