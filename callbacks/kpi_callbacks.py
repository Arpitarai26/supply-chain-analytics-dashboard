# -----------------------------------------------------
# callbacks/kpi_callbacks.py
# KPI Callbacks
# -----------------------------------------------------

from dash import Input, Output

from services.data_filter import filter_dataframe


def register_kpi_callbacks(app, df):

    @app.callback(

        [

            Output("kpi-revenue", "children"),

            Output("kpi-orders", "children"),

            Output("kpi-pieces", "children"),

            Output("kpi-customers", "children"),

            Output("kpi-locations", "children"),

            Output("kpi-business", "children"),

            Output("kpi-revenue-change", "children"),

            Output("kpi-orders-change", "children"),

        ],

        [

            Input("customer-dropdown", "value"),

            Input("location-dropdown", "value"),

            Input("business-dropdown", "value"),

            Input("date-range", "start_date"),

            Input("date-range", "end_date"),

        ],

    )

    def update_kpis(

        customers,

        locations,

        business_types,

        start_date,

        end_date,

    ):

        # ==========================================
        # Filter Data
        # ==========================================

        filtered_df = filter_dataframe(

            df,

            customers,

            locations,

            business_types,

            start_date,

            end_date,

        )

        if filtered_df.empty:

            return (

                "$0",

                "0",

                "0",

                "0",

                "0",

                "0",

                "",

                "",

            )

        # ==========================================
        # KPI Values
        # ==========================================

        total_revenue = filtered_df["TotalRevenue"].sum()

        total_orders = filtered_df["OrderCount"].sum()

        total_pieces = filtered_df["NumberOfPieces"].sum()

        total_customers = filtered_df["Customer"].nunique()

        total_locations = filtered_df["Location"].nunique()

        total_business = filtered_df["BusinessType"].nunique()

        # ==========================================
        # Revenue / Order
        # ==========================================

        avg_revenue = (

            total_revenue / total_orders

            if total_orders

            else 0

        )

        avg_pieces = (

            total_pieces / total_orders

            if total_orders

            else 0

        )

        return (

            f"${total_revenue:,.2f}",

            f"{total_orders:,}",

            f"{total_pieces:,}",

            f"{total_customers:,}",

            f"{total_locations:,}",

            f"{total_business:,}",

            f"Avg / Order: ${avg_revenue:.2f}",

            f"Avg Pieces / Order: {avg_pieces:.2f}",

        )