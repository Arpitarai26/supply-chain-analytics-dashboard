# main.py — Entry point for Plotly Cloud Deployment

from dash import Dash
import os

from data_loader import load_data
from layout import create_layout
from callbacks import register_callbacks

# -----------------------------------------------------
# Initialize Dash application
# -----------------------------------------------------
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    assets_folder=os.path.join(os.getcwd(), "assets")
)

# Required by Plotly Cloud
server = app.server

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------
df = load_data("supply_chain_deliveries.csv")

# -----------------------------------------------------
# App Layout + Callbacks
# -----------------------------------------------------
app.layout = create_layout(df)
register_callbacks(app, df)
