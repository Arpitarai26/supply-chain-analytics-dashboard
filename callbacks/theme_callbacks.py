# -----------------------------------------------------
# callbacks/theme_callbacks.py
# Dashboard Theme Callback
# -----------------------------------------------------

from dash import Input, Output


def register_theme_callbacks(app):
    """
    Handles dashboard theme switching.
    """

    @app.callback(

        Output(
            "dashboard-container",
            "className",
        ),

        Input(
            "theme-toggle",
            "value",
        ),

    )
    def update_theme(theme):

        if theme == "light":

            return "dashboard-container light"

        return "dashboard-container dark"