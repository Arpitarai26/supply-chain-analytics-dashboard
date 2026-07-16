# -----------------------------------------------------
# callbacks/filter_callbacks.py
# Filter Callbacks
# -----------------------------------------------------

from dash import Input, Output, State


def register_filter_callbacks(app, df):
    """
    Register filter callbacks.
    """

    @app.callback(

        [

            Output("customer-dropdown", "value"),

            Output("location-dropdown", "value"),

            Output("business-dropdown", "value"),

            Output("date-range", "start_date"),

            Output("date-range", "end_date"),

        ],

        [

            Input("reset-button", "n_clicks"),

        ],

        [

            State("theme-toggle", "value"),

        ],

        prevent_initial_call=True,

    )

    def reset_filters(

        n_clicks,

        theme,

    ):

        if not n_clicks:

            return (

                [],

                [],

                [],

                df["WorkDate"].min(),

                df["WorkDate"].max(),

            )

        return (

            [],

            [],

            [],

            df["WorkDate"].min(),

            df["WorkDate"].max(),

        )