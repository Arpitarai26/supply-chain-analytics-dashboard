# -----------------------------------------------------
# customer/customer_heatmap.py
# Customer × Location Revenue Heatmap
# -----------------------------------------------------

import plotly.express as px


def customer_heatmap(df, PALETTE):
    """
    Customer vs Location Revenue Heatmap.
    """

    if df is None or df.empty:
        return px.imshow([[0]])

    # =====================================================
    # Aggregate Revenue
    # =====================================================

    pivot = (

        df.pivot_table(

            index="Customer",

            columns="Location",

            values="TotalRevenue",

            aggfunc="sum",

            fill_value=0,

        )

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

    fig = px.imshow(

        pivot,

        aspect="auto",

        color_continuous_scale="Viridis",

        labels=dict(

            color="Revenue ($)"

        ),

    )

    fig.update_traces(

        hovertemplate=

        "<b>%{y}</b><br>"

        "Location : %{x}<br>"

        "Revenue : $%{z:,.0f}"

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

        title="Customer × Location Revenue",

        height=420,

        margin=dict(

            l=40,

            r=20,

            t=55,

            b=20,

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

    )

    return fig