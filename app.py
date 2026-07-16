# -----------------------------------------------------
# app.py
# Supply Chain Analytics Dashboard
# -----------------------------------------------------

from dash import Dash

from data_loader import load_data
from layout import create_layout
from callbacks import register_callbacks


def create_app():
    """
    Create and configure the Dash application.
    """

    # ==========================================
    # Load Dataset
    # ==========================================

    df = load_data()

    # ==========================================
    # Create Dash App
    # ==========================================

    app = Dash(
        __name__,
        title="Supply Chain Analytics Dashboard",
        suppress_callback_exceptions=True,
    )

    # Flask server
    server = app.server

    # ==========================================
    # Layout
    # ==========================================

    app.layout = create_layout(df)

    # ==========================================
    # Register Callbacks
    # ==========================================

    register_callbacks(app, df)

    return app, server


# =====================================================
# Create Application
# =====================================================

app, server = create_app()


# =====================================================
# Run
# =====================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=8051,
    )