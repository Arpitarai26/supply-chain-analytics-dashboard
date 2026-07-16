# -----------------------------------------------------
# components/modal_graphs/customer_orders_table.py
# Top Revenue Orders Table
# -----------------------------------------------------

from dash import html


def customer_orders_table(df):

    # ==============================================
    # Top Orders
    # ==============================================

    top_orders = (

        df.sort_values(
            "TotalRevenue",
            ascending=False,
        )

        .head(10)

    )

    # ==============================================
    # Header
    # ==============================================

    header = html.Thead(

        html.Tr(

            [

                html.Th("Date"),

                html.Th("Location"),

                html.Th("Business Type"),

                html.Th("Orders"),

                html.Th("Pieces"),

                html.Th("Revenue"),

            ]

        )

    )

    # ==============================================
    # Rows
    # ==============================================

    rows = []

    for _, row in top_orders.iterrows():

        rows.append(

            html.Tr(

                [

                    html.Td(row["WorkDate"]),

                    html.Td(row["Location"]),

                    html.Td(row["BusinessType"]),

                    html.Td(f"{row['OrderCount']:,}"),

                    html.Td(f"{row['NumberOfPieces']:,}"),

                    html.Td(f"${row['TotalRevenue']:,.2f}"),

                ]

            )

        )

    body = html.Tbody(rows)

    return html.Div(

        [

            html.H3(

                "Top Revenue Orders",

                className="modal-heading",

            ),

            html.Table(

                [

                    header,

                    body,

                ],

                className="modal-table",

            ),

        ]

    )