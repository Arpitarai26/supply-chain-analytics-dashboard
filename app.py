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

import os

if __name__ == "__main__":

    app.run(
        debug=False,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8051)),
    )

def create_app():

    print("STEP 1: Loading data...")
    df = load_data()
    print("STEP 1 COMPLETE")

    print("STEP 2: Creating Dash app...")
    app = Dash(
        __name__,
        title="Supply Chain Analytics Dashboard",
        suppress_callback_exceptions=True,
    )
    server = app.server
    print("STEP 2 COMPLETE")

    print("STEP 3: Creating layout...")
    app.layout = create_layout(df)
    print("STEP 3 COMPLETE")

    print("STEP 4: Registering callbacks...")
    register_callbacks(app, df)
    print("STEP 4 COMPLETE")

    print("APP INITIALIZED SUCCESSFULLY")

    return app, server