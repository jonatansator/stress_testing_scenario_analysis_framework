# Stress Testing and Scenario Analysis Framework

- This Python framework simulates adverse market conditions (e.g., economic downturns, interest rate shocks) to assess their impact on a loan portfolio.
- It provides insights into potential vulnerabilities, aiding senior management in risk mitigation planning.

---

## Files
- `stress_testing_framework.py`: Main script for generating synthetic portfolio data, applying stress scenarios, and visualizing results with Plotly.
- `output.png`: Plot

---

## Libraries Used
- `pandas`
- `numpy`
- `plotly`

---

## Features
- **Data Generation**: Creates synthetic loan portfolio data with balances, interest rates, default probabilities, and loan-to-value (LTV) ratios.
- **Stress Scenarios**: Defines three scenarios:
  - Baseline: No changes.
  - Rate Shock: +2% rate, 1.2x default probability, +5% LTV.
  - Downturn: +1% rate, 1.5x default probability, +10% LTV.
- **Simulation**: Calculates expected losses under each scenario based on balance, default probability, and LTV.
- **Metrics**: Reports total loss and loss ratio (% of portfolio value) for each scenario.
- **Visualization**: Plots expected loss across scenarios with a baseline reference using Plotly.
