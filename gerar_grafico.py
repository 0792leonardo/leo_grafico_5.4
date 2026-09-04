from pathlib import Path
import plotly.graph_objects as go

periodos = [
    "2000-2002","2001-2003","2002-2004","2003-2005","2004-2006","2005-2007",
    "2006-2008","2007-2009","2008-2010","2009-2011","2010-2012","2011-2013",
    "2012-2014","2013-2015","2014-2016","2015-2017","2016-2018","2017-2019",
    "2018-2020","2019-2021","2020-2022","2021-2023","2022-2024","2023-2025",
    "2025-2024",
]

media_3anos = [
    51.4,49.9,44.9,40.8,37.3,37.1,38.4,36.0,36.2,36.4,37.5,35.3,
    34.7,33.2,31.8,29.3,28.8,28.6,28.2,27.8,26.9,26.7,28.6,29.3,33.5,
]

p10 = [
    41.0,41.4,36.0,34.9,33.2,33.0,34.7,32.3,31.7,32.5,34.7,32.1,
    31.2,29.5,28.6,26.2,25.6,24.7,24.3,23.8,23.4,23.0,25.1,26.0,34.5,
]

p90 = [
    70.0,63.3,57.7,48.3,42.3,42.3,45.1,42.9,41.6,40.3,39.9,37.7,
    39.2,37.9,37.1,34.3,32.1,33.4,32.3,31.0,30.1,29.7,33.0,33.4,45.5,
]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=periodos, y=p90, mode="lines",
    line=dict(width=0), showlegend=False, hoverinfo="skip"
))

fig.add_trace(go.Scatter(
    x=periodos, y=p10, mode="lines",
    line=dict(width=0),
    fill="tonexty",
    fillcolor="rgba(79,129,189,0.20)",
    name="Percentis 10/90",
    hovertemplate="Período: %{x}<br>P10: %{y:.1f} µg/m³<extra></extra>"
))

fig.add_trace(go.Scatter(
    x=periodos, y=media_3anos,
    mode="lines+markers",
    name="Média Móvel (3 anos)",
    line=dict(color="#005A9C", width=2),
    marker=dict(size=7, color="#005A9C", line=dict(color="#111111", width=1)),
    hovertemplate="Período: %{x}<br>Média móvel: %{y:.1f} µg/m³<extra></extra>"
))

fig.update_layout(
    title="",
    template="plotly_white",
    height=560,
    margin=dict(l=75, r=35, t=80, b=115),
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="top", y=-0.20, xanchor="center", x=0.5),
    xaxis=dict(title="Período de monitoramento", tickangle=-45, showgrid=False),
    yaxis=dict(title="MP₁₀ (µg/m³)", range=[0, 80], dtick=10,
               gridcolor="rgba(0,0,0,0.08)")
)

fig.write_html(
    Path("index.html"),
    include_plotlyjs=True,
    full_html=True,
    config={"responsive": True, "displaylogo": False}
)
