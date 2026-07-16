# -----------------------------------------------------
# components/modal_graphs/orders_table.py
# Reusable Orders Table
# -----------------------------------------------------

from dash import html


def orders_table(
    df,
    date_col="WorkDate",
    customer_col="Customer",
    location_col="Location",
    business_col="BusinessType",
    order_col="OrderCount",
    pieces_col="NumberOfPieces",
    revenue_col="TotalRevenue",
    top_n=10,
):
    """
    Create a reusable top orders table.

    Parameters
    ----------
    df : DataFrame

    top_n : int
        Number of rows to display.
    """

    # =====================================================
    # Sort Orders
    # =====================================================

    data = (

        df.sort_values(

            revenue_col,

            ascending=False,

        )

        .head(top_n)

    )

    # =====================================================
    # Header
    # =====================================================

    header = html.Thead(

        html.Tr(

            [

                html.Th("Date"),

                html.Th("Customer"),

                html.Th("Location"),

                html.Th("Business"),

                html.Th("Orders"),

                html.Th("Pieces"),

                html.Th("Revenue"),

            ]

        )

    )

    # =====================================================
    # Rows
    # =====================================================

    rows = []

    for _, row in data.iterrows():

        rows.append(

            html.Tr(

                [

                    html.Td(row[date_col]),

                    html.Td(row[customer_col]),

                    html.Td(row[location_col]),

                    html.Td(row[business_col]),

                    html.Td(f"{row[order_col]:,}"),

                    html.Td(f"{row[pieces_col]:,}"),

                    html.Td(f"${row[revenue_col]:,.2f}"),

                ]

            )

        )

    # =====================================================
    # Table
    # =====================================================

    return html.Div(

        [

            html.Table(

                [

                    header,

                    html.Tbody(rows),

                ],

                className="modal-table",

            ),

        ],

        className="orders-table-container",

    )