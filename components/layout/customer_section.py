# -----------------------------------------------------
# components/layout/customer_section.py
# Customer Analytics Section
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


def customer_section():

    return html.Section(

        [

            html.H2(
                "Customer Analytics",
                className="section-title",
            ),

            html.Div(

                [

                    html.Div(

                        [

                            html.H4(
                                "Customer Pareto Analysis",
                                className="chart-title",
                            ),

                            dcc.Graph(
                                id="customer-pareto",
                                style=GRAPH_STYLE,
                                config=GRAPH_CONFIG,
                            ),

                        ],

                        className="chart-card",

                    ),

                    html.Div(

                        [

                            html.H4(
                                "Customer × Location Heatmap",
                                className="chart-title",
                            ),

                            dcc.Graph(
                                id="customer-heatmap",
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