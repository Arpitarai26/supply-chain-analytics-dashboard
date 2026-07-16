# -----------------------------------------------------
# executive/revenue_trend.py
# Monthly Revenue Trend with Moving Average
# -----------------------------------------------------

import pandas as pd
import plotly.graph_objects as go


def revenue_trend(df, PALETTE):
    """
    Monthly Revenue Trend with 3-Month Moving Average.
    """

    if df is None or df.empty:
        return go.Figure()

    # =====================================================
    # Copy Data
    # =====================================================

    data = df.copy()

    # =====================================================
    # Date Conversion
    # =====================================================

    data["WorkDate"] = pd.to_datetime(
        data["WorkDate"],
        dayfirst=True,
        errors="coerce",
    )

    data = data.dropna(subset=["WorkDate"])

    # =====================================================
    # Monthly Revenue
    # =====================================================

    monthly = (
        data.groupby(
            pd.Grouper(
                key="WorkDate",
                freq="M",
            )
        )["TotalRevenue"]
        .sum()
        .reset_index()
    )

    monthly["MovingAverage"] = (
        monthly["TotalRevenue"]
        .rolling(3)
        .mean()
    )

    # =====================================================
    # Theme
    # =====================================================

    background = str(
        PALETTE.get(
            "background",
            "#121212",
        )
    ).lower()

    dark = background in (
        "#121212",
        "#181818",
        "#000000",
        "black",
    )

    # =====================================================
    # Figure
    # =====================================================

    fig = go.Figure()

    # Revenue

    fig.add_trace(

        go.Scatter(

            x=monthly["WorkDate"],

            y=monthly["TotalRevenue"],

            mode="lines+markers",

            name="Revenue",

            line=dict(

                width=3,

                color=PALETTE.get(
                    "primary",
                    "#2563EB",
                ),

            ),

            marker=dict(

                size=6,

            ),

            hovertemplate=
            "<b>%{x|%b %Y}</b><br>"
            "Revenue: $%{y:,.0f}"
            "<extra></extra>",

        )

    )

    # Moving Average

    fig.add_trace(

        go.Scatter(

            x=monthly["WorkDate"],

            y=monthly["MovingAverage"],

            mode="lines",

            name="3-Month Avg",

            line=dict(

                dash="dash",

                width=3,

                color="#EF4444",

            ),

            hovertemplate=
            "<b>%{x|%b %Y}</b><br>"
            "Moving Avg: $%{y:,.0f}"
            "<extra></extra>",

        )

    )

    # =====================================================
    # Highest Month Annotation
    # =====================================================

    highest = monthly.loc[
        monthly["TotalRevenue"].idxmax()
    ]

    fig.add_annotation(

        x=highest["WorkDate"],

        y=highest["TotalRevenue"],

        text="Highest",

        showarrow=True,

        arrowhead=2,

    )

    # =====================================================
    # Lowest Month Annotation
    # =====================================================

    lowest = monthly.loc[
        monthly["TotalRevenue"].idxmin()
    ]

    fig.add_annotation(

        x=lowest["WorkDate"],

        y=lowest["TotalRevenue"],

        text="Lowest",

        showarrow=True,

        arrowhead=2,

    )

    # =====================================================
    # Layout
    # =====================================================

    fig.update_layout(

        template="plotly_dark"
        if dark
        else "plotly_white",

        title="Monthly Revenue Trend",

        height=360,

        hovermode="x unified",

        margin=dict(

            l=30,

            r=20,

            t=55,

            b=30,

        ),

        paper_bgcolor=PALETTE.get(
            "plot_bg",
            "#181818",
        ),

        plot_bgcolor=PALETTE.get(
            "plot_bg",
            "#181818",
        ),

        font=dict(

            color=PALETTE.get(
                "text",
                "#E5E7EB",
            ),

        ),

        legend=dict(

            orientation="h",

            y=1.05,

        ),

    )

    fig.update_yaxes(

        title="Revenue ($)",

        tickprefix="$",

        showgrid=True,

        gridcolor="rgba(150,150,150,0.15)",

    )

    fig.update_xaxes(

        title="",

        showgrid=False,

    )

    return fig