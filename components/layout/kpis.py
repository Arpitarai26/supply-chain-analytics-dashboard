# -----------------------------------------------------
# components/layout/kpis.py
# KPI Section
# -----------------------------------------------------

from dash import html


def kpi_section():
    """
    Dashboard KPI cards.
    """

    return html.Div(

        [

            # ==========================================
            # Revenue
            # ==========================================

            html.Div(

                [

                    html.P(
                        "Total Revenue",
                        className="kpi-title",
                    ),

                    html.H2(
                        id="kpi-revenue",
                        className="kpi-value",
                    ),

                    html.Span(
                        id="kpi-revenue-change",
                        className="kpi-change",
                    ),

                ],

                className="kpi-card",

            ),

            # ==========================================
            # Orders
            # ==========================================

            html.Div(

                [

                    html.P(
                        "Total Orders",
                        className="kpi-title",
                    ),

                    html.H2(
                        id="kpi-orders",
                        className="kpi-value",
                    ),

                    html.Span(
                        id="kpi-orders-change",
                        className="kpi-change",
                    ),

                ],

                className="kpi-card",

            ),

            # ==========================================
            # Pieces
            # ==========================================

            html.Div(

                [

                    html.P(
                        "Total Pieces",
                        className="kpi-title",
                    ),

                    html.H2(
                        id="kpi-pieces",
                        className="kpi-value",
                    ),

                ],

                className="kpi-card",

            ),

            # ==========================================
            # Customers
            # ==========================================

            html.Div(

                [

                    html.P(
                        "Customers",
                        className="kpi-title",
                    ),

                    html.H2(
                        id="kpi-customers",
                        className="kpi-value",
                    ),

                ],

                className="kpi-card",

            ),

            # ==========================================
            # Locations
            # ==========================================

            html.Div(

                [

                    html.P(
                        "Locations",
                        className="kpi-title",
                    ),

                    html.H2(
                        id="kpi-locations",
                        className="kpi-value",
                    ),

                ],

                className="kpi-card",

            ),

            # ==========================================
            # Business Types
            # ==========================================

            html.Div(

                [

                    html.P(
                        "Business Types",
                        className="kpi-title",
                    ),

                    html.H2(
                        id="kpi-business",
                        className="kpi-value",
                    ),

                ],

                className="kpi-card",

            ),

        ],

        className="kpi-container",

    )