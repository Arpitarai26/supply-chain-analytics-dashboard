# -----------------------------------------------------
# components/modal_graphs/location_business.py
# Business Type Distribution by Location
# -----------------------------------------------------

import plotly.graph_objects as go


def location_business(df):
    """
    Business Type Revenue Distribution
    for the selected location.
    """

    # =====================================================
    # Revenue by Business Type
    # =====================================================

    revenue = (

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
    # Colors
    # =====================================================

    colors = [

        "#2563EB",   # Blue
        "#10B981",   # Green
        "#F59E0B",   # Orange
        "#EF4444",   # Red
        "#8B5CF6",   # Purple
        "#06B6D4",   # Cyan

    ]

    # =====================================================
    # Figure
    # =====================================================

    fig = go.Figure(

        data=[

            go.Pie(

                labels=revenue["BusinessType"],

                values=revenue["TotalRevenue"],

                hole=0.60,

                sort=False,

                direction="clockwise",

                marker=dict(

                    colors=colors,

                    line=dict(

                        color="white",

                        width=2,

                    ),

                ),

                textinfo="percent",

                textfont=dict(

                    size=14,

                ),

                hovertemplate=(

                    "<b>%{label}</b><br>"

                    "Revenue: $%{value:,.2f}<br>"

                    "Share: %{percent}"

                    "<extra></extra>"

                ),

            )

        ]

    )

    # =====================================================
    # Total Revenue Annotation
    # =====================================================

    total = revenue["TotalRevenue"].sum()

    fig.add_annotation(

        text=(

            "<b>Total Revenue</b><br>"

            f"${total:,.0f}"

        ),

        x=0.5,

        y=0.5,

        showarrow=False,

        font=dict(

            size=16,

        ),

    )

    # =====================================================
    # Layout
    # =====================================================

    fig.update_layout(

        template="plotly_white",

        height=320,

        margin=dict(

            l=20,

            r=20,

            t=40,

            b=20,

        ),

        title=dict(

            text="Business Type Distribution",

            x=0.5,

            font=dict(

                size=18,

            ),

        ),

        legend=dict(

            orientation="h",

            y=-0.15,

            x=0.5,

            xanchor="center",

        ),

    )

    return fig