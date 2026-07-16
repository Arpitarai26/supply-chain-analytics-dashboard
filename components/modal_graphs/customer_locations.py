# -----------------------------------------------------
# components/modal_graphs/customer_locations.py
# Top Revenue Locations
# -----------------------------------------------------

import plotly.graph_objects as go


def customer_locations(df):

    # =====================================================
    # Aggregate Revenue by Location
    # =====================================================

    revenue = (

        df.groupby("Location", as_index=False)["TotalRevenue"]

        .sum()

        .sort_values("TotalRevenue", ascending=False)

        .head(10)

    )

    # Reverse for horizontal bars (highest at top)
    revenue = revenue.iloc[::-1]

    # =====================================================
    # Create Figure
    # =====================================================

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=revenue["TotalRevenue"],

            y=revenue["Location"],

            orientation="h",

            text=[
                f"${x:,.0f}"
                for x in revenue["TotalRevenue"]
            ],

            textposition="outside",

            marker=dict(

                color="#2563EB",

                line=dict(

                    color="#1D4ED8",

                    width=1,

                ),

            ),

            hovertemplate=(

                "<b>%{y}</b><br>"

                "Revenue: $%{x:,.2f}"

                "<extra></extra>"

            ),

        )

    )

    # =====================================================
    # Layout
    # =====================================================

    fig.update_layout(

        template="plotly_white",

        height=320,

        margin=dict(

            l=30,

            r=25,

            t=35,

            b=30,

        ),

        title=dict(

            text="Top Revenue Locations",

            x=0.5,

            font=dict(

                size=18,

            ),

        ),

        xaxis=dict(

            title="Revenue ($)",

            gridcolor="#E5E7EB",

            zeroline=False,

        ),

        yaxis=dict(

            title="",

            showgrid=False,

        ),

        showlegend=False,

    )

    return fig