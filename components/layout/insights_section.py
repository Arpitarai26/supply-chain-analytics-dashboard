# -----------------------------------------------------
# components/layout/insights_section.py
# Executive Insights Section
# -----------------------------------------------------

from dash import html


def create_card(
    icon,
    title,
    card_id,
    value_id=None,
    subtitle_id=None,
    subtitle_text=None,
    summary=False,
):
    """
    Creates a reusable executive insight card.
    """

    children = [

        html.Div(
            icon,
            className="insight-icon",
        ),

        html.H4(
            title,
            className="insight-title",
        ),

    ]

    # -------------------------------------------------
    # Dataset Summary Card
    # -------------------------------------------------

    if summary:

        children.append(

            html.P(
                "",
                id=subtitle_id,
                className="insight-summary",
            )

        )

    # -------------------------------------------------
    # Normal Cards
    # -------------------------------------------------

    else:

        if value_id:

            children.append(

                html.H2(
                    id=value_id,
                    className="insight-value",
                )

            )

        if subtitle_id:

            children.append(

                html.P(
                    "",
                    id=subtitle_id,
                    className="insight-subtitle",
                )

            )

        elif subtitle_text:

            children.append(

                html.P(
                    subtitle_text,
                    className="insight-subtitle",
                )

            )

    return html.Div(

        children,

        id=card_id,

        className="insight-card clickable-card",

        n_clicks=0,

    )


def insights_section():
    """
    Executive Insights Section
    """

    return html.Section(

        [

            # =====================================================
            # Section Title
            # =====================================================

            html.H2(
                "Executive Insights",
                className="section-title",
            ),

            # =====================================================
            # Insight Grid
            # =====================================================

            html.Div(

                [

                    create_card(
                        icon="🏆",
                        title="Top Customer",
                        card_id="top-customer-card",
                        value_id="top-customer",
                        subtitle_id="top-customer-revenue",
                    ),

                    create_card(
                        icon="📍",
                        title="Best Location",
                        card_id="top-location-card",
                        value_id="top-location",
                        subtitle_id="top-location-revenue",
                    ),

                    create_card(
                        icon="🚚",
                        title="Business Type",
                        card_id="top-business-card",
                        value_id="top-business",
                        subtitle_id="top-business-revenue",
                    ),

                    create_card(
                        icon="📈",
                        title="Highest Revenue",
                        card_id="highest-month-card",
                        value_id="highest-month",
                        subtitle_id="highest-month-revenue",
                    ),

                    create_card(
                        icon="📉",
                        title="Lowest Revenue",
                        card_id="lowest-month-card",
                        value_id="lowest-month",
                        subtitle_id="lowest-month-revenue",
                    ),

                    create_card(
                        icon="💰",
                        title="Avg Revenue / Order",
                        card_id="avg-revenue-card",
                        value_id="avg-revenue",
                        subtitle_text="Per Order",
                    ),

                    create_card(
                        icon="📦",
                        title="Avg Pieces / Order",
                        card_id="avg-pieces-card",
                        value_id="avg-pieces",
                        subtitle_text="Per Order",
                    ),

                    create_card(
                        icon="📊",
                        title="Dataset Summary",
                        card_id="dataset-card",
                        subtitle_id="dataset-summary",
                        summary=True,
                    ),

                ],

                className="insight-grid",

            ),

        ],

        className="dashboard-section",

    )