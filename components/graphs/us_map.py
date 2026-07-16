# -----------------------------------------------------
# us_map.py
# U.S. Revenue Distribution Map
# -----------------------------------------------------

import plotly.express as px
import plotly.graph_objects as go


def revenue_us_map(df, PALETTE):
    """
    Revenue distribution across U.S. states.
    """

    # =====================================================
    # Empty Dataset
    # =====================================================

    if (
        df is None
        or df.empty
        or "State" not in df.columns
    ):

        fig = go.Figure()

        fig.update_layout(

            title="No Geographic Data Available",

            height=430,

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

    # =====================================================
    # Aggregate Revenue
    # =====================================================

    revenue = (

        df.groupby(
            "State",
            as_index=False,
        )["TotalRevenue"]

        .sum()

        .sort_values(
            "TotalRevenue",
            ascending=False,
        )

    )

    # =====================================================
    # Choropleth
    # =====================================================

    fig = px.choropleth(

        revenue,

        locations="State",

        locationmode="USA-states",

        color="TotalRevenue",

        scope="usa",

        color_continuous_scale="Tealgrn",

        labels={

            "TotalRevenue": "Revenue ($)",

        },

        title="Revenue Distribution Across U.S. States",

    )

    # =====================================================
    # Hover
    # =====================================================

    fig.update_traces(

        hovertemplate=

        "<b>%{location}</b><br>"

        "Revenue: <b>$%{z:,.2f}</b>"

        "<extra></extra>",

    )

    # =====================================================
    # Layout
    # =====================================================

    fig.update_layout(

        height=430,

        title=dict(

            text="Revenue Distribution Across U.S. States",

            x=0.5,

            font=dict(

                size=22,

            ),

        ),

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

            size=13,

        ),

        margin=dict(

            l=20,

            r=20,

            t=70,

            b=40,

        ),

        coloraxis_colorbar=dict(

            title="Revenue",

            orientation="h",

            x=0.5,

            xanchor="center",

            y=-0.12,

            thickness=12,

            len=0.75,

        ),

        geo=dict(

            showframe=False,

            showcoastlines=False,

            bgcolor=PALETTE.get(

                "plot_bg",

                "#181818",

            ),

            landcolor=PALETTE.get(

                "plot_bg",

                "#181818",

            ),

        ),

    )

    # =====================================================
    # Highlight Best State
    # =====================================================

    if not revenue.empty:

        best = revenue.iloc[0]

        fig.add_annotation(

            text=(
                f"<b>Top Performing State</b><br>"
                f"{best['State']}<br>"
                f"${best['TotalRevenue']:,.0f}"
            ),

            xref="paper",

            yref="paper",

            x=0.98,

            y=0.02,

            xanchor="right",

            yanchor="bottom",

            showarrow=False,

            bgcolor="rgba(0,0,0,0.55)",

            bordercolor=PALETTE.get(

                "primary",

                "#00BCD4",

            ),

            borderwidth=1,

            font=dict(

                size=12,

                color=PALETTE.get(

                    "text",

                    "#E5E7EB",

                ),

            ),

        )

    return fig