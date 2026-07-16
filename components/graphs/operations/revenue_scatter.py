# -----------------------------------------------------
# operations/revenue_scatter.py
# Revenue vs Shipment Size Analysis
# -----------------------------------------------------

import plotly.express as px


def revenue_scatter(df, PALETTE):
    """
    Relationship between shipment size and revenue.
    """

    if df is None or df.empty:
        return px.scatter()

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
    # Scatter Plot
    # =====================================================

    fig = px.scatter(

        df,

        x="NumberOfPieces",

        y="TotalRevenue",

        color="BusinessType",

        size="OrderCount",

        hover_name="Customer",

        size_max=18,

        opacity=0.75,

    )

    # =====================================================
    # Traces
    # =====================================================

    fig.update_traces(

        marker=dict(

            line=dict(

                width=0.5,

                color="white",

            )

        ),

        hovertemplate=

        "<b>%{hovertext}</b><br>"

        "Business Type: %{marker.color}<br>"

        "Pieces: %{x:,}<br>"

        "Revenue: $%{y:,.2f}<br>"

        "Order Size: %{marker.size}"

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

        title="Revenue vs Shipment Size",

        height=380,

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

            l=40,

            r=20,

            t=55,

            b=30,

        ),

        legend=dict(

            orientation="h",

            y=1.05,

        ),

    )

    fig.update_xaxes(

        title="Number of Pieces",

        showgrid=True,

        gridcolor="rgba(150,150,150,0.15)",

    )

    fig.update_yaxes(

        title="Revenue ($)",

        tickprefix="$",

        showgrid=True,

        gridcolor="rgba(150,150,150,0.15)",

    )

    return fig