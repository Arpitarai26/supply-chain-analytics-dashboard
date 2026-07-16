# -----------------------------------------------------
# callbacks/insight_callbacks.py
# Executive Insight Callbacks
# -----------------------------------------------------

from dash import Input, Output

from services.data_filter import filter_dataframe
from services.executive_insights import ExecutiveInsights


def register_insight_callbacks(app, df):

    @app.callback(

        [

            Output("top-customer", "children"),
            Output("top-customer-revenue", "children"),

            Output("top-location", "children"),
            Output("top-location-revenue", "children"),

            Output("top-business", "children"),
            Output("top-business-revenue", "children"),

            Output("highest-month", "children"),
            Output("highest-month-revenue", "children"),

            Output("lowest-month", "children"),
            Output("lowest-month-revenue", "children"),

            Output("avg-revenue", "children"),
            Output("avg-pieces", "children"),

            Output("dataset-summary", "children"),

        ],

        [

            Input("customer-dropdown", "value"),
            Input("location-dropdown", "value"),
            Input("business-dropdown", "value"),
            Input("date-range", "start_date"),
            Input("date-range", "end_date"),

        ],

    )

    def update_insights(

        customers,
        locations,
        business_types,
        start_date,
        end_date,

    ):

        # ==========================================
        # Filter Dataset
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

                "-", "-",

                "-", "-",

                "-", "-",

                "-", "-",

                "-", "-",

                "-", "-",

                "No data available."

            )

        # ==========================================
        # Generate Insights
        # ==========================================

        insights = ExecutiveInsights.generate(filtered_df)

        # ==========================================
        # Dataset Summary
        # ==========================================

        summary = (

            f"{insights['total_customers']} Customers • "

            f"{insights['total_locations']} Locations • "

            f"{insights['total_business_types']} Business Types"

        )

        # ==========================================
        # Return Values
        # ==========================================

        return (

            insights["top_customer"],
            f"${insights['top_customer_revenue']:,.2f}",

            insights["top_location"],
            f"${insights['top_location_revenue']:,.2f}",

            insights["top_business_type"],
            f"${insights['top_business_revenue']:,.2f}",

            insights["highest_revenue_month"],
            f"${insights['highest_revenue']:,.2f}",

            insights["lowest_revenue_month"],
            f"${insights['lowest_revenue']:,.2f}",

            f"${insights['avg_revenue_per_order']:.2f}",
            f"{insights['avg_pieces_per_order']:.2f}",

            summary,

        )