# -----------------------------------------------------
# components/layout/executive_section.py
# Executive Dashboard Section
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


def executive_section():

    return html.Section(

        [

            html.H2(
                "Executive Overview",
                className="section-title",
            ),

            html.Div(

                [

                    html.Div(

                        [

                            html.H4(
                                "Monthly Revenue Trend",
                                className="chart-title",
                            ),

                            dcc.Graph(
                                id="revenue-trend",
                                style=GRAPH_STYLE,
                                config=GRAPH_CONFIG,
                            ),

                        ],

                        className="chart-card",

                    ),

                    html.Div(

                        [

                            html.H4(
                                "Orders vs Revenue",
                                className="chart-title",
                            ),

                            dcc.Graph(
                                id="orders-vs-revenue",
                                style=GRAPH_STYLE,
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