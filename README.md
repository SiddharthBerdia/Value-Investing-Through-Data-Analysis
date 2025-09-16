# Value-Investing-Through-Data-Analysis
A Python-based framework for applying value investing principles through data analysis. The project combines financial data, portfolio construction, and web visualization to help identify undervalued stocks and compare investment strategies.

Project Overview :-

Implements Equal Weight and 80-20 Strategy portfolios.
Backtests returns across multiple horizons (1M, 3M, 6M, 1Y).
Provides a Flask web app interface for real-time stock screening.
Uses Python packages for data analysis, valuation, and visualization.

Tech Stack :-

Backend: Python, Flask

Data Analysis: Pandas, NumPy, Scikit-learn
Visualization: Matplotlib, Seaborn
Frontend: HTML, Bootstrap (via Flask templates)
Data Input: Excel (.xlsx), APIs

Strategies Implemented :-

🔸 Equal Weight Portfolio
Every selected stock has the same weight.

Lower risk concentration.

🔸 80-20 Strategy
Top 20% of value-ranked stocks get 80% of portfolio weight.

Higher conviction, potentially higher returns.

Comparison Results:-

Over shorter horizons (1M, 3M, 6M), the 80-20 strategy outperformed.

Over longer horizon (1Y), Equal Weight provided steadier returns.






