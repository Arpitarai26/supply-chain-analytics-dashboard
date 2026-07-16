# -----------------------------------------------------
# customer/customer_pareto.py
# Customer Pareto Analysis (80/20 Rule)
# -----------------------------------------------------

import pandas as pd
import plotly.graph_objects as go


def customer_pareto(df, PALETTE):
    """
    Customer Pareto Analysis.

    Shows which customers contribute the
    largest share of revenue.
    """

    if df is None or df.empty:
        return go.Figure()

    # ---------------------------------------------
    # Aggregate Revenue
    # ---------------------------------------------

    customer = (
        df.groupby("Customer")["TotalRevenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    # ---------------------------------------------
    # Contribution %
    # ---------------------------------------------

    total = customer["TotalRevenue"].sum()

    customer["Contribution"] = (
        customer["TotalRevenue"] / total
    ) * 100

    customer["Cumulative"] = (
        customer["Contribution"]
        .cumsum()
    )

    # ---------------------------------------------
    # Theme
    # ---------------------------------------------

    dark = (
        PALETTE.get(
            "background",
            "#121212",
        ).lower()
        in [
            "#121212",
            "#181818",
            "#000000",
            "black",
        ]
    )

    # ---------------------------------------------
    # Figure
    # ---------------------------------------------

    fig = go.Figure()

    # Revenue Bars

    fig.add_trace(

        go.Bar(

            x=customer["Customer"],

            y=customer["TotalRevenue"],

            name="Revenue",

            marker_color=PALETTE.get(
                "primary",
                "#2563EB",
            ),

            hovertemplate=
            "<b>%{x}</b><br>"
            "Revenue: $%{y:,.0f}"
            "<extra></extra>",

        )

    )

    # Cumulative %

    fig.add_trace(

        go.Scatter(

            x=customer["Customer"],

            y=customer["Cumulative"],

            mode="lines+markers",

            name="Cumulative %",

            line=dict(

                color="#EF4444",

                width=3,

            ),

            marker=dict(size=6),

            yaxis="y2",

            hovertemplate=
            "<b>%{x}</b><br>"
            "Cumulative: %{y:.1f}%"
            "<extra></extra>",

        )

    )

    # 80% Reference Line

    fig.add_hline(

        y=80,

        yref="y2",

        line_dash="dash",

        line_color="green",

        annotation_text="80%",

    )

    # ---------------------------------------------
    # Layout
    # ---------------------------------------------

    fig.update_layout(

        template="plotly_dark"
        if dark
        else "plotly_white",

        title="Customer Pareto Analysis",

        height=360,

        hovermode="x unified",

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
            )
        ),

        margin=dict(
            l=30,
            r=30,
            t=55,
            b=80,
        ),

        legend=dict(
            orientation="h",
            y=1.05,
        ),

        yaxis=dict(

            title="Revenue ($)",

            showgrid=True,

            gridcolor="rgba(150,150,150,0.15)",

        ),

        yaxis2=dict(

            title="Cumulative %",

            overlaying="y",

            side="right",

            range=[0, 100],

        ),

    )

    fig.update_xaxes(

        tickangle=-35,

        title="",

    )

    return fig