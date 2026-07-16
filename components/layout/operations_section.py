# -----------------------------------------------------
# components/layout/operations_section.py
# Operations Analytics Section
# -----------------------------------------------------

from dash import html, dcc


GRAPH_STYLE = {
    "height": "320px",
    "width": "100%",
}


GRAPH_CONFIG = {
    "displayModeBar": False,
    "responsive": True,
}


def operations_section():
    """
    Operations analytics section.
    """

    return html.Section(

        [

            # ==================================================
            # Section Title
            # ==================================================

            html.H2(
                "Operations Analytics",
                className="section-title",
            ),

            # ==================================================
            # First Row
            # ==================================================

            html.Div(

                [

                    # ------------------------------------------
                    # Top Revenue Locations
                    # ------------------------------------------

                    html.Div(

                        [

                            html.H4(
                                "Top Revenue Locations",
                                className="chart-title",
                            ),

                            dcc.Graph(
                                id="top-locations",
                                style=GRAPH_STYLE,
                                config=GRAPH_CONFIG,
                            ),

                        ],

                        className="chart-card",

                    ),

                    # ------------------------------------------
                    # Business Treemap
                    # ------------------------------------------

                    html.Div(

                        [

                            html.H4(
                                "Business Segment Performance",
                                className="chart-title",
                            ),

                            dcc.Graph(
                                id="business-treemap",
                                style=GRAPH_STYLE,
                                config=GRAPH_CONFIG,
                            ),

                        ],

                        className="chart-card",

                    ),

                ],

                className="two-column-grid",

            ),

            html.Br(),

            # ==================================================
            # Second Row
            # ==================================================

            html.Div(

                [

                    # ------------------------------------------
                    # Revenue Scatter
                    # ------------------------------------------

                    html.Div(

                        [

                            html.H4(
                                "Revenue vs Shipment Size",
                                className="chart-title",
                            ),

                            dcc.Graph(
                                id="revenue-scatter",
                                style=GRAPH_STYLE,
                                config=GRAPH_CONFIG,
                            ),

                        ],

                        className="chart-card",

                    ),

                    # ------------------------------------------
                    # USA Revenue Map
                    # ------------------------------------------

                    html.Div(

                        [

                            html.H4(
                                "Revenue Distribution Across USA",
                                className="chart-title",
                            ),

                            dcc.Graph(
                                id="us-map",
                                style={
                                    "height": "360px",
                                    "width": "100%",
                                },
                                config=GRAPH_CONFIG,
                            ),

                        ],

                        className="chart-card",

                    ),

                ],

                className="two-column-grid",

            ),

        ],

        className="dashboard-section",

    )