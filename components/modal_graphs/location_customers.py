# -----------------------------------------------------
# components/modal_graphs/location_customers.py
# Top Customers by Revenue
# -----------------------------------------------------

import plotly.graph_objects as go


def location_customers(df):
    """
    Top revenue-generating customers
    for the selected location.
    """

    # =====================================================
    # Aggregate Revenue
    # =====================================================

    revenue = (

        df.groupby(

            "Customer",

            as_index=False,

        )["TotalRevenue"]

        .sum()

        .sort_values(

            "TotalRevenue",

            ascending=False,

        )

        .head(10)

    )

    # Highest customer at top

    revenue = revenue.iloc[::-1]

    # =====================================================
    # Figure
    # =====================================================

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=revenue["TotalRevenue"],

            y=revenue["Customer"],

            orientation="h",

            text=[

                f"${x:,.0f}"

                for x in revenue["TotalRevenue"]

            ],

            textposition="outside",

            marker=dict(

                color="#10B981",

                line=dict(

                    color="#059669",

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

            l=40,

            r=20,

            t=40,

            b=30,

        ),

        title=dict(

            text="Top Customers",

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