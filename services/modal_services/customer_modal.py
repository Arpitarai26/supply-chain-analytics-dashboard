# -----------------------------------------------------
# services/modal_services/customer_modal.py
# Customer Analytics Modal
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

from services.modal_services.summary_generator import (
    customer_summary,
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
# Customer Analytics Modal
# =====================================================

def build_customer_modal(df):

    """
    Customer Analytics Modal
    """

    # -------------------------------------------------
    # Top Customer
    # -------------------------------------------------

    revenue = (

        df.groupby("Customer")["TotalRevenue"]

        .sum()

        .sort_values(ascending=False)

    )

    customer = revenue.index[0]

    total_revenue = revenue.iloc[0]

    # -------------------------------------------------
    # Filter Dataset
    # -------------------------------------------------

    customer_df = (

        df[

            df["Customer"] == customer

        ]

        .copy()

    )

    # -------------------------------------------------
    # KPIs
    # -------------------------------------------------

    total_orders = (

        customer_df["OrderCount"]

        .sum()

    )

    total_pieces = (

        customer_df["NumberOfPieces"]

        .sum()

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

    top_locations = (

        customer_df

        .groupby("Location")["TotalRevenue"]

        .sum()

        .sort_values(ascending=False)

        .head(5)

        .index

        .tolist()

    )

    summary = customer_summary(

        df,

        customer,

    )

    # -------------------------------------------------
    # Modal Body
    # -------------------------------------------------

    body = html.Div(

        className="customer-modal",

        children=[

            # ==========================================
            # KPI GRID
            # ==========================================

            html.Div(

                [

                    metric(

                        "Customer",

                        customer,

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

                    customer_df,

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
            # Customer Analytics
            # =====================================================

            html.Div(

                [

                    # -----------------------------------------
                    # Revenue by Location
                    # -----------------------------------------

                    html.Div(

                        [

                            html.H3(

                                "Top Revenue Locations",

                                className="modal-heading",

                            ),

                            dcc.Graph(

                                figure=horizontal_bar(

                                    customer_df,

                                    category="Location",

                                    title="Top Revenue Locations",

                                    color="#2563EB",

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

                                    customer_df,

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

                customer_df,

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
            # Top Revenue Locations
            # =====================================================

            html.Div(

                [

                    html.H2(

                        "Top Revenue Locations",

                        className="modal-heading",

                    ),

                    html.Ul(

                        [

                            html.Li(location)

                            for location in top_locations

                        ],

                        className="summary-list",

                    ),

                ],

                className="modal-summary",

            ),

            html.Hr(),

            # =====================================================
            # Customer Insights
            # =====================================================

            html.Div(

                [

                    html.H2(

                        "Customer Insights",

                        className="modal-heading",

                    ),

                    html.Ul(

                        [

                            html.Li(

                                f"{customer} generated ${total_revenue:,.0f} in total revenue."

                            ),

                            html.Li(

                                f"This customer contributes {contribution:.2f}% of company revenue."

                            ),

                            html.Li(

                                f"{total_orders:,} orders produced {total_pieces:,} shipped pieces."

                            ),

                            html.Li(

                                f"Average revenue per order is ${avg_revenue:,.2f}."

                            ),

                            html.Li(

                                "Revenue trend and business distribution indicate overall customer performance."

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

                                "Maintain strong engagement with this customer through dedicated account management."

                            ),

                            html.Li(

                                "Increase operational capacity during peak demand months."

                            ),

                            html.Li(

                                "Focus on the highest-performing locations for future expansion."

                            ),

                            html.Li(

                                "Monitor monthly revenue trends to improve forecasting accuracy."

                            ),

                            html.Li(

                                "Review high-value orders to identify opportunities for increasing profitability."

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

        "🏆 Customer Analytics",

        body,

    )
