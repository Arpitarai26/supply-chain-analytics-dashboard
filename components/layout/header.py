# -----------------------------------------------------
# components/layout/header.py
# Dashboard Header
# -----------------------------------------------------

from dash import html


def header():

    return html.Div(

        [

            html.Div(

                [

                    html.H1(
                        "Supply Chain Analytics Dashboard",
                        className="dashboard-title",
                    ),

                    html.P(
                        "Business Intelligence Platform for Supply Chain Performance Analysis",
                        className="dashboard-subtitle",
                    ),

                ]

            ),

        ],

        className="header-container",

    )