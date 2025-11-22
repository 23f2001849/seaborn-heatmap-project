import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    # 1. Setup & Styling
    # Use a clean, professional style
    sns.set_style("whitegrid")
    sns.set_context("talk") # "talk" context makes labels readable at 512x512

    # 2. Generate Realistic Synthetic Data
    # Context: Customer Engagement Metrics for Retail Client
    np.random.seed(42)
    n_customers = 200

    # Create base variables with realistic relationships
    # Metric 1: Time on App (minutes)
    time_on_app = np.random.normal(loc=15, scale=5, size=n_customers)
    
    # Metric 2: Pages Visited (correlated with Time)
    pages_visited = (time_on_app * 0.8) + np.random.normal(0, 2, n_customers)
    
    # Metric 3: Purchase Value (correlated with Pages and Time)
    purchase_value = (pages_visited * 5) + (time_on_app * 2) + np.random.normal(0, 10, n_customers)
    
    # Metric 4: Support Tickets (negative correlation with Satisfaction)
    support_tickets = np.random.poisson(lam=1, size=n_customers)
    
    # Metric 5: Cust. Satisfaction (negative with Support, positive with Value)
    satisfaction = 10 - (support_tickets * 2) + (purchase_value * 0.01) + np.random.normal(0, 1, n_customers)
    
    # Clip values to realistic ranges
    time_on_app = np.maximum(time_on_app, 1)
    pages_visited = np.maximum(pages_visited, 1)
    purchase_value = np.maximum(purchase_value, 0)
    satisfaction = np.clip(satisfaction, 1, 10)

    # Create DataFrame
    df = pd.DataFrame({
        'Time on App': time_on_app,
        'Pages Visited': pages_visited,
        'Purchase Value': purchase_value,
        'Support Tickets': support_tickets,
        'Satisfaction': satisfaction
    })

    # 3. Calculate Correlation Matrix
    # This is the key step for this specific task type
    corr_matrix = df.corr()

    # 4. Create Heatmap
    # Requirement: 512x512 pixels -> 8 inches * 64 DPI
    plt.figure(figsize=(8, 8))
    
    # Generate the Seaborn heatmap
    # annot=True adds the numbers, fmt=".2f" formats them
    # cmap='coolwarm' is standard for correlation (Red=Pos, Blue=Neg)
    # vmin=-1, vmax=1 ensures the color scale is correct for correlations
    ax = sns.heatmap(corr_matrix, 
                     annot=True, 
                     fmt=".2f", 
                     cmap='coolwarm', 
                     vmin=-1, vmax=1, 
                     square=True,
                     cbar_kws={"shrink": .8})

    # 5. Professional Styling
    plt.title('Customer Engagement Correlation Matrix', fontsize=16, pad=20)
    
    # Rotate labels for readability
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(rotation=0, fontsize=10)

    # Use tight_layout to fit labels INSIDE the figure without changing image size
    plt.tight_layout()

    # 6. Save Chart
    # Saving strictly as 512x512 pixels
    plt.savefig('chart.png', dpi=64)
    print("Success: Generated 'chart.png' (512x512 pixels)")

if __name__ == "__main__":
    main()