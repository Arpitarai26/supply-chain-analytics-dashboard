# -----------------------------------------------------
# revenue_bar.py
# Professional Revenue by Location Chart
# -----------------------------------------------------

import plotly.express as px


def revenue_by_location(df, CUSTOMER_COLORS, PALETTE):
    """
    Revenue by Location grouped by Customer.
    """

    if df is None or df.empty:
        return {}

    # =====================================================
    # Theme
    # =====================================================

    background = str(
        PALETTE.get("background", "#121212")
    ).lower()

    dark_mode = background in (
        "#121212",
        "#181818",
        "#000000",
        "black",
    )

    # =====================================================
    # Aggregate Data
    # =====================================================

    revenue = (
        df.groupby(
            ["Location", "Customer"],
            as_index=False,
        )["TotalRevenue"]
        .sum()
        .sort_values(
            "TotalRevenue",
            ascending=False,
        )
    )

    # =====================================================
    # Figure
    # =====================================================

    fig = px.bar(
        revenue,
        x="Location",
        y="TotalRevenue",
        color="Customer",
        color_discrete_map=CUSTOMER_COLORS,
        barmode="group",
    )

    # =====================================================
    # Trace Styling
    # =====================================================

    fig.update_traces(

        marker_line_width=0,

        hovertemplate=
        "<b>%{x}</b><br>"
        "Customer : %{fullData.name}<br>"
        "Revenue : <b>$%{y:,.0f}</b>"
        "<extra></extra>",

    )

    # =====================================================
    # Layout
    # =====================================================

    fig.update_layout(

        template=(
            "plotly_dark"
            if dark_mode
            else "plotly_white"
        ),

        height=320,

        autosize=True,

        title=dict(

            text="Revenue by Location",

            x=0.5,

            font=dict(
                size=18,
                family="Arial",
            ),

        ),

        hovermode="closest",

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

            b=35,

        ),

        legend=dict(

            orientation="h",

            y=1.02,

            x=0,

            bgcolor="rgba(0,0,0,0)",

            font=dict(
                size=10,
            ),

        ),

        bargap=0.20,

        bargroupgap=0.08,

    )

    # =====================================================
    # X Axis
    # =====================================================

    fig.update_xaxes(

        title="Location",

        tickangle=-15,

        tickfont=dict(
            size=10,
        ),

        showgrid=False,

        zeroline=False,

    )

    # =====================================================
    # Y Axis
    # =====================================================

    fig.update_yaxes(

        title="Revenue ($)",

        tickprefix="$",

        tickfont=dict(
            size=10,
        ),

        showgrid=True,

        zeroline=False,

        gridcolor=PALETTE.get(
            "grid",
            "rgba(255,255,255,0.08)",
        ),

    )

    return fig