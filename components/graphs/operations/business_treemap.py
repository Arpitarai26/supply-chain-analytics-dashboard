# -----------------------------------------------------
# operations/business_treemap.py
# Revenue by Business Segment
# -----------------------------------------------------

import plotly.express as px


def business_treemap(df, PALETTE):
    """
    Business Segment Treemap.
    """

    if df is None or df.empty:
        return px.treemap()

    # =====================================================
    # Aggregate
    # =====================================================

    business = (

        df.groupby(
            "BusinessType",
            as_index=False,
        )

        .agg(

            Revenue=("TotalRevenue", "sum"),

            Orders=("OrderCount", "sum"),

        )

    )

    business["AvgRevenuePerOrder"] = (

        business["Revenue"]

        / business["Orders"]

    )

    # =====================================================
    # Theme
    # =====================================================

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

    # =====================================================
    # Figure
    # =====================================================

    fig = px.treemap(

        business,

        path=["BusinessType"],

        values="Revenue",

        color="AvgRevenuePerOrder",

        color_continuous_scale="Viridis",

        custom_data=[
            "Orders",
            "AvgRevenuePerOrder",
        ],

    )

    fig.update_traces(

        textinfo="label+value+percent root",

        hovertemplate=

        "<b>%{label}</b><br>"

        "Revenue : $%{value:,.0f}<br>"

        "Orders : %{customdata[0]:,.0f}<br>"

        "Avg Revenue / Order : $%{customdata[1]:.2f}"

        "<extra></extra>",

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

        title="Business Segment Performance",

        height=360,

        margin=dict(

            l=15,

            r=15,

            t=55,

            b=15,

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

    )

    return fig