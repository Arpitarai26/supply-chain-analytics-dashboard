# -----------------------------------------------------
# components/kpis.py
# Modern KPI cards
# -----------------------------------------------------

from dash import html


def generate_kpis(df):
    """
    Generate KPI cards for dashboard metrics.
    """

    # =====================================================
    # Metrics
    # =====================================================

    total_orders = df["OrderCount"].sum()
    total_pieces = df["NumberOfPieces"].sum()
    total_revenue = df["TotalRevenue"].sum()

    avg_revenue = (
        total_revenue / total_orders
        if total_orders
        else 0
    )

    unique_customers = df["Customer"].nunique()

    # =====================================================
    # Card Generator
    # =====================================================

    def make_card(title, value, icon, color):

        return html.Div(

            [

                html.Div(

                    [

                        html.Div(
                            icon,
                            style={
                                "fontSize": "34px",
                            },
                        ),

                        html.Div(

                            [

                                html.Div(
                                    title,
                                    style={
                                        "fontSize": "15px",
                                        "color": "#6b7280",
                                        "fontWeight": "600",
                                    },
                                ),

                                html.Div(
                                    value,
                                    style={
                                        "fontSize": "34px",
                                        "fontWeight": "700",
                                        "color": "#111827",
                                        "marginTop": "8px",
                                    },
                                ),

                            ],

                            style={
                                "marginLeft": "18px",
                            },

                        ),

                    ],

                    style={
                        "display": "flex",
                        "alignItems": "center",
                    },

                ),

            ],

            style={
                "backgroundColor": "white",
                "borderLeft": f"6px solid {color}",
                "borderRadius": "14px",
                "padding": "22px",
                "boxShadow": "0 6px 18px rgba(0,0,0,0.08)",
                "width": "18%",
                "minWidth": "240px",
                "transition": "all .25s ease",
            },

        )

    # =====================================================
    # Cards
    # =====================================================

    return [

        make_card(
            "Total Orders",
            f"{total_orders:,}",
            "📦",
            "#2563eb",
        ),

        make_card(
            "Total Pieces",
            f"{total_pieces:,}",
            "📋",
            "#10b981",
        ),

        make_card(
            "Total Revenue",
            f"${total_revenue:,.0f}",
            "💰",
            "#f59e0b",
        ),

        make_card(
            "Avg Revenue / Order",
            f"${avg_revenue:,.2f}",
            "📈",
            "#8b5cf6",
        ),

        make_card(
            "Customers",
            f"{unique_customers:,}",
            "👥",
            "#ef4444",
        ),

    ]