import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Step 1: Generate synthetic portfolio data
df = pd.DataFrame({
    'loan_id': range(1000),
    'balance': np.random.uniform(50000, 500000, 1000),
    'rate': np.random.normal(0.04, 0.01, 1000),
    'default_prob': np.random.uniform(0.01, 0.1, 1000),
    'ltv': np.random.uniform(0.5, 0.9, 1000)
})
base_default = df['default_prob'].mean()
base_balance = df['balance'].sum()

# Step 2: Define stress scenarios
scenarios = {
    'Baseline': {'rate_shift': 0.0, 'default_mult': 1.0, 'ltv_shift': 0.0},
    'Rate Shock': {'rate_shift': 0.02, 'default_mult': 1.2, 'ltv_shift': 0.05},
    'Downturn': {'rate_shift': 0.01, 'default_mult': 1.5, 'ltv_shift': 0.1}
}

# Step 3: Simulate portfolio under each scenario
results = {}
for scen, params in scenarios.items():
    temp = df.copy()
    temp['rate'] += params['rate_shift']
    temp['default_prob'] *= params['default_mult']
    temp['ltv'] += params['ltv_shift']
    temp['loss'] = temp['balance'] * temp['default_prob'] * temp['ltv']
    results[scen] = temp['loss'].sum()

# Step 4: Aggregate metrics
metrics = pd.DataFrame({
    'scenario': list(results.keys()),
    'total_loss': list(results.values()),
    'loss_ratio': [x / base_balance for x in results.values()]
})

# Step 5: Create refined Plotly visualization
fig = go.Figure()

# Line for total loss
fig.add_trace(go.Scatter(
    x=metrics['scenario'],
    y=metrics['total_loss'],
    name='Expected Loss',
    mode='lines+markers+text',
    line=dict(color='#FF6B6B', width=2),
    marker=dict(size=10),
    text=[f'{x:,.0f}' for x in metrics['total_loss']],
    textposition='top center',
    textfont=dict(color='white', size=12)
))

# Dashed line for baseline
fig.add_trace(go.Scatter(
    x=metrics['scenario'],
    y=[base_balance * base_default] * len(metrics),
    name='Baseline Loss',
    mode='lines',
    line=dict(color='#4ECDC4', dash='dash', width=2)
))

fig.update_layout(
    title=dict(text='Stress Test: Portfolio Loss Across Scenarios', font_color='white', x=0.5),
    xaxis=dict(
        title='Stress Scenario',
        title_font_color='white',
        tickfont=dict(color='white', size=14, family='Arial'),
        tickangle=0,
        ticks='outside',
        ticklen=6,
        gridcolor='rgba(255, 255, 255, 0.1)',
        gridwidth=0.5
    ),
    yaxis=dict(
        title='Expected Loss ($)',
        title_font_color='white',
        tickfont=dict(color='white', size=14, family='Arial'),
        tickformat=',.0f',
        ticksuffix=' USD',
        gridcolor='rgba(255, 255, 255, 0.1)',
        gridwidth=0.5
    ),
    plot_bgcolor='rgb(40, 40, 40)',
    paper_bgcolor='rgb(40, 40, 40)',
    margin=dict(l=50, r=50, t=50, b=50),
    showlegend=True,
    hovermode='x unified'
)

# Step 6: Output results
print(metrics.round(2))
fig.show()