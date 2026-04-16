import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("daily_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig = px.line(df, x="date", y="sales", color="region",
              labels={"date": "Date", "sales": "Sales ($)", "region": "Region"},
              title="Pink Morsel Sales Over Time")

fig.add_shape(type="line",
              x0="2021-01-15", x1="2021-01-15",
              y0=0, y1=1, yref="paper",
              line=dict(color="red", dash="dash"))

fig.add_annotation(x="2021-01-15", y=1, yref="paper",
                   text="Price Increase", showarrow=False,
                   xanchor="left", font=dict(color="red"))

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "fontFamily": "Arial"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
