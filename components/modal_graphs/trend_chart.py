# -----------------------------------------------------
# components/modal_graphs/trend_chart.py
# Reusable Monthly Trend Chart
# -----------------------------------------------------

import pandas as pd
import plotly.graph_objects as go


def trend_chart(
    df,
    title="Monthly Revenue Trend",
    date_column="WorkDate",
    value_column="TotalRevenue",
    color="#2563EB",
):
    """
    Create a reusable monthly trend chart.

    Parameters
    ----------
    df : DataFrame

    title : str

    date_column : str

    value_column : str

    color : str
    """

    temp = df.copy()

    temp[date_column] = pd.to_datetime(

        temp[date_column],

        dayfirst=True,

        errors="coerce",

    )

    monthly = (

        temp.groupby(

            temp[date_column].dt.to_period("M")

        )[value_column]

        .sum()

        .reset_index()

    )

    monthly[date_column] = (

        monthly[date_column]

        .astype(str)

    )

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=monthly[date_column],

            y=monthly[value_column],

            mode="lines+markers",

            line=dict(

                color=color,

                width=3,

            ),

            marker=dict(

                size=8,

                color=color,

            ),

            fill="tozeroy",

            fillcolor="rgba(37,99,235,.12)",

            hovertemplate=(

                "<b>%{x}</b><br>"

                "Revenue: $%{y:,.2f}"

                "<extra></extra>"

            ),

        )

    )

    fig.update_layout(

        template="plotly_white",

        height=320,

        margin=dict(

            l=35,

            r=20,

            t=35,

            b=35,

        ),

        title=dict(

            text=title,

            x=0.5,

        ),

        xaxis=dict(

            title="Month",

            showgrid=False,

        ),

        yaxis=dict(

            title="Revenue ($)",

            gridcolor="#E5E7EB",

        ),

        hovermode="x unified",

        showlegend=False,

    )

    return fig