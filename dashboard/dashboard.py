import dash
from dash import dcc, html
import plotly.express as px

app = dash.Dash(__name__)
df = None  # placeholder
fig = px.line(df, x='date', y='freight_rate') if df is not None else None

app.layout = html.Div([
    html.H1("Maritime Macro Signals"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)