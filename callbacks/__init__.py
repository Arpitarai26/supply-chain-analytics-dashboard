# -----------------------------------------------------
# callbacks/__init__.py
# Register all dashboard callbacks
# -----------------------------------------------------

from .chart_callbacks import register_chart_callbacks
from .filter_callbacks import register_filter_callbacks
from .insight_callbacks import register_insight_callbacks
from .kpi_callbacks import register_kpi_callbacks
from .theme_callbacks import register_theme_callbacks
from .modal_callbacks import register_modal_callbacks


def register_callbacks(app, df):

    register_chart_callbacks(app, df)

    register_kpi_callbacks(app, df)

    register_insight_callbacks(app, df)

    register_filter_callbacks(app, df)

    register_theme_callbacks(app)

    register_modal_callbacks(app, df)