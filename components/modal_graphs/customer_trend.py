# -----------------------------------------------------
# components/modal_graphs/customer_trend.py
# Monthly Revenue Trend
# -----------------------------------------------------

import pandas as pd
import plotly.graph_objects as go


def customer_trend(df):

    # ==============================================
    # Prepare Data
    # ==============================================

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

    monthly["WorkDate"] = (

        monthly["WorkDate"]

        .astype(str)

    )

    # ==============================================
    # Figure
    # ==============================================

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=monthly["WorkDate"],

            y=monthly["TotalRevenue"],

            mode="lines+markers",

            line=dict(

                color="#2563eb",

                width=3,

            ),

            marker=dict(

                size=8,

                color="#2563eb",

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

    # ==============================================
    # Layout
    # ==============================================

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

            text="Monthly Revenue",

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