# -----------------------------------------------------
# services/modal_services/customer_modal.py
# Customer Analytics Modal
# -----------------------------------------------------

from dash import html, dcc

from components.modal_graphs.customer_trend import customer_trend
from components.modal_graphs.customer_locations import (
    customer_locations,
)
from components.modal_graphs.business_distribution import (
    business_distribution,
)
from components.modal_graphs.customer_orders_table import (
    customer_orders_table,
)

from services.modal_services.summary_generator import (
    customer_summary,
)


# =====================================================
# KPI Card
# =====================================================

def metric(title, value):
    """
    Creates a KPI card for the customer modal.
    """

    return html.Div(

        [

            html.H4(
                title,
            ),

            html.H2(
                value,
            ),

        ],

        className="modal-card",

    )


# =====================================================
# Customer Modal Builder
# =====================================================

def build_customer_modal(df):

    """
    Build Customer Analytics Modal.
    """

    # -------------------------------------------------
    # Revenue by Customer
    # -------------------------------------------------

    customer_revenue = (

        df.groupby("Customer")["TotalRevenue"]

        .sum()

        .sort_values(ascending=False)

    )

    customer = customer_revenue.index[0]

    total_revenue = customer_revenue.iloc[0]

    # -------------------------------------------------
    # Filter Customer
    # -------------------------------------------------

    customer_df = df[

        df["Customer"] == customer

    ].copy()

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

    # -------------------------------------------------
    # Executive Summary
    # -------------------------------------------------

    summary = customer_summary(

        df,

        customer,

    )

    # -------------------------------------------------
    # Modal Layout
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

                figure=customer_trend(customer_df),

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

                                figure=customer_locations(

                                    customer_df

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
                    # Business Distribution
                    # ---------------------------------------------

                    html.Div(

                        [

                            html.H3(

                                "Business Type Distribution",

                                className="modal-heading",

                            ),

                            dcc.Graph(

                                figure=business_distribution(

                                    customer_df

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

            customer_orders_table(

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

                            html.Li(

                                point,

                            )

                            for point in summary

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

                    html.H3(

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
            # Business Insights
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

                                f"{customer} contributes {contribution:.2f}% of the company's total revenue."

                            ),

                            html.Li(

                                f"Average revenue per order is ${avg_revenue:,.2f}."

                            ),

                            html.Li(

                                f"Total shipped pieces: {total_pieces:,}."

                            ),

                            html.Li(

                                f"Total orders processed: {total_orders:,}."

                            ),

                            html.Li(

                                "Revenue trend and business distribution charts above provide detailed operational insights."

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

                                "Prioritize operational capacity for this customer during peak demand."

                            ),

                            html.Li(

                                "Monitor the highest-performing locations and replicate their logistics practices."

                            ),

                            html.Li(

                                "Increase investment in the strongest business segment to maximize revenue."

                            ),

                            html.Li(

                                "Continuously monitor monthly revenue trends for early demand forecasting."

                            ),

                            html.Li(

                                "Review high-value orders to identify opportunities for improving customer profitability."

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
    # Return
    # =====================================================

    return (

        "🏆 Customer Analytics",

        body,

    )