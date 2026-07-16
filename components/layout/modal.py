# -----------------------------------------------------
# components/layout/modal.py
# Executive Analytics Modal
# -----------------------------------------------------

from dash import html, dcc


def analytics_modal():

    return html.Div(

        id="analytics-modal",

        className="modal",

        style={"display": "none"},

        children=[

            html.Div(

                className="modal-content",

                children=[

                    html.Div(

                        [

                            html.H2(
                                id="modal-title",
                                children="Analytics",
                            ),

                            html.Button(
                                "✕",
                                id="close-modal",
                                n_clicks=0,
                                className="close-button",
                            ),

                        ],

                        className="modal-header",

                    ),

                    html.Hr(),

                    html.Div(

                        id="modal-body",

                    ),

                ],

            ),

        ],

    )