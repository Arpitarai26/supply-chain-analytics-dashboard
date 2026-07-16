# -----------------------------------------------------
# executive/orders_vs_revenue.py
# Monthly Orders vs Revenue
# -----------------------------------------------------

import pandas as pd
import plotly.graph_objects as go


def orders_vs_revenue(df, PALETTE):
    """
    Monthly Orders vs Revenue.
    """

    if df is None or df.empty:
        return go.Figure()

    # =====================================================
    # Copy Data
    # =====================================================

    data = df.copy()

    data["WorkDate"] = pd.to_datetime(
        data["WorkDate"],
        dayfirst=True,
        errors="coerce",
    )

    data = data.dropna(subset=["WorkDate"])

    # =====================================================
    # Monthly Aggregation
    # =====================================================

    monthly = (

        data.groupby(
            pd.Grouper(
                key="WorkDate",
                freq="ME",
            )
        )

        .agg(

            Orders=("OrderCount", "sum"),

            Revenue=("TotalRevenue", "sum"),

        )

        .reset_index()

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

    # ---------------------------
    # Orders (Bars)
    # ---------------------------

    fig.add_trace(

        go.Bar(

            x=monthly["WorkDate"],

            y=monthly["Orders"],

            name="Orders",

            marker_color=PALETTE.get(
                "secondary",
                "#F59E0B",
            ),

            hovertemplate=
            "<b>%{x|%b %Y}</b><br>"
            "Orders: %{y:,}"
            "<extra></extra>",

            yaxis="y",

        )

    )

    # ---------------------------
    # Revenue (Line)
    # ---------------------------

    fig.add_trace(

        go.Scatter(

            x=monthly["WorkDate"],

            y=monthly["Revenue"],

            mode="lines+markers",

            name="Revenue",

            line=dict(

                width=3,

                color=PALETTE.get(
                    "primary",
                    "#2563EB",
                ),

            ),

            marker=dict(size=6),

            hovertemplate=
            "<b>%{x|%b %Y}</b><br>"
            "Revenue: $%{y:,.0f}"
            "<extra></extra>",

            yaxis="y2",

        )

    )

    # =====================================================
    # Layout
    # =====================================================

    fig.update_layout(

        template=(
            "plotly_dark"
            if dark
            else "plotly_white"
        ),

        title="Monthly Orders vs Revenue",

        height=360,

        hovermode="x unified",

        margin=dict(

            l=30,

            r=30,

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
            )

        ),

        legend=dict(

            orientation="h",

            y=1.05,

        ),

        yaxis=dict(

            title="Orders",

            showgrid=True,

            gridcolor="rgba(150,150,150,0.15)",

        ),

        yaxis2=dict(

            title="Revenue ($)",

            overlaying="y",

            side="right",

            tickprefix="$",

        ),

    )

    fig.update_xaxes(

        title="",

        showgrid=False,

    )

    return fig