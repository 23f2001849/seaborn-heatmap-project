import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    # 1. Set Professional Styling
    # Using a clean theme and scaling font for presentation
    sns.set_theme(style="whitegrid")
    sns.set_context("talk")

    # 2. Generate Realistic Synthetic Data
    # Scenario: Customer Engagement Score by Day of Week vs Hour of Day
    np.random.seed(42) # Ensure reproducibility
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    hours = [f"{h:02d}:00" for h in range(24)]
    
    # Create synthetic data matrix (7 days x 24 hours)
    # Logic: Higher engagement in evenings (18-22h) and weekends
    data = np.zeros((7, 24))
    
    for i, day in enumerate(days):
        # Base engagement higher on weekends (Fri-Sun)
        base_activity = 40 if i >= 4 else 20
        
        for j in range(24):
            # Peak hours pattern (Evening spike)
            if 18 <= j <= 22:
                time_factor = 35
            elif 9 <= j <= 17:
                time_factor = 15
            else:
                time_factor = 5
                
            # Add some random noise for realism
            noise = np.random.randint(-5, 10)
            data[i, j] = base_activity + time_factor + noise
            
            # Ensure no negative scores
            data[i, j] = max(0, data[i, j])

    # Convert to DataFrame for Seaborn
    df = pd.DataFrame(data, index=days, columns=hours)

    # 3. Create the Heatmap
    # Figure Size: 8 inches * 64 DPI = 512 pixels
    plt.figure(figsize=(8, 8))
    
    # Create heatmap with 'YlGnBu' (Yellow-Green-Blue) professional palette
    ax = sns.heatmap(df, cmap='YlGnBu', 
                     cbar_kws={'label': 'Engagement Score'},
                     linewidths=0.5, linecolor='white')

    # 4. Style the Chart
    plt.title('Customer Engagement Heatmap', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Hour of Day', fontsize=12, labelpad=10)
    plt.ylabel('Day of Week', fontsize=12, labelpad=10)
    
    # Rotate x-axis labels to prevent overlap
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.yticks(rotation=0, fontsize=10)

    # Use tight_layout to arrange elements neatly within the figure
    plt.tight_layout()

    # 5. Export Chart
    # Requirement: Exactly 512x512 pixels.
    # Note: We intentionally OMIT bbox_inches='tight' because it clips the image 
    # and alters the strict 512x512 dimensions required for validation.
    plt.savefig('chart.png', dpi=64)
    print("Success: Generated 'chart.png' with dimensions 512x512 pixels.")

if __name__ == "__main__":
    main()
