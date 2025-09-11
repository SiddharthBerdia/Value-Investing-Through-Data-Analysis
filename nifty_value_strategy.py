
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter

PORTFOLIO_SIZE = 100000
CSV_FILE = 'nifty500_fundamentals_cleaned.csv'

# Load cleaned CSV
df = pd.read_csv(CSV_FILE)

# Calculate percentiles for each value metric
metrics = ['p_e_ratio', 'p_b_ratio', 'p_s_ratio', 'ev_ebitda', 'ev_gp']
for metric in metrics:
    df[metric + '_percentile'] = df[metric].rank(pct=True, ascending=True)

# Calculate Robust Value Score (RV Score)
df['rv_score'] = df[[m + '_percentile' for m in metrics]].mean(axis=1)

# Select top 50 stocks by RV score
df_top = df.sort_values('rv_score').head(50).copy()

# Calculate number of shares to buy per stock (equal allocation)
position_size = PORTFOLIO_SIZE / len(df_top)
df_top['share_price'] = np.random.uniform(100, 2000, size=len(df_top))  # Dummy prices for simulation
df_top['shares_to_buy'] = (position_size // df_top['share_price']).astype(int)

# Simulate returns (% gain/loss) per timeframe
timeframes = ['1m_return', '3m_return', '6m_return', '1y_return']
for tf in timeframes:
    df_top[tf] = np.random.uniform(-0.1, 0.3, size=len(df_top))  # Dummy returns between -10% and +30%

# Calculate portfolio returns (Equal Weight)
equal_weight_returns = {}
for tf in timeframes:
    equal_weight_returns[tf] = (df_top[tf].mean()) * 100

# Calculate portfolio returns (80-20 strategy)
df_top_sorted = df_top.sort_values('rv_score')
top_20_pct_count = int(0.2 * len(df_top_sorted))
top_20_df = df_top_sorted.head(top_20_pct_count)
rest_df = df_top_sorted.tail(len(df_top_sorted) - top_20_pct_count)

returns_80_20 = {}
for tf in timeframes:
    top_return = top_20_df[tf].mean() * 0.8
    rest_return = rest_df[tf].mean() * 0.2
    returns_80_20[tf] = (top_return + rest_return) * 100

# Save to Excel
excel_file = 'value_strategy_results.xlsx'
writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df_top.to_excel(writer, sheet_name='Top 50 Value Stocks', index=False)
writer.close()

# Plot comparison graph
labels = ['1M', '3M', '6M', '1Y']
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, [equal_weight_returns[k] for k in timeframes], width, label='Equal Weight')
rects2 = ax.bar(x + width/2, [returns_80_20[k] for k in timeframes], width, label='80-20 Strategy')

ax.set_ylabel('Portfolio Return (%)')
ax.set_title('Return Comparison by Strategy')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.tight_layout()
plt.savefig('strategy_comparison.png')
plt.show()
