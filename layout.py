# -----------------------------------------------------
# layout.py
# Main Dashboard Layout
# -----------------------------------------------------

from dash import html, dcc

from components.layout.header import header
from components.layout.filters import filters
from components.layout.kpis import kpi_section
from components.layout.executive_section import executive_section
from components.layout.customer_section import customer_section
from components.layout.operations_section import operations_section
from components.layout.insights_section import insights_section
from components.layout.modal import analytics_modal


def create_layout(df):
    """
    Create the complete Supply Chain Analytics Dashboard layout.
    """

    return html.Div(

        [

            # =====================================================
            # Theme Store
            # =====================================================

            dcc.Store(
                id="theme-store",
                data="dark",
            ),

            # =====================================================
            # Header
            # =====================================================

            header(),

            # =====================================================
            # Filters
            # =====================================================

            filters(df),

            # =====================================================
            # KPI Cards
            # =====================================================

            kpi_section(),

            # =====================================================
            # Executive Analytics
            # =====================================================

            executive_section(),

            # =====================================================
            # Customer Analytics
            # =====================================================

            customer_section(),

            # =====================================================
            # Operations Analytics
            # =====================================================

            operations_section(),

            # =====================================================
            # Executive Insights
            # =====================================================

            insights_section(),

            # =====================================================
            # Analytics Modal
            # =====================================================

            analytics_modal(),

            # =====================================================
            # Footer
            # =====================================================

            html.Footer(

                [

                    html.Hr(),

                    html.Div(

                        [

                            html.H3(

                                "Supply Chain Analytics Dashboard",

                                className="footer-title",

                            ),

                            html.P(

                                "Business Intelligence Platform for Supply Chain Performance Analysis",

                                className="footer-subtitle",

                            ),

                            html.Div(

                                [

                                    html.Span("Version 1.0.0"),

                                    html.Span(" • "),

                                    html.Span("Python"),

                                    html.Span(" • "),

                                    html.Span("Dash"),

                                    html.Span(" • "),

                                    html.Span("Plotly"),

                                    html.Span(" • "),

                                    html.Span("Pandas"),

                                ],

                                className="footer-tech",

                            ),

                            html.P(

                                "Developed by Arpita Rai",

                                className="footer-author",

                            ),

                            html.P(

                                "© 2026 All Rights Reserved",

                                className="footer-copyright",

                            ),

                        ],

                        className="footer-content",

                    ),

                ],

                className="dashboard-footer",

            ),

        ],

        id="dashboard-container",

        className="dashboard-container dark",

    )