# -----------------------------------------------------
# operations/top_locations.py
# Top 10 Revenue Generating Locations
# -----------------------------------------------------

import plotly.graph_objects as go


def top_locations(df, PALETTE):
    """
    Display the Top 10 revenue generating locations.
    """

    if df is None or df.empty:
        return go.Figure()

    # =====================================================
    # Aggregate Revenue
    # =====================================================

    location = (
        df.groupby("Location", as_index=False)["TotalRevenue"]
        .sum()
        .sort_values("TotalRevenue", ascending=False)
        .head(10)
        .sort_values("TotalRevenue")
    )

    # =====================================================
    # Theme
    # =====================================================

    dark = (
        PALETTE.get("background", "#121212").lower()
        in [
            "#121212",
            "#181818",
            "#000000",
            "black",
        ]
    )

    # =====================================================
    # Highlight Best Location
    # =====================================================

    colors = []

    for _, row in location.iterrows():

        if row["TotalRevenue"] == location["TotalRevenue"].max():

            colors.append("#16A34A")      # Green

        elif row["TotalRevenue"] == location["TotalRevenue"].min():

            colors.append("#DC2626")      # Red

        else:

            colors.append(
                PALETTE.get(
                    "primary",
                    "#2563EB",
                )
            )

    # =====================================================
    # Figure
    # =====================================================

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=location["TotalRevenue"],

            y=location["Location"],

            orientation="h",

            marker_color=colors,

            text=[
                f"${v:,.0f}"
                for v in location["TotalRevenue"]
            ],

            textposition="outside",

            hovertemplate=
            "<b>%{y}</b><br>"
            "Revenue: $%{x:,.0f}"
            "<extra></extra>",

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

        title="Top 10 Revenue Locations",

        height=360,

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
            l=80,
            r=40,
            t=55,
            b=20,
        ),

        showlegend=False,

    )

    fig.update_xaxes(

        title="Revenue ($)",

        tickprefix="$",

        showgrid=True,

        gridcolor="rgba(150,150,150,0.15)",

    )

    fig.update_yaxes(

        title="",

        automargin=True,

    )

    return fig