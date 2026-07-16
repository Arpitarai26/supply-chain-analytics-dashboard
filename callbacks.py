# -----------------------------------------------------
# callbacks.py
# Register all dashboard callbacks
# -----------------------------------------------------

from callbacks.chart_callbacks import register_chart_callbacks
from callbacks.kpi_callbacks import register_kpi_callbacks
from callbacks.insight_callbacks import register_insight_callbacks
from callbacks.filter_callbacks import register_filter_callbacks



def register_callbacks(app, df):
    """
    Register all callbacks for the dashboard.
    """

    register_chart_callbacks(app, df)

    register_kpi_callbacks(app, df)

    register_insight_callbacks(app, df)

    register_filter_callbacks(app, df)