# -----------------------------------------------------
# revenue_business_type.py
# Professional Revenue by Business Type Chart
# -----------------------------------------------------

import plotly.express as px


def revenue_by_business_type(df, PALETTE):
    """
    Revenue by Business Type.
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

    business = (
        df.groupby(
            "BusinessType",
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
        business,
        x="BusinessType",
        y="TotalRevenue",
        color="TotalRevenue",
        color_continuous_scale="Blues",
        text_auto=".2s",
    )

    # =====================================================
    # Trace Styling
    # =====================================================

    fig.update_traces(

        textposition="outside",

        marker_line_width=0,

        hovertemplate=
        "<b>%{x}</b><br>"
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

            text="Revenue by Business Type",

            x=0.5,

            font=dict(
                size=18,
                family="Arial",
            ),

        ),

        showlegend=False,

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

        coloraxis_showscale=False,

    )

    # =====================================================
    # X Axis
    # =====================================================

    fig.update_xaxes(

        title="Business Type",

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