# -----------------------------------------------------
# components/modal_graphs/horizontal_bar.py
# Reusable Horizontal Bar Chart
# -----------------------------------------------------

import plotly.graph_objects as go


def horizontal_bar(
    df,
    category,
    value="TotalRevenue",
    title="Horizontal Bar Chart",
    top_n=10,
    color="#2563EB",
):
    """
    Create a reusable horizontal bar chart.

    Parameters
    ----------
    df : DataFrame

    category : str
        Column used on Y-axis

    value : str
        Numeric column

    title : str

    top_n : int

    color : str
    """

    data = (

        df.groupby(category, as_index=False)[value]

        .sum()

        .sort_values(value, ascending=False)

        .head(top_n)

    )

    # Highest value at top
    data = data.iloc[::-1]

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=data[value],

            y=data[category],

            orientation="h",

            text=[

                f"${v:,.0f}"

                for v in data[value]

            ],

            textposition="outside",

            marker=dict(

                color=color,

                line=dict(

                    color=color,

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

    fig.update_layout(

        template="plotly_white",

        height=320,

        margin=dict(

            l=35,

            r=20,

            t=40,

            b=30,

        ),

        title=dict(

            text=title,

            x=0.5,

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