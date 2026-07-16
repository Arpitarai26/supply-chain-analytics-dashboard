# -----------------------------------------------------
# callbacks/modal_callbacks.py
# Executive Analytics Modal Callbacks
# -----------------------------------------------------

from dash import Input, Output, callback_context
from dash.exceptions import PreventUpdate

from services.modal_services.customer_modal import (
    build_customer_modal,
)

from services.modal_services.location_modal import (
    build_location_modal,
)

from services.modal_services.business_modal import (
    build_business_modal,
)

from services.modal_services.simple_modals import (
    highest_month_modal,
    lowest_month_modal,
    avg_revenue_modal,
    avg_pieces_modal,
    dataset_summary_modal,
)


# =====================================================
# Register Modal Callbacks
# =====================================================

def register_modal_callbacks(app, df):

    @app.callback(

        [

            Output("analytics-modal", "style"),

            Output("modal-title", "children"),

            Output("modal-body", "children"),

        ],

        [

            Input("top-customer-card", "n_clicks"),

            Input("top-location-card", "n_clicks"),

            Input("top-business-card", "n_clicks"),

            Input("highest-month-card", "n_clicks"),

            Input("lowest-month-card", "n_clicks"),

            Input("avg-revenue-card", "n_clicks"),

            Input("avg-pieces-card", "n_clicks"),

            Input("dataset-card", "n_clicks"),

            Input("close-modal", "n_clicks"),

        ],

        prevent_initial_call=True,

    )

    def open_modal(

        customer,

        location,

        business,

        highest,

        lowest,

        avg_revenue,

        avg_pieces,

        dataset,

        close,

    ):

        ctx = callback_context

        if not ctx.triggered:

            raise PreventUpdate

        trigger = ctx.triggered[0]["prop_id"].split(".")[0]

        # =====================================================
        # Close Modal
        # =====================================================

        if trigger == "close-modal":

            return (

                {"display": "none"},

                "",

                "",

            )

        # =====================================================
        # Customer Analytics
        # =====================================================

        if trigger == "top-customer-card":

            title, body = build_customer_modal(df)

        # =====================================================
        # Location Analytics
        # =====================================================

        elif trigger == "top-location-card":

            title, body = build_location_modal(df)

        # =====================================================
        # Business Analytics
        # =====================================================

        elif trigger == "top-business-card":

            title, body = build_business_modal(df)

        # =====================================================
        # Highest Revenue Month
        # =====================================================

        elif trigger == "highest-month-card":

            title, body = highest_month_modal(df)

        # =====================================================
        # Lowest Revenue Month
        # =====================================================

        elif trigger == "lowest-month-card":

            title, body = lowest_month_modal(df)

        # =====================================================
        # Average Revenue
        # =====================================================

        elif trigger == "avg-revenue-card":

            title, body = avg_revenue_modal(df)

        # =====================================================
        # Average Pieces
        # =====================================================

        elif trigger == "avg-pieces-card":

            title, body = avg_pieces_modal(df)

        # =====================================================
        # Dataset Summary
        # =====================================================

        elif trigger == "dataset-card":

            title, body = dataset_summary_modal(df)

        else:

            raise PreventUpdate

        # =====================================================
        # Open Modal
        # =====================================================

        return (

            {"display": "flex"},

            title,

            body,

        )