import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("daily_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

app.layout = html.Div(style={"fontFamily": "Arial", "backgroundColor": "#f9f9f9", "padding": "20px"}, children=[
    html.H1("Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#d63384", "marginBottom": "10px"}),
    html.P("Filter by region:", style={"textAlign": "center", "fontWeight": "bold"}),
    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={"textAlign": "center", "marginBottom": "20px", "fontSize": "16px"}
    ),
    dcc.Graph(id="sales-chart")
])

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    filtered = df if region == "all" else df[df["region"] == region]
    fig = px.line(filtered, x="date", y="sales", color="region",
                  labels={"date": "Date", "sales": "Sales ($)", "region": "Region"},
                  title="Pink Morsel Sales Over Time")
    fig.add_shape(type="line",
                  x0="2021-01-15", x1="2021-01-15",
                  y0=0, y1=1, yref="paper",
                  line=dict(color="red", dash="dash"))
    fig.add_annotation(x="2021-01-15", y=1, yref="paper",
                       text="Price Increase", showarrow=False,
                       xanchor="left", font=dict(color="red"))
    fig.update_layout(plot_bgcolor="#fff", paper_bgcolor="#f9f9f9")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
