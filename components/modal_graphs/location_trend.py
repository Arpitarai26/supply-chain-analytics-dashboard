# -----------------------------------------------------
# components/modal_graphs/location_trend.py
# Monthly Revenue Trend by Location
# -----------------------------------------------------

import pandas as pd
import plotly.graph_objects as go


def location_trend(df):
    """
    Monthly revenue trend for a selected location.
    """

    temp = df.copy()

    temp["WorkDate"] = pd.to_datetime(
        temp["WorkDate"],
        dayfirst=True,
        errors="coerce",
    )

    monthly = (

        temp.groupby(
            temp["WorkDate"].dt.to_period("M")
        )["TotalRevenue"]

        .sum()

        .reset_index()

    )

    monthly["WorkDate"] = monthly["WorkDate"].astype(str)

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=monthly["WorkDate"],

            y=monthly["TotalRevenue"],

            mode="lines+markers",

            line=dict(

                color="#2563EB",

                width=3,

            ),

            marker=dict(

                size=8,

                color="#2563EB",

            ),

            fill="tozeroy",

            fillcolor="rgba(37,99,235,.15)",

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

            t=40,

            b=35,

        ),

        title=dict(

            text="Monthly Revenue Trend",

            x=0.5,

            font=dict(

                size=18,

            ),

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