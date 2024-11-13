# File: data_visualization_dashboard.py

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 30, 40]
})

# Create a Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Data Visualization Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(
        id='bar-chart',
        figure=px.bar(df, x="Category", y="Values", title="Bar Chart")
    ),
    dcc.Graph(
        id='line-chart',
        figure=px.line(df, x="Category", y="Values", title="Line Chart")
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
