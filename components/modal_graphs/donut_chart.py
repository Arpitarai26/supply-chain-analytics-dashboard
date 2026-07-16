# -----------------------------------------------------
# components/modal_graphs/donut_chart.py
# Reusable Donut Chart
# -----------------------------------------------------

import plotly.graph_objects as go


def donut_chart(
    df,
    category,
    value="TotalRevenue",
    title="Distribution",
):
    """
    Create a reusable donut chart.

    Parameters
    ----------
    df : DataFrame

    category : str

    value : str

    title : str
    """

    # =====================================================
    # Aggregate Data
    # =====================================================

    data = (

        df.groupby(

            category,

            as_index=False,

        )[value]

        .sum()

        .sort_values(

            value,

            ascending=False,

        )

    )

    # =====================================================
    # Colors
    # =====================================================

    colors = [

        "#2563EB",

        "#10B981",

        "#F59E0B",

        "#EF4444",

        "#8B5CF6",

        "#06B6D4",

        "#14B8A6",

        "#F97316",

    ]

    # =====================================================
    # Figure
    # =====================================================

    fig = go.Figure(

        data=[

            go.Pie(

                labels=data[category],

                values=data[value],

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
    # Center Annotation
    # =====================================================

    total = data[value].sum()

    fig.add_annotation(

        text=(

            "<b>Total</b><br>"

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

            text=title,

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