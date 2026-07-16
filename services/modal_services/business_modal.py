# -----------------------------------------------------
# services/modal_services/business_modal.py
# Business Analytics Modal
# -----------------------------------------------------

from dash import html, dcc

from components.modal_graphs.orders_table import (
    orders_table,
)

from services.modal_services.business_summary import (
    business_summary,
)

from components.modal_graphs.trend_chart import (
    trend_chart,
)

from components.modal_graphs.horizontal_bar import (
    horizontal_bar,
)

# =====================================================
# KPI Card
# =====================================================

def metric(title, value):
    """
    KPI Card
    """

    return html.Div(

        [

            html.H4(title),

            html.H2(value),

        ],

        className="modal-card",

    )


# =====================================================
# Business Modal
# =====================================================

def build_business_modal(df):

    """
    Build Business Analytics Modal.
    """

    # -------------------------------------------------
    # Highest Revenue Business Type
    # -------------------------------------------------

    revenue = (

        df.groupby("BusinessType")["TotalRevenue"]

        .sum()

        .sort_values(ascending=False)

    )

    business = revenue.index[0]

    total_revenue = revenue.iloc[0]

    # -------------------------------------------------
    # Filter Dataset
    # -------------------------------------------------

    business_df = (

        df[

            df["BusinessType"] == business

        ]

        .copy()

    )

    # -------------------------------------------------
    # KPI Calculations
    # -------------------------------------------------

    total_orders = (

        business_df["OrderCount"]

        .sum()

    )

    total_pieces = (

        business_df["NumberOfPieces"]

        .sum()

    )

    customer_count = (

        business_df["Customer"]

        .nunique()

    )

    location_count = (

        business_df["Location"]

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

    # -------------------------------------------------
    # Top Customers
    # -------------------------------------------------

    top_customers = (

        business_df

        .groupby("Customer")["TotalRevenue"]

        .sum()

        .sort_values(ascending=False)

        .head(5)

        .index

        .tolist()

    )

    # -------------------------------------------------
    # Executive Summary
    # -------------------------------------------------

    summary = business_summary(

        df,

        business,

    )

    # -------------------------------------------------
    # Layout
    # -------------------------------------------------

    body = html.Div(

        className="business-modal",

        children=[

            # ==========================================
            # KPI GRID
            # ==========================================

            html.Div(

                [

                    metric(

                        "Business Type",

                        business,

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

                        "Locations",

                        f"{location_count:,}",

                    ),

                    metric(

                        "Revenue / Order",

                        f"${avg_revenue:,.2f}",

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

                    business_df,
                    title="Monthly Revenue Trend"

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
            # Two Column Analytics
            # =====================================================

            html.Div(

                [

                    # ---------------------------------------------
                    # Revenue by Location
                    # ---------------------------------------------

                    html.Div(

                        [

                            html.H3(

                                "Top Revenue Locations",

                                className="modal-heading",

                            ),

                            dcc.Graph(

                                figure=horizontal_bar(

                                    business_df,
                                    category="Location",
                                    title="Top Revenue Locations",
                                    color="#F59E0B",

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

                    # ---------------------------------------------
                    # Top Customers
                    # ---------------------------------------------

                    html.Div(

                        [

                            html.H3(

                                "Top Customers",

                                className="modal-heading",

                            ),

                            dcc.Graph(

                                figure=horizontal_bar(

                                    business_df,
                                    category="Customer",
                                    title="Top Customers",
                                    color="#8B5CF6",

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
            # Top Revenue Orders
            # =====================================================

            html.H2(

                "Top Revenue Orders",

                className="modal-heading",

            ),

            orders_table(

                business_df,

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

                            html.Li(point)

                            for point in summary

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
            # Top Revenue Locations
            # =====================================================

            html.Div(

                [

                    html.H2(

                        "Top Locations",

                        className="modal-heading",

                    ),

                    html.Ul(

                        [

                            html.Li(location)

                            for location in (

                                business_df

                                .groupby("Location")["TotalRevenue"]

                                .sum()

                                .sort_values(ascending=False)

                                .head(5)

                                .index

                            )

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

                        "Business Insights",

                        className="modal-heading",

                    ),

                    html.Ul(

                        [

                            html.Li(

                                f"{business} generated ${total_revenue:,.0f} in revenue."

                            ),

                            html.Li(

                                f"This business contributes {contribution:.2f}% of total company revenue."

                            ),

                            html.Li(

                                f"{customer_count:,} customers generated {total_orders:,} orders."

                            ),

                            html.Li(

                                f"{location_count:,} locations participate in this business segment."

                            ),

                            html.Li(

                                f"Average revenue per order is ${avg_revenue:,.2f}."

                            ),

                            html.Li(

                                f"{total_pieces:,} total pieces were shipped."

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

                                "Expand operations in the highest-performing locations."

                            ),

                            html.Li(

                                "Prioritize high-value customers for long-term contracts."

                            ),

                            html.Li(

                                "Optimize logistics routes to reduce transportation costs."

                            ),

                            html.Li(

                                "Monitor monthly trends to improve demand forecasting."

                            ),

                            html.Li(

                                "Review high-value orders to improve operational efficiency."

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

        "🚚 Business Analytics",

        body,

    )