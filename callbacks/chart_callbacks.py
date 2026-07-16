# -----------------------------------------------------
# callbacks/chart_callbacks.py
# Chart Callbacks
# -----------------------------------------------------

import importlib

from dash import Input, Output

from services.data_filter import filter_dataframe

from components.graphs.executive.revenue_trend import revenue_trend
from components.graphs.executive.orders_vs_revenue import (
    orders_vs_revenue,
)

from components.graphs.customer.customer_pareto import (
    customer_pareto,
)

from components.graphs.customer.customer_heatmap import (
    customer_heatmap,
)

from components.graphs.operations.top_locations import (
    top_locations,
)

from components.graphs.operations.business_treemap import (
    business_treemap,
)

from components.graphs.operations.revenue_scatter import (
    revenue_scatter,
)

from components.graphs.geography.us_map import (
    revenue_us_map,
)


def register_chart_callbacks(app, df):

    @app.callback(

        [

            Output(
                "revenue-trend",
                "figure",
            ),

            Output(
                "orders-vs-revenue",
                "figure",
            ),

            Output(
                "customer-pareto",
                "figure",
            ),

            Output(
                "customer-heatmap",
                "figure",
            ),

            Output(
                "top-locations",
                "figure",
            ),

            Output(
                "business-treemap",
                "figure",
            ),

            Output(
                "revenue-scatter",
                "figure",
            ),

            Output(
                "us-map",
                "figure",
            ),

        ],

        [

            Input(
                "customer-dropdown",
                "value",
            ),

            Input(
                "location-dropdown",
                "value",
            ),

            Input(
                "business-dropdown",
                "value",
            ),

            Input(
                "date-range",
                "start_date",
            ),

            Input(
                "date-range",
                "end_date",
            ),

            Input(
                "theme-toggle",
                "value",
            ),

        ],

    )

    def update_charts(

        customers,
        locations,
        business_types,
        start_date,
        end_date,
        theme,

    ):

        # ==========================================
        # Theme
        # ==========================================

        try:

            theme_module = importlib.import_module(
                f"components.colors_{theme}"
            )

        except Exception:

            theme_module = importlib.import_module(
                "components.colors_dark"
            )

        PALETTE = getattr(
            theme_module,
            "PALETTE",
        )

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

        # ==========================================
        # Return Graphs
        # ==========================================

        return (

            revenue_trend(
                filtered_df,
                PALETTE,
            ),

            orders_vs_revenue(
                filtered_df,
                PALETTE,
            ),

            customer_pareto(
                filtered_df,
                PALETTE,
            ),

            customer_heatmap(
                filtered_df,
                PALETTE,
            ),

            top_locations(
                filtered_df,
                PALETTE,
            ),

            business_treemap(
                filtered_df,
                PALETTE,
            ),

            revenue_scatter(
                filtered_df,
                PALETTE,
            ),

            revenue_us_map(
                filtered_df,
                PALETTE,
            ),

        )