# -----------------------------------------------------
# revenue_trend.py
# Professional Revenue Trend Chart
# -----------------------------------------------------

import plotly.express as px


def revenue_over_time(df, PALETTE):
    """
    Revenue trend over time.
    """

    if df is None or df.empty:
        return {}

    # ==========================================================
    # Theme
    # ==========================================================

    background = str(
        PALETTE.get("background", "#121212")
    ).lower()

    dark_mode = background in (
        "#121212",
        "#181818",
        "#000000",
        "black",
    )

    # ==========================================================
    # Aggregate Data
    # ==========================================================

    trend = (
        df.groupby(
            "WorkDate",
            as_index=False,
        )["TotalRevenue"]
        .sum()
        .sort_values("WorkDate")
    )

    # ==========================================================
    # Figure
    # ==========================================================

    fig = px.line(
        trend,
        x="WorkDate",
        y="TotalRevenue",
        markers=True,
    )

    # ==========================================================
    # Line
    # ==========================================================

    fig.update_traces(

        line=dict(
            color=PALETTE.get(
                "primary",
                "#2563EB",
            ),
            width=3,
        ),

        marker=dict(
            size=5,
            color=PALETTE.get(
                "secondary",
                "#F59E0B",
            ),
            line=dict(
                color="white",
                width=1,
            ),
        ),

        fill="tozeroy",

        fillcolor="rgba(37,99,235,0.10)",

        hovertemplate=
        "<b>%{x}</b><br>"
        "Revenue : <b>$%{y:,.0f}</b>"
        "<extra></extra>",

    )

    # ==========================================================
    # Layout
    # ==========================================================

    fig.update_layout(

        template=(
            "plotly_dark"
            if dark_mode
            else "plotly_white"
        ),

        height=320,

        autosize=True,

        hovermode="x unified",

        showlegend=False,

        title=dict(

            text="Revenue Trend",

            x=0.5,

            font=dict(
                size=18,
                family="Arial",
            ),

        ),

        plot_bgcolor=PALETTE.get(
            "plot_bg",
            "#181818",
        ),

        paper_bgcolor=PALETTE.get(
            "plot_bg",
            "#181818",
        ),

        font=dict(

            color=PALETTE.get(
                "text",
                "#E5E7EB",
            ),

            size=12,

        ),

        margin=dict(

            l=25,

            r=20,

            t=50,

            b=20,

        ),

    )

    # ==========================================================
    # X Axis
    # ==========================================================

    fig.update_xaxes(

        title="",

        showgrid=False,

        showline=False,

        tickfont=dict(
            size=10,
        ),

    )

    # ==========================================================
    # Y Axis
    # ==========================================================

    fig.update_yaxes(

        title="Revenue ($)",

        tickprefix="$",

        showgrid=True,

        zeroline=False,

        gridcolor=PALETTE.get(
            "grid",
            "rgba(255,255,255,0.08)",
        ),

        tickfont=dict(
            size=10,
        ),

    )

    return fig