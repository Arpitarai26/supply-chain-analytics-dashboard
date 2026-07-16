# -----------------------------------------------------
# services/modal_services/location_modal.py
# Location Analytics Modal
# -----------------------------------------------------

from dash import html, dcc

from components.modal_graphs.trend_chart import (
    trend_chart,
)

from components.modal_graphs.horizontal_bar import (
    horizontal_bar,
)

from components.modal_graphs.donut_chart import (
    donut_chart,
)

from components.modal_graphs.orders_table import (
    orders_table,
)

from services.modal_services.location_summary import (
    location_summary,
)


# =====================================================
# KPI Card
# =====================================================

def metric(title, value):

    return html.Div(

        [

            html.H4(title),

            html.H2(value),

        ],

        className="modal-card",

    )


# =====================================================
# Location Analytics Modal
# =====================================================

def build_location_modal(df):

    """
    Location Analytics Modal
    """

    # -------------------------------------------------
    # Best Location
    # -------------------------------------------------

    revenue = (

        df.groupby("Location")["TotalRevenue"]

        .sum()

        .sort_values(ascending=False)

    )

    location = revenue.index[0]

    total_revenue = revenue.iloc[0]

    # -------------------------------------------------
    # Filter Dataset
    # -------------------------------------------------

    location_df = (

        df[

            df["Location"] == location

        ]

        .copy()

    )

    # -------------------------------------------------
    # KPIs
    # -------------------------------------------------

    total_orders = (

        location_df["OrderCount"]

        .sum()

    )

    total_pieces = (

        location_df["NumberOfPieces"]

        .sum()

    )

    customer_count = (

        location_df["Customer"]

        .nunique()

    )

    avg_revenue = (

        total_revenue /

        total_orders

        if total_orders

        else 0

    )

    company_revenue = (

        df["TotalRevenue"]

        .sum()

    )

    contribution = (

        total_revenue /

        company_revenue *

        100

    )

    top_customers = (

        location_df

        .groupby("Customer")["TotalRevenue"]

        .sum()

        .sort_values(ascending=False)

        .head(5)

        .index

        .tolist()

    )

    summary = location_summary(

        df,

        location,

    )

    # -------------------------------------------------
    # Modal Layout
    # -------------------------------------------------

    body = html.Div(

        className="location-modal",

        children=[

            # ==========================================
            # KPI GRID
            # ==========================================

            html.Div(

                [

                    metric(

                        "Location",

                        location,

                    ),

                    metric(

                        "Revenue",

                        f"${total_revenue:,.2f}",

                    ),

                    metric(

                        "Orders",

                        f"{total_orders:,}",

                    ),

                    metric(

                        "Pieces",

                        f"{total_pieces:,}",

                    ),

                    metric(

                        "Customers",

                        f"{customer_count:,}",

                    ),

                    metric(

                        "Revenue Share",

                        f"{contribution:.2f}%",

                    ),

                ],

                className="modal-grid",

            ),

            html.Hr(),
                        # =====================================================
            # Monthly Revenue Trend
            # =====================================================

            html.H2(

                "Monthly Revenue Trend",

                className="modal-heading",

            ),

            dcc.Graph(

                figure=trend_chart(

                    location_df,

                    title="Monthly Revenue Trend",

                ),

                config={

                    "displayModeBar": False,

                    "responsive": True,

                },

                style={

                    "height": "340px",

                    "width": "100%",

                },

            ),

            html.Hr(),

            # =====================================================
            # Analytics Section
            # =====================================================

            html.Div(

                [

                    # -----------------------------------------
                    # Top Customers
                    # -----------------------------------------

                    html.Div(

                        [

                            html.H3(

                                "Top Customers",

                                className="modal-heading",

                            ),

                            dcc.Graph(

                                figure=horizontal_bar(

                                    location_df,

                                    category="Customer",

                                    title="Top Customers",

                                    color="#10B981",

                                ),

                                config={

                                    "displayModeBar": False,

                                    "responsive": True,

                                },

                                style={

                                    "height": "320px",

                                },

                            ),

                        ],

                        className="chart-card",

                    ),

                    # -----------------------------------------
                    # Business Distribution
                    # -----------------------------------------

                    html.Div(

                        [

                            html.H3(

                                "Business Type Distribution",

                                className="modal-heading",

                            ),

                            dcc.Graph(

                                figure=donut_chart(

                                    location_df,

                                    category="BusinessType",

                                    value="TotalRevenue",

                                    title="Business Distribution",

                                ),

                                config={

                                    "displayModeBar": False,

                                    "responsive": True,

                                },

                                style={

                                    "height": "320px",

                                },

                            ),

                        ],

                        className="chart-card",

                    ),

                ],

                className="two-column-grid",

            ),

            html.Hr(),

            # =====================================================
            # Orders Table
            # =====================================================

            html.H2(

                "Top Revenue Orders",

                className="modal-heading",

            ),

            orders_table(

                location_df,

            ),

            html.Hr(),
                        # =====================================================
            # Executive Summary
            # =====================================================

            html.Div(

                [

                    html.H2(

                        "Executive Summary",

                        className="modal-heading",

                    ),

                    html.Ul(

                        [

                            html.Li(item)

                            for item in summary

                        ],

                        className="summary-list",

                    ),

                ],

                className="modal-summary",

            ),

            html.Hr(),

            # =====================================================
            # Top Customers
            # =====================================================

            html.Div(

                [

                    html.H2(

                        "Top Customers",

                        className="modal-heading",

                    ),

                    html.Ul(

                        [

                            html.Li(customer)

                            for customer in top_customers

                        ],

                        className="summary-list",

                    ),

                ],

                className="modal-summary",

            ),

            html.Hr(),

            # =====================================================
            # Operational Insights
            # =====================================================

            html.Div(

                [

                    html.H2(

                        "Operational Insights",

                        className="modal-heading",

                    ),

                    html.Ul(

                        [

                            html.Li(

                                f"{location} generated ${total_revenue:,.0f} in revenue."

                            ),

                            html.Li(

                                f"This location contributes {contribution:.2f}% of total company revenue."

                            ),

                            html.Li(

                                f"{customer_count:,} unique customers generated {total_orders:,} orders."

                            ),

                            html.Li(

                                f"{total_pieces:,} pieces were shipped from this location."

                            ),

                            html.Li(

                                f"Average revenue per order is ${avg_revenue:,.2f}."

                            ),

                            html.Li(

                                "The monthly trend and business mix indicate overall operational performance."

                            ),

                        ],

                        className="summary-list",

                    ),

                ],

                className="modal-summary",

            ),

            html.Hr(),

            # =====================================================
            # Recommendations
            # =====================================================

            html.Div(

                [

                    html.H2(

                        "Recommendations",

                        className="modal-heading",

                    ),

                    html.Ul(

                        [

                            html.Li(

                                "Increase warehouse capacity during high-demand periods."

                            ),

                            html.Li(

                                "Prioritize service for the highest-value customers."

                            ),

                            html.Li(

                                "Optimize transportation routes to reduce delivery time."

                            ),

                            html.Li(

                                "Monitor monthly revenue trends for workforce planning."

                            ),

                            html.Li(

                                "Review top-value orders regularly to improve operational efficiency."

                            ),

                        ],

                        className="summary-list",

                    ),

                ],

                className="modal-summary",

            ),

        ],

    )

    # =====================================================
    # Return Modal
    # =====================================================

    return (

        "📍 Location Analytics",

        body,

    )